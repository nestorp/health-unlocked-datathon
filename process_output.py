# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 22:24:42 2018

@author: nes
"""

import xml.etree.ElementTree as ET 
import os
from os import listdir
from os.path import isfile, join, splitext

#filename = "outputFiles/fibromyalgia-action-uk_718c2b6b1941fa5f4b0853215c70ff9b.txt.xmi"

outputDir = "outputFiles"
finalDir = "processedFiles"

sofaTag = "{http:///uima/cas.ecore}Sofa"
classTag = "{http:///org/apache/ctakes/typesystem/type/textsem.ecore}"

tagDic = {classTag + "MedicationMention":"DRUG",
          classTag +"SignSymptomMention":"SYMPTOM",
           #classTag +"AnatomicalSiteMention":"BODYPART",
           classTag +"DateAnnotation":"DATE",
           classTag +"CourseModifier":"COURSE",
           classTag +"DiseaseDisorderMention":"DISEASE",
           classTag +"TimeMention":"TIME:",
           classTag +"SeverityModifier":"SEVERITY",
           classTag +"MedicationDosageModifier":"DOSAGE"
        }

sep = "\t"
newline = "\n"

for f in listdir(outputDir): 
    filename = join(outputDir, f)
    if isfile(filename):
        ext = splitext(f)[1]
        if ext==".xmi":
            tree = ET.parse(filename)  
            root = tree.getroot()
            
            originalPost = root.findall(sofaTag)[0].attrib["sofaString"]
            
            with open(join(finalDir, f.replace(".xmi","")),"w+",encoding="utf-8") as fwriter:
                for el in root:
                    if el.tag in tagDic.keys():
                        try:
                            begin = int(el.attrib["begin"])
                            end = int(el.attrib["end"])
                            chunk = originalPost[begin:end]
                            #print(tagDic[el.tag] + sep + chunk + sep + str(begin) + sep + str(end) + newline)
                            fwriter.write(tagDic[el.tag] + sep + chunk + sep + str(begin) + sep + str(end) + newline)
                        except Exception as e:
                            print(e)