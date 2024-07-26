#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-US-16"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["A262_1"] =  [ 119785, 119786, 120088, 120102,]

on["A262_2"] =  [ 120096, 120104,]

on["A262_3"] =  [ 120100, 120106,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["A262_1"] = "extent=240"
pars1["A262_2"] = "extent=240"
pars1["A262_3"] = "extent=240"


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["A262_1"] = "bank=0 pix_list=-13"
pars2["A262_2"] = "bank=0 pix_list=-13"
pars2["A262_3"] = "bank=0 pix_list=-13"

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
