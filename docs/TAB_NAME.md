# Thread Studio tab

The native page now uses the stable name **Thread Studio**, matching Gear
Studio, Vase Studio and Box Studio. The plugin catalog title and dock action
remain Orca Thread Studio and Orca Thread Studio - Painel Lateral.

The local installer migrates only the saved `Gerador de Roscas` visibility key
to `Thread Studio` in either supported install-state filename. Hidden tabs stay
hidden, enabled tabs stay enabled, and an explicit new-name preference wins.
All other values, including permission grants, are preserved. The original
state is backed up beside the installed plugin; subsequent installs retain
that first backup. Malformed or ambiguous states are left untouched.

This fix does not change mesh generation, export, personal presets or runtime
dependencies. The bundle/wheel smoke checks assert the page name directly.
Install with OrcaSlicer closed, then reopen it to load the renamed capability.
If an active study or unsaved project is open, finish/save it before restarting.

The standalone installer contains the migration. For updates performed by a
different installer (such as OrcaCloud), review the new capability's visibility
in the plugin manager if that installer retains the old saved name.
