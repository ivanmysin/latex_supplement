#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("/home/ivan/PycharmProjects/CA1_rhythms_model/")
import pandas as pd
from basic_parameters import get_basic_params

basic_params = get_basic_params()


raw_table = "{0} & {1} & {2} \\\\"

for celltype, params in basic_params["CellParameters"].items():
    
    
    
    try:
        iext = params["iext"]
        
        iext_std = params["iext_std"]
        
        
        line = raw_table.format(celltype, iext, iext_std)

        
        print(line)
    
    
    except KeyError:
        continue

