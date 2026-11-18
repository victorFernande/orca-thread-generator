# Dimensions, sources and experimental compatibility

## PCO-1881

Primary source: [ISBT Threadspecs](https://www.isbt.com/resources/isbt-threadspecs), PCO 1881-1 drawing **3784253-21** ([official PDF](https://cdn.prod.website-files.com/646b9f8f61d2f66e1f5d5e20/65131b77ef381c1c6e2c0daa_3784253-21.pdf)). Inspected 2026-11-18; source PDF is not redistributed.

The drawing supplies major diameter 27.40 mm, root/body diameter 24.20 mm and 2.70 mm single-start right-hand pitch. The generator uses radial depth (27.40 − 24.20)/2 = 1.60 mm and a separately defined asymmetric **simplified** tooth. It omits the controlled tooling radii and flank details, exact 650° finite thread termination, four interrupted reliefs, tamper-evident geometry and complete pressure-sealing finish. The seven-millimetre generated thread length is a printable experimental envelope, not a transcription of every axial dimension. Therefore the cap/neck is experimental and not claimed to conform fully to ISBT or retain pressure. The ISBT drawing describes a neck finish; it is not a proprietary cap-tooling specification.

## Mason 70 / 70-450

Primary source: [Comet Tool 70-450 closure sheet](https://www.comet-tool.com/wp-content/uploads/2021/08/70-450-0109-merged.pdf), inspected 2026-11-18. It gives a 70-450 closure family, 0.250 inch pitch (6.35 mm), approximately 1.25 turns, and partial closure dimensions. It marks the sheet as an advertising drawing, unsuitable for quality control, and reserves reproduction rights. This repository links the source and does not redistribute its PDF or artwork.

The model keeps a 70 mm experimental nominal envelope and 7.9375 mm threaded length (1.25 × 6.35). Radial tooth depth/shape and mating neck details are generic printable approximations because the source does not establish a complete controlled thread profile. Brand-to-brand Mason compatibility is not asserted. Measure your actual jar and calibrate.

## Mason 86

No verified full drawing was available. The software does not enlarge the Mason 70 profile. A user must supply measured major diameter, root diameter, pitch (at least 0.5 mm), threaded length (at least 3 mm) and confirm those measurements. The same simplified printable profile remains experimental; measurements alone do not certify sealing or interchangeability.

## Metric and FDM profiles

The metric mode uses an idealized 60° basic profile with external radial depth 0.61343 × pitch, a truncated crest, and no specified commercial tolerance class. FDM uses a truncated 45° tooth with depth 0.375 × pitch. Higbee attenuation smoothly reduces the male tooth at both threaded ends. Female grooves are widened axially and expanded by half the diametral clearance. Multiple starts change lead, not axial pitch. Small diameters limit tooth depth to preserve a positive root radius.

No logo, illustration or copyrighted standard document from the above publishers is bundled. The project documents simplifications so analytical/manifold tests are not mistaken for certification of external hardware.
