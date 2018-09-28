# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 21:08:11 2018

@author: nes
"""
import os
from os import listdir
from os.path import isfile, join, splitext


source_directory = "Archive"
target_directory = "inputFiles"
output_directory = "outputFiles"

for f in listdir(source_directory): 
    if isfile(join(source_directory, f)):
        ext = splitext(f)[1]
        if ext==".txt":
            with open(join(source_directory, f),"r",encoding="utf-8") as freader:
                lines = freader.readlines()
                source = lines[0].replace("\n","").strip()
                text=""
                for line in lines[2:]:
                    text+=line
                print(str(join(target_directory, f)))
                with open(join(target_directory, f),"w+",encoding="utf-8") as fwriter:
                    fwriter.write(text)
