#!/usr/bin/env python
"""
cleans the documents build directory

"""

import os,shutil
from lpedit import NoGuiAnalysis

## clean first
if os.path.isdir("_latex"):
        shutil.rmtree("_latex")

## specify the report(s)
fileName = 'lme4.nw'
language = 'r'

## load files into project
nga = NoGuiAnalysis()
nga.load_file(fileName,fileLang=language)

## compile and create view
nga.build(fileName)
nga.compile_pdf(recompile=True)
