'''
Created on Sep 22, 2012

Handles all file processing for text files

@author: creed
'''

import os


class TextFileProcessor:
    def __init__(self):
        self.rootDirectory = 'files/'

    def openFile(self, fileName):
        fileResource = open(self.rootDirectory + fileName, 'r')
        return fileResource

    def processFileContents(self, fileResource, delimeter):
        dataArray = []

        for line in fileResource:
            line = line.rstrip(os.linesep)

            dataArray.append(line.split(delimeter))

        return dataArray
