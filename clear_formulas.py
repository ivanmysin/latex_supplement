#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sfile_path = "mmc1.tex"

file = open(sfile_path, "r")
file_content = file.read()
file.close()

file_content = file_content.replace(r"{\begin{english}", r"\begin{equation}") 
file_content = file_content.replace(r"{\end{english}", r"\end{equation}") 

file_content = file_content.replace(r"\begin{equation*}", r"\begin{equation}") 
file_content = file_content.replace(r"{\end{equation*}", r"\end{equation}") 

splited = file_content.split(r"{\normalsubformula{\text{")

file_content = ""
for sp in splited:
    sp = sp.replace("}", "", 1)
    file_content += sp

# file_content.replace("", "")

file = open("_" + sfile_path, "w")
file.write(file_content)
file.close()
