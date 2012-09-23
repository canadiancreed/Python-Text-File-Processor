'''
Created on Sep 22, 2012

This file is the entry point for this application

@author: creed
'''
from os import listdir
from textFileProcessor import TextFileProcessor
from data import Data

t = TextFileProcessor()

try:
    d = Data()
except:
    quit()

dirFileList = listdir('files')
currentFileResource = ''
currentFileDataArray = []

for fileName in dirFileList:
    currentFileResource = t.openFile(fileName)

    if currentFileResource != 'false':
        currentFileDataArray = t.processFileContents(currentFileResource, ',')
    else:
        continue

    try:
        d.insertData('playerStats', currentFileDataArray)
    except:
        continue
