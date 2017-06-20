#!/usr/bin/env python
"""
Docstring
"""

#===============================================================================
class TargetFile(object):
    def __init__(self, file_object):
        self.file_object = file_object
        self.fileArray = list()
        self.subFileArray = list ()
        self.keyWordsFile = list()
        self.excludedInstructions = list ()
        self.prefix = ''
        self.suffix = ''

    def open_TargetFile(self, file_path):
        self.file_object = open(file_path, 'r')

    def close_TargetFile(self):
        self.file_object.close()

    def checkLines(self):
        pointnum = 1
        s = ''
        for line in range (len(self.fileArray)):
            if self.checkRules (self.fileArray[line]):
                s1 = self.fileArray[line]
                s2 = self.fileArray[line]
                start = s2.find('[[')
                end = s2.find(']]')
                s2 = s2[start:end + 2]
                self.subFileArray.append(s2)
                self.fileArray[line] = s1.replace(s2, self.prefix + str(pointnum) + self.suffix)
                pointnum = pointnum + 1

    def checkStrInLists(self, aStr, aList):
        return (any ( x in aStr for x in aList ))

    def checkCharInStr(self, aChar, aStr):
        return (aChar in aStr)

    def checkRules(self, aStr):
        return self.checkStrInLists(aStr, self.keyWordsFile) and not \
            self.checkStrInLists(aStr, self.excludedInstructions) \
            and not self.checkCharInStr('!', aStr) and self.checkCharInStr('[[', aStr)

    def readTargetFileLines(self):
        for line in self.file_object.readlines ():
            self.fileArray.append ( line )
            self.close_TargetFile()

    def setPrefix(self, aStr):
        self.prefix = aStr

    def setSuffix(self, aStr):
        self.suffix = aStr
