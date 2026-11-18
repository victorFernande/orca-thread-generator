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
