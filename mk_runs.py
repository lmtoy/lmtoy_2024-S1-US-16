#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-US-16"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["A262_1"] =  [ 119785, 119786, 120088, 120102, 120275, \
                  121140, 121142, 121144, 121146, 121277, \
                  121279, 121281, 121283, 121285, 121287, 121289,]

on["A262_2"] =  [ 120096, 120104,-120279, 120355, 120454,]

on["A262_3"] =  [ 120100, 120106, 120359, 120361, 120458, 120466, 120533, 120535, 120537, 120539, 120541,]

on["A262_4"] =  [ 120367, 120369, 120462, 120564, 120566, 120568, 120570, 120572, 120574, 120576, 120580, 120582, \
                  120817, 120819, 120821, 120823, 120825, \
                  120899, 120901, 120903, 120905, \
                  120996, 120998, 121000, 121002, 121004,]



# parameters for the first pass of the pipeline (restart=1 is automatically enforced here)

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}   
pars1["A262_1"] = "extent=240"                 # W=236
pars1["A262_2"] = "extent=240"                 # W=213
pars1["A262_3"] = "extent=240"                 # W=129
pars1["A262_4"] = "extent=240 dv=275 dw=375"   # W=502


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["A262_1"] = "bank=0 pix_list=-13"
pars2["A262_2"] = "bank=0 pix_list=-13"
pars2["A262_3"] = "bank=0 pix_list=-13"
pars2["A262_4"] = "bank=0 pix_list=-13"

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
