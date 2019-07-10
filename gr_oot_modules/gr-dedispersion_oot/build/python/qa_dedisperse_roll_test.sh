#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/python
export PATH=/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/build/swig:$PYTHONPATH
/usr/bin/python2 /home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/python/qa_dedisperse_roll.py 
