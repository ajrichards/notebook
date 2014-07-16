#!/usr/bin/env python
"""
cleans the documents build directory
builds and compiles all specified files
"""

import os,shutil
from lpedit import NoGuiAnalysis

clean = True

## 
files = [('TwoComponentGaussian.nw','python')
          ]

## clean first
if clean == True and os.path.isdir("_latex"):
    shutil.rmtree("_latex")

## load files into project
nga = NoGuiAnalysis()
for filePath, language in files:
    nga.load_file(filePath,fileLang=language)

## build all the files
for filePath,language in files:
    fileName = os.path.split(filePath)[-1]
    if language != None:
        print 'BUILDING:', fileName
        nga.build(fileName=fileName)

## compile pdf
nga.compile_pdf()
