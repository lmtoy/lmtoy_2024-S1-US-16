#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-US-16"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

# 121861-897 bad

on["A262_1"] =  [ 119785, 119786, 120088, 120102, 120275,
                  121140, 121142, 121144, 121146, 121277,
                  121279, 121281, 121283, 121285, 121287, 121289,
                 -121897, # nov 6 bad
                  122041, 122043, 122045, 122047, 122049, 122051, 122055, 122057, 122059, 122061,
                  122246, 122248, 122250, 122252, 122254, 122256, 122258, 122264, 122266, 122268, 122270, 122272,]   # nov 10


on["A262_2"] =  [ 120096, 120104,-120279, 120355, 120454,
                 -121861,-121863,-121865,-121869,-121871,-121873,-121875,  # nov 6 bad
                  122278,]

on["A262_3"] =  [ 120100, 120106, 120359, 120361, 120458, 120466, 120533, 120535, 120537, 120539, 120541,
                 -121881,-121883,-121885,-121887,-121889,-121891,  # nov 6 bad
                  122027, 122029, 122031, 122033, 122035,]

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
