#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
latex generation
"""
import pandas as pd
import numpy as np


def f(number):
    if type(number) is str:
        return number
    if np.isnan(number):
        return " --- "
    if number == 0:
        return "0"
    is_negative = False
    if number < 0:
        is_negative = True
        number = -number
    sigfig = 2

    str_number = ("%.15f" % (round(number, int(-1 * floor(log10(number)) + (sigfig - 1))))).rstrip("0").rstrip(".")
    if is_negative:
        str_number = "-" + str_number
    return str_number


file = "/home/ivan/Data/bis.csv"
targetfile = "bistable.tex"
table = pd.read_csv(file, dtype=str)

label = "ca1_bis_cell_parameters"
caption = "Bistratifired cells parameters"
"""
for index, row in content.iterrows():
    for col in row[:-1]:
        print(col, end=" & ")
    
    print(row[-1], end=" ")
    print(r"\\ \hline ", end=" ")
"""
funsc = [f for _ in range(len(table.columns))]
latex_lable = table.to_latex(na_rep=" --- ", index=False, longtable=True, caption=caption, label=label, formatters=funsc) #
latex_lable = latex_lable.replace("conductance", "g_{max}")
with open(targetfile, "w") as texfile:
    texfile.write(latex_lable)