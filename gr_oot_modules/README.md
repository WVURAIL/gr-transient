# Legacy GNU Radio out-of-tree modules

These directories preserve GNU Radio 3.7-era XML/SWIG modules from the 2019
transient-detection project:

- `gr-dedispersion_oot/` — experimental dedispersion, pulse-detection, and
  Kelvin-to-jansky blocks
- `gr-howto/` — tutorial blocks and generated module scaffolding

They have not been ported or validated against current GNU Radio or Python
releases. For maintained related work, use
[`WVURAIL/gr-radio_astro`](https://github.com/WVURAIL/gr-radio_astro).

The historical build pattern was:

```text
mkdir build
cd build
cmake ..
make
sudo make install
```

That sequence is recorded for context, not as a supported installation
procedure. Review all commands and paths before using it in a legacy
environment. Generated build directories were removed from the archival tree
but remain in Git history.
