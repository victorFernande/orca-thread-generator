"""Exercise the ctypes D-Bus protocol and cleanup without a session bus."""

import ctypes
import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import thread_studio.linux_ipc as ipc


class Function:
    def __init__(self, call):
        self.call = call

    def __call__(self, *args):
        return self.call(*args)


class FakeBus:
    service = b"com.orcaslicer.OrcaSlicer.InstanceCheck.Object123"

    def __init__(self, case="ok"):
        self.case = case
        self.messages = {}
        self.live = set()
        self.next = 10
        self.close_count = 0
        self.connection_unref = 0
        self.sent = []
        self.flags = []
        self.pid_target = None
        self.storage = (ctypes.c_char_p * 1)(self.service)
        functions = {
            "dbus_threads_init_default": lambda: 1,
            "dbus_bus_get_private": lambda *_: 1,
            "dbus_connection_set_exit_on_disconnect": lambda *_: None,
            "dbus_message_new_method_call": self.new,
            "dbus_message_append_args": self.append,
            "dbus_connection_send_with_reply_and_block": self.reply,
            "dbus_message_get_type": lambda _: 2,
            "dbus_message_get_args": self.get_args,
            "dbus_message_unref": self.unref,
            "dbus_free_string_array": lambda _: None,
            "dbus_message_set_no_reply": lambda request, value: self.flags.append(
                ("no_reply", value)
            ),
            "dbus_message_set_auto_start": lambda request, value: self.flags.append(
                ("auto_start", value)
            ),
            "dbus_connection_send": self.send,
            "dbus_connection_flush": lambda _: None,
            "dbus_connection_get_is_connected": lambda _: self.case != "disconnect",
            "dbus_connection_close": self.close,
            "dbus_connection_unref": self.unref_connection,
        }
        for name, fn in functions.items():
            setattr(self, name, Function(fn))

    def new(self, destination, path, interface, method):
        handle = self.next
        self.next += 1
        self.messages[handle] = dict(
            destination=destination, path=path, interface=interface, method=method
        )
        self.live.add(handle)
        return handle

    def append(self, request, kind, argument, end):
        self.messages[request]["argument"] = argument._obj.value
        return 1

    def reply(self, connection, request, timeout, error):
        source = self.messages[request]
        response = self.new(b"", b"", b"", source["method"])
        self.messages[response]["argument"] = source.get("argument")
        return response

    def get_args(self, request, error, kind, *args):
        message = self.messages[request]
        if message["method"] == b"ListNames":
            ctypes.cast(args[1], ctypes.POINTER(ctypes.POINTER(ctypes.c_char_p)))[0] = (
                ctypes.cast(self.storage, ctypes.POINTER(ctypes.c_char_p))
            )
            args[2]._obj.value = 1
        elif message["method"] == b"GetNameOwner":
            args[0]._obj.value = b":1.42"
        elif message["method"] == b"GetConnectionUnixProcessID":
            self.pid_target = message["argument"]
            args[0]._obj.value = os.getpid() + (1 if self.case == "wrongpid" else 0)
        return 1

    def unref(self, message):
        if message not in self.live:
            raise AssertionError("Message unreferenced twice")
        self.live.remove(message)

    def send(self, connection, message, serial):
        self.sent.append(self.messages[message].copy())
        serial._obj.value = 7
        return self.case != "sendfail"

    def close(self, connection):
        self.close_count += 1

    def unref_connection(self, connection):
        self.connection_unref += 1


class LinuxTransportTests(unittest.TestCase):
    def test_unique_owner_routing_and_resource_cleanup(self):
        for case in ("ok", "wrongpid", "sendfail", "disconnect"):
            with self.subTest(case=case):
                fake = FakeBus(case)
                with (
                    patch.object(ipc.sys, "platform", "linux"),
                    patch.object(ipc.ctypes, "CDLL", return_value=fake),
                ):
                    ok, message = ipc.send_linux_plater_request(
                        '"orca-slicer.exe";"part.3mf"'
                    )
                self.assertEqual(ok, case == "ok")
                self.assertFalse(fake.live)
                self.assertEqual(fake.close_count, 1)
                self.assertEqual(fake.connection_unref, 1)
                self.assertEqual(fake.pid_target, b":1.42")
                if case != "wrongpid":
                    request = fake.sent[0]
                    self.assertEqual(request["destination"], b":1.42")
                    self.assertEqual(request["interface"], fake.service)
                    self.assertEqual(request["method"], b"AnotherInstance")
                    self.assertIn(("no_reply", 1), fake.flags)
                    self.assertIn(("auto_start", 0), fake.flags)
                else:
                    self.assertEqual(fake.sent, [])


if __name__ == "__main__":
    unittest.main()
