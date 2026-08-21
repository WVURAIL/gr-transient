# Known limitations

This repository is a historical research prototype, not a supported software
release.

- The modules target GNU Radio 3.7, Python 2-era APIs, XML GRC definitions,
  and SWIG. Eleven tracked Python files do not parse under Python 3.
- Flowgraphs and generated `top_block.py` contain absolute paths under
  `/home/andy/FRB_Pipeline_and_Contributions/gr-transient/`.
- The QA files are scaffolding and do not validate scientific behavior.
- `dedisperse_roll` uses circular wrapping, performs little input validation,
  and prints timing information while processing.
- `Pulse_Detection` can read beyond an array boundary near the end of its peak
  search and has empty-peak and zero-noise paths that can produce invalid
  results.
- The Kelvin-to-jansky and jansky-to-joule blocks use `10e-26`; verify the
  equations and units before use because one jansky is `1e-26 W m^-2 Hz^-1`.
- Notebook dependencies are unpinned. Several notebooks use hard-coded paths,
  and generated random data were not recorded with a reproducible seed.

The current `gr-radio_astro` implementation is not a drop-in replacement for
every experimental block here. Reimplement and test any desired behavior
rather than copying these blocks unchanged.
