"""OrcaSlicer session-bus transport. No subprocess or third-party package.

Protocol reference: OrcaSlicer v2.5.1 src/slic3r/GUI/InstanceCheck.cpp.
Transport completion does not confirm the host has loaded the objects.
"""

from __future__ import annotations

import ctypes
import os
import re
import sys


def send_linux_plater_request(
    payload: str, *, process_id: int | None = None
) -> tuple[bool, str]:
    """Send only to the Orca instance hosted in this process (or explicit PID)."""
    if not sys.platform.startswith("linux"):
        return False, "Linux session D-Bus transport is unavailable on this platform."
    if not isinstance(payload, str) or not payload or "\x00" in payload:
        return False, "The import request must be a nonempty string without NUL."
    connection = None
    library = None
    try:
        library = ctypes.CDLL("libdbus-1.so.3")
        pointer = ctypes.c_void_p
        string = ctypes.c_char_p
        uint = ctypes.c_uint32
        signatures = {
            "dbus_threads_init_default": (ctypes.c_int, []),
            "dbus_bus_get_private": (pointer, [ctypes.c_int, pointer]),
            "dbus_connection_set_exit_on_disconnect": (None, [pointer, ctypes.c_int]),
            "dbus_message_new_method_call": (pointer, [string, string, string, string]),
            "dbus_message_append_args": (ctypes.c_int, [pointer, ctypes.c_int]),
            "dbus_message_get_args": (ctypes.c_int, [pointer, pointer, ctypes.c_int]),
            "dbus_connection_send_with_reply_and_block": (
                pointer,
                [pointer, pointer, ctypes.c_int, pointer],
            ),
            "dbus_message_get_type": (ctypes.c_int, [pointer]),
            "dbus_message_set_no_reply": (None, [pointer, ctypes.c_int]),
            "dbus_message_set_auto_start": (None, [pointer, ctypes.c_int]),
            "dbus_connection_send": (
                ctypes.c_int,
                [pointer, pointer, ctypes.POINTER(uint)],
            ),
            "dbus_connection_flush": (None, [pointer]),
            "dbus_connection_get_is_connected": (ctypes.c_int, [pointer]),
            "dbus_message_unref": (None, [pointer]),
            "dbus_connection_close": (None, [pointer]),
            "dbus_connection_unref": (None, [pointer]),
            "dbus_free_string_array": (None, [ctypes.POINTER(string)]),
        }
        for name, (result, arguments) in signatures.items():
            function = getattr(library, name)
            function.restype = result
            function.argtypes = arguments
        if not library.dbus_threads_init_default():
            return False, "Unable to initialize D-Bus threading."
        connection = library.dbus_bus_get_private(0, None)
        if not connection:
            return False, "No usable session D-Bus connection; export a 3MF instead."
        library.dbus_connection_set_exit_on_disconnect(connection, 0)

        def daemon_call(method: bytes, argument: str | None = None):
            request = library.dbus_message_new_method_call(
                b"org.freedesktop.DBus",
                b"/org/freedesktop/DBus",
                b"org.freedesktop.DBus",
                method,
            )
            if not request:
                raise RuntimeError("Cannot allocate D-Bus request.")
            try:
                if argument is not None:
                    encoded = string(argument.encode("utf-8"))
                    if not library.dbus_message_append_args(
                        request, ord("s"), ctypes.byref(encoded), ctypes.c_int(0)
                    ):
                        raise RuntimeError("Cannot encode D-Bus request.")
                reply = library.dbus_connection_send_with_reply_and_block(
                    connection, request, 1500, None
                )
                if not reply:
                    raise RuntimeError("D-Bus daemon request timed out or failed.")
                if library.dbus_message_get_type(reply) != 2:
                    library.dbus_message_unref(reply)
                    raise RuntimeError("D-Bus daemon rejected the request.")
                return reply
            finally:
                library.dbus_message_unref(request)

        reply = daemon_call(b"ListNames")
        names = ctypes.POINTER(string)()
        count = ctypes.c_int()
        try:
            if not library.dbus_message_get_args(
                reply,
                None,
                ord("a"),
                ctypes.c_int(ord("s")),
                ctypes.byref(names),
                ctypes.byref(count),
                ctypes.c_int(0),
            ):
                raise RuntimeError("Invalid D-Bus service listing.")
            candidates = [names[i].decode("utf-8") for i in range(count.value)]
        finally:
            if names:
                library.dbus_free_string_array(names)
            library.dbus_message_unref(reply)
        expected_pid = os.getpid() if process_id is None else int(process_id)
        owned = []
        for name in candidates:
            if not re.fullmatch(
                r"com\.orcaslicer\.OrcaSlicer\.InstanceCheck\.Object[0-9]+", name
            ):
                continue
            try:
                reply = daemon_call(b"GetNameOwner", name)
                unique_owner = string()
                try:
                    valid = library.dbus_message_get_args(
                        reply,
                        None,
                        ord("s"),
                        ctypes.byref(unique_owner),
                        ctypes.c_int(0),
                    )
                    if not valid or not unique_owner.value:
                        continue
                    owner = unique_owner.value.decode("utf-8")
                finally:
                    library.dbus_message_unref(reply)
                reply = daemon_call(b"GetConnectionUnixProcessID", owner)
            except RuntimeError:
                continue
            pid = uint()
            try:
                valid = library.dbus_message_get_args(
                    reply, None, ord("u"), ctypes.byref(pid), ctypes.c_int(0)
                )
                if valid and pid.value == expected_pid:
                    owned.append((name, owner))
            finally:
                library.dbus_message_unref(reply)
        if len(owned) != 1:
            return (
                False,
                "Unable to identify exactly one OrcaSlicer service for this process; export a 3MF instead.",
            )
        interface, destination = owned[0]
        suffix = interface.rsplit("Object", 1)[1]
        request = library.dbus_message_new_method_call(
            destination.encode("ascii"),
            ("/com/orcaslicer/OrcaSlicer/InstanceCheck/Object" + suffix).encode(
                "ascii"
            ),
            interface.encode("ascii"),
            b"AnotherInstance",
        )
        if not request:
            return False, "Unable to allocate the import request."
        try:
            encoded = string(payload.encode("utf-8"))
            if not library.dbus_message_append_args(
                request, ord("s"), ctypes.byref(encoded), ctypes.c_int(0)
            ):
                return False, "Unable to encode the import request."
            library.dbus_message_set_no_reply(request, 1)
            library.dbus_message_set_auto_start(request, 0)
            serial = uint()
            if not library.dbus_connection_send(
                connection, request, ctypes.byref(serial)
            ):
                return False, "D-Bus could not queue the import request."
            library.dbus_connection_flush(connection)
            if not library.dbus_connection_get_is_connected(connection):
                return False, "D-Bus disconnected while sending the import request."
            return True, "Import request sent; object loading has not been confirmed."
        finally:
            library.dbus_message_unref(request)
    except (OSError, AttributeError, RuntimeError, ValueError) as error:
        return False, "Linux import unavailable: " + str(error)
    finally:
        if connection and library is not None:
            library.dbus_connection_close(connection)
            library.dbus_connection_unref(connection)
