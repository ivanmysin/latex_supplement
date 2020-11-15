#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
latex generation
"""
import pandas as pd

file = "/home/ivan/Data/pyr.csv"

content = pd.read_csv(file, dtype=str)

for index, row in content.iterrows():
    for col in row[:-1]:
        print(col, end=" & ")
    
    print(row[-1], end=" ")
    print(r"\\ \hline ", end=" ")