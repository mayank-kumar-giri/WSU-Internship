#!/usr/bin/env python
# coding: utf-8

# Importing libraries
import numpy as np
import pandas as pd
import os

# Getting location of our File Stack
cwd = os.getcwd()
cwd += "\\Input_Data\\FS_L\\FS_L\\file_stack"
print("\nLocation of File Stack:\n",cwd)


# Generating a list of files in our File Stack
files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd,f))]
files.remove(".DS_Store")
print("\nList of files in the File Stack:\n",files)


# Identifying which files from CSV actually exist (final)
fp = open("Input_Data/FS_L/FS_L/list.csv","r+")
csvdata = fp.read().splitlines(True)
final = []
count = 1
for i in csvdata:
    for j in i.split(","):
        if j[-1]!="\n":
            curr = j + ".txt"
        else:
            curr = j[:(len(j)-1)] + ".txt"
        count += 1
        if curr in files:
            final.append(curr)
fp.close()
del fp
print("\nFiles to be modified:\n",final)


# Finally, for each file in 'final', Splitting into words, Capitalizing and Appending the word count
for i in final:
    path = cwd+"\\"+i
    fpp = open(path,"r+")
    data = fpp.read().splitlines(True)
    count = 0
    print("\nOriginal Data:\n",data)
    for line_num in range(len(data)):
        words = data[line_num].split()
        for word_num in range(len(words)):
            words[word_num] = words[word_num].capitalize()
            count += 1
        line = ""
        for j in range(len(words)):
            if j==(len(words)-1):
                line += words[j]
            else:
                line += (words[j]+" ")
        data[line_num] = line
    data.append("\n"+str(count))
    print("\nModified Data:\n",data)
    fpp.seek(0,0)
    fpp.writelines(data)
    fpp.close()
    del fpp