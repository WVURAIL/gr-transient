# gr-transient

> **Archive notice:** This repository is retained as a historical record of a
> 2019 GNU Radio radio-transient detector prototype. No further development or
> compatibility support is planned.

A research prototype for simulating, dedispersing, and detecting pulsar and
radio-transient signals with GNU Radio and Jupyter.

For maintained GNU Radio radio-astronomy work, see
[`WVURAIL/gr-radio_astro`](https://github.com/WVURAIL/gr-radio_astro).
Closely related 2019 dedispersion and detection work is preserved there at
[`v2019.10-dedisperse`](https://github.com/WVURAIL/gr-radio_astro/tree/v2019.10-dedisperse).
This repository remains the record for its own experimental variants,
notebooks, generated data, and test benches.

[Historical project page](https://wvurail.org/gr-transient/)

## Repository contents

- `gr_oot_modules/` — historical GNU Radio out-of-tree modules
- `jupyter/` — simulation and detection notebooks with generated data
- `historical_notebook_checkpoints/` — three unique intermediate notebook
  states retained for preservation
- `documentation/` — pipeline notes and figures
- `gr_testbenches/` — GNU Radio Companion flowgraphs and bench results
- `c/` — placeholder README; no C implementation is present

## Compatibility

The out-of-tree modules and `.grc` files use the GNU Radio 3.7-era XML/SWIG
layout. They have not been ported or tested against current GNU Radio
releases. Several examples and notebooks contain machine-specific paths and
depend on unrecorded environments. See [`KNOWN_ISSUES.md`](KNOWN_ISSUES.md)
before attempting to reuse the code or interpret its results.

## Preservation

The archival cleanup removed generated CMake build trees, compiled Python
files, and two redundant notebook autosaves. Three checkpoint notebooks with
unique historical states are retained under `historical_notebook_checkpoints/`.
All original versions, including removed generated files, remain available in
Git history.

Some legacy testbenches preserved in `gr-radio_astro` retain their original
references to the generated binary data files under `jupyter/`; those paths
and files remain unchanged here.

## Attribution and licensing

Project contributors are recorded in [`CONTRIBUTORS.md`](CONTRIBUTORS.md).
The top-level [`LICENSE`](LICENSE) supplies GNU GPL version 3 text for software
files that invoke it. Individual files and imported scaffolding retain their
own notices; see [`NOTICE`](NOTICE) and [`LICENSE-CMake.txt`](LICENSE-CMake.txt).
