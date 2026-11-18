# Validation status

Recorded on 2026-11-18 for version 1.0.0.

## Verified locally

- Python 3.12.13 with NumPy 2.5.5: all 25 unittest cases pass with `-B -W error`.
- Independent mesh checks cover closed oriented edges, nondegenerate float32 surfaces, positive volume and topology appropriate to each part.
- Section tests on the actual mating meshes verify positive clearance after lid inversion, including low-resolution three-start threads with 0.05 mm diametral clearance.
- Invalid measured dimensions and requests exceeding the mesh budget are rejected before expensive allocations.
- Standalone single-file bundles and the extracted wheel load independently of the source directory.
- Generated JavaScript passes Node.js syntax checking. Chromium browser rendering with a local test bridge verifies the default geometry, English/Portuguese interface, theme changes, representative presets, multistart lead, undo/redo, calibration parts, 3MF export and compact dock rendering.
- The Linux transport has isolated tests for unique-owner routing, wrong process identity, send failure, disconnection and resource cleanup. These are simulated transport checks rather than a live Linux OrcaSlicer session.

## Pending validation

- Live native page/dock activation, permission handling and Plater delivery inside OrcaSlicer on all three operating systems.
- Real printed thread engagement, printer/material calibration, insert or external hardware compatibility, sealing and mechanical behavior.
- Hardware-specific frame rate and calibration print duration.

PCO-1881 and Mason profiles remain experimental as described in [dimension sources](STANDARDS_AND_SOURCES.md). Passing software checks does not establish interchangeability with a physical bottle or jar.

The repository's CI independently builds and tests the same source on Windows, macOS and Linux. Its run history provides the current cross-platform result.


## Version 1.0.1 corrective verification

The version 1.0.0 results above remain the historical baseline. On 2026-11-18, version 1.0.1 passed all **35** local unittest cases with Python 3.12.13, NumPy 2.5.5 and `-B -W error` (15.60 seconds). The build command with `--no-install` also passed bundle/wheel registration, embedded-icon and standalone smoke checks. This patch was not installed by the patch tests.

The additional regressions verify that explicitly supplied invalid printer dimensions and height aliases fail, including `None`, nonfinite values, zero and malformed strings. Defaults apply only to absent limits. Valid height aliases use key-presence precedence (`max_z`, `bed_z`, `printable_height`), direct host values before nested printer values; an invalid lower-priority supplied alias still fails.

Object names and project titles containing characters forbidden by XML 1.0 are rejected before a 3MF archive is written. Valid Unicode names and escaped XML punctuation still parse successfully.

The installer now validates the resolved dedicated plugin directory and cache-removal paths. Bundle and icon destinations are replaced with same-directory temporary files and `os.replace`, rather than being opened through existing links. A real hard-link regression verifies that external original files remain unchanged, install-state metadata survives, and failed replacement cleans temporary files while preserving the old destination.

Both single-file distributions now embed the complete MIT license and original copyright notices as comments immediately after the PEP 723 metadata. The wheel continues to include `LICENSE`.

Cross-platform CI for version 1.0.1 and all live native-application/physical-print checks remain pending at this local verification point. No live OrcaSlicer interaction was performed for this patch.
