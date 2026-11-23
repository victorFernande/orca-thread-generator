# Data-only standalone packing

Compress only the offline HTML/CSS/JavaScript literal in the standalone
bundle; restore it with Python's standard-library Base64/zlib. Keep executable
Python bridge code readable. The source package and wheel keep their original
document. No geometry or parameter changes are part of this packaging patch.

Regression tests verify exact UTF-8 bytes, surrounding bridge preservation,
rejection of ambiguous/computed template assignments, and whole-module AST
equivalence after restoring the real document.

Measured against the local 1.1.0 development snapshot, the standalone bundle
decreased from 246,572 to 168,467 bytes (31.68%). All 71 local Python tests and
page/dock template interactions passed. The Windows native review generated a
three-start jar (3 mm pitch, 9 mm lead), exported its 3MF, then selected a
left-hand M20 bolt in the sidebar and exported bolt/nut STLs.

The UI overhaul present in that local snapshot is separate, pre-existing work
and is intentionally excluded from this additive packaging PR. The 31.68%
measurement describes that local snapshot, not an unchanged 1.0.1 release.
No print-fit or macOS/Linux application validation is implied.
