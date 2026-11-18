# Orca Thread Studio — user manual

## First model

Open **Gerador de Roscas** or the **Orca Thread Studio — Painel Lateral** script. Choose a library project, then edit nominal diameter, axial pitch, threaded length, handedness and starts. Lead is pitch × starts. Diametral clearance is the total diameter difference; radial clearance is half of it.

Before a full print, select **3 calibration rings**. One, two or three physical notches identify diametral clearances of 0.10, 0.18 and 0.26 mm. Test the rings against the corresponding male part. They do not replace a measured hardware gauge. Select the clearance that works with your actual filament, printer and orientation.

## Model families

**Container and lid:** choose body diameter/height, wall/floor thickness and texture. Threads belong to the upper outside of the container and the inside of the matching lid. The lid prints open side up. The optional gasket channel is a real annular recess in the inside floor, with width, depth and inset controls. A channel does not establish liquid-tight performance.

**Bottle cap or neck:** the cap is closed and the neck has an open passage. PCO-1881 and Mason 70 use explicitly experimental simplified envelopes. Mason 86 requires measured major/root diameters, pitch and threaded length plus explicit confirmation before generation. These are not certified interchangeable bottle closures.

**Hose/vacuum adapter:** choose inlet/outlet size, overall length and end length. Independently select smooth tapered, barb, male thread or female thread at each end. Smooth/barbed diameters describe the clear bore; threaded diameters describe nominal thread diameter. Impossible wall/bore combinations fail explicitly.

**Bolt and nut:** hex, knurled and wing heads are available. Zero bolt bore makes a solid bolt; a positive bore makes a through passage. The nut is open. Metric profiles are idealized printable approximations without a certified tolerance class.

## Preview and workflow

Drag to orbit, wheel to zoom and use **Fit view** to reset the camera. Axial section reveals the internal thread. Opening separates the mating parts. Screw motion combines rotation and axial travel using the actual lead. The 2D loupe follows the position, marking analytical interference or no engagement; it does not simulate plastic deformation, friction or stress.

The dock offers Parameters, Preview and Export tabs. Page and dock share the same loaded controller, user presets and undo/redo history. Reset restores the initial parameters. PT/EN changes language and the theme button toggles light/dark.

Select all parts, primary, secondary or calibration. STL writes individual part files; 3MF retains multiple objects and optional mechanical slicing defaults. Original-scale packing rejects a bed that is too small. Export parts separately or choose a larger printer.

Send to plater prepares the file and waits for native transport completion. A sent request is not proof that object loading finished: check the actual OrcaSlicer plater. If host transport fails, open the export folder and import the 3MF manually. User presets and exports stay in local plugin storage. No server is contacted during modeling.

Always validate physical fit with a print. No food, pressure, sealing or structural performance is asserted. Print time depends on the real slicing profile; the original six-minute calibration target is not guaranteed.
