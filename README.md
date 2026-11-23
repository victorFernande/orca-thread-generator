# Orca Thread Studio

Offline parametric thread, bottle and adapter generator for **OrcaSlicer 2.5.1+**.

![Studio icon](assets/icon.svg)

English and Brazilian Portuguese interface, a full studio tab and a compact dock. Version 1.1 adopts the **Orca Vase Studio template**: compact header, filtered preset gallery, parameter cards, paired sliders/numeric fields, floating inspection tools and a fixed export footer. See [template provenance](docs/UI_TEMPLATE.md).

## Features

- Containers with matched screw lids, smooth/fluted/knurled/faceted bodies and an optional gasket groove.
- ISO-inspired 60° and FDM 45° profiles, right/left handedness, one to three starts, Higbee run-in/out and independent diametral/axial clearance.
- Bottle caps and open necks: experimental PCO-1881 and Mason 70; Mason 86 requires measured dimensions and explicit confirmation.
- Smooth tapered, barbed, externally threaded and internally threaded hose/vacuum adapter ends.
- Solid or hollow bolts and nuts with hex, knurled or wing shapes.
- Twelve bilingual presets, editable user presets, shared page/dock state, undo, redo and reset.
- Three calibration rings with physical 1/2/3 notch markings and 0.10/0.18/0.26 mm diametral clearances.
- WebGL2 preview of the **same vertices and triangles exported**, axial clipping, screw-motion animation and a 2D analytical engagement loupe that follows opening and rotation.
- Binary STL and multi-object 3MF, original-scale bed packing and mechanical slicing defaults.

## Install

Use `dist/orca_thread_generator.py` as the single-file native plugin. Install it using the OrcaSlicer plugin interface, or run the local installer with the Python interpreter bundled with OrcaSlicer:

```powershell
& 'C:\Program Files\OrcaSlicer\python\python.exe' -B scripts/build_and_install.py
```

The installer writes only this plugin's directory, `orca_plugins/orca_thread_generator`, under the OrcaSlicer user data directory. It does not change sibling plugins. The SVG icon is embedded and can materialize automatically if only the Python bundle is installed. A universal `_any.py` bundle and a pure Python wheel are also included. No marketplace submission is performed.

After installing or updating, **close and reopen OrcaSlicer** to load the new bundle. In **Plugins**, check the version and enable **Orca Thread Studio**. Replacing the file while OrcaSlicer is running does not reload the plugin already held in memory.

## Develop and verify

All 68 local version 1.1.0 tests passed. In OrcaSlicer 2.5.1 on Windows, a native session using the 1.1.0 interface before the final theme adapters confirmed page activation, real geometry generation, 3MF export, WM_COPYDATA delivery and the container base/lid visibly loaded on the Plater. The final dock and final theme adapters still need native verification; live macOS/Linux integration also remains pending. No slicing, printing or physical fit test was performed. See [validation status](docs/VALIDATION.md).

Python >=3.12 and NumPy >=1.26 are required. Runtime generation is offline. The OrcaSlicer shared Python package directory is discovered if NumPy is not on the standard import path.

```powershell
& 'C:\Program Files\OrcaSlicer\python\python.exe' -B scripts/build_and_install.py --no-install
& 'C:\Program Files\OrcaSlicer\python\python.exe' -B -W error -m unittest discover -s tests -v
```

The tests cover closed oriented topology, nondegenerate faces, genus, actual mating mesh cross sections, all adapter end combinations, calibration markings, profile math, asynchronous delivery status, preset persistence, JavaScript syntax and standalone bundle/wheel loading. Node.js adds the JavaScript syntax check when available. CI exercises Windows, macOS and Linux; its simulated host checks complement the limited Windows native evidence recorded above. Live macOS/Linux integration and final Windows dock/theme checks remain pending.

## Important engineering limits

The ISO mode is an idealized metric profile, not a certified tolerance class or gauge. External hardware fits require calibration. Diametral clearance is a diameter difference; the nominal radial gap is half that value. Multi-start lead equals **pitch × starts**. Hardware parts are not rated for structural or pressure service.

PCO and Mason selections are explicitly **experimental**. PCO uses the published 27.40 mm major diameter, 24.20 mm root/body diameter and 2.70 mm pitch from ISBT drawing 3784253-21, with a simplified asymmetric radial tooth. Tooling radii, precise 650° thread termination, the four interrupted reliefs, tamper-evident features and the complete sealing finish are not reproduced. It is not an interchangeable certified bottle closure.

Mason 70 is an experimental starting envelope informed by a 70-450 closure drawing: 6.35 mm pitch and approximately 1.25 turns. The drawing supplies partial advertising dimensions, not a complete controlled mating-thread specification. Mason 86 is **not** a scaled copy: generation is blocked until the user supplies major/root diameters, pitch and thread length and confirms measurement. Both Mason profiles remain experimental and require a test print.

No food-contact, liquid-tight, pressure-retaining or load-bearing performance is asserted. Printing times are determined by the selected printer/material and slicer settings; the original six-minute calibration target is not a promise. This project does not transmit models or presets to a server.

The loupe reports analytical radial/flank clearance at the displayed screw position. It is not a deformation, friction, leakage or stress simulation. WebGL2 performance depends on the embedded browser/GPU and selected mesh resolution; no fixed frame rate is guaranteed.

## Export and host delivery

STL and 3MF files are saved to the plugin's local storage, not into this repository. 3MF uses five walls, five top/bottom layers, 30% gyroid infill and a pitch-dependent fine layer height when automatic slicing defaults are enabled. The current printer's process snapshot and bed are included when available. Oversize layouts are rejected without scaling the model.

Windows sends to the active process's Plater through WM_COPYDATA. macOS schedules Cocoa file opening on the main queue. Linux uses the current process's D-Bus instance service and a unique-owner check, without shell commands. A completed transport is reported as **request sent**, never as proof that object loading finished. Failure keeps the exported file available for manual import.

Open the exported 3MF as a project, or use an empty plate. If importing it as geometry into an existing project, arrange the objects before slicing. In the Windows validation session, importing Thread geometry into a project already containing Box objects caused overlap; import delivery does not arrange pre-existing objects.

## Public repository hygiene

Each plugin is a separate project. Source, tests, documentation, icons and reviewed distribution bundles are public deliverables. Exported user models, presets, local configuration, credentials, logs, temporary files, environments and editor state belong outside tracked source. A gitignore does not remove already tracked secrets: review the actual staged files before publishing.

## Documentation and provenance

- [Manual em Português](docs/MANUAL_PT-BR.md)
- [English manual](docs/MANUAL_EN.md)
- [Technical geometry notes](docs/GEOMETRY_AND_VALIDATION.md)
- [Validation status](docs/VALIDATION.md)
- [Source dimensions and compatibility limits](docs/STANDARDS_AND_SOURCES.md)
- [Community listing draft](docs/COMMUNITY_LISTING.md)

The packager, exporters and native host transport derive from the sibling Orca Gear Studio / Orca Vase Studio projects under MIT. Original copyright notices remain in `LICENSE`. No third-party bottle drawing or copyrighted PDF is redistributed.
