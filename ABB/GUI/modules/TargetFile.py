#!/usr/bin/env python
"""
Docstring
"""

#===============================================================================
import re


class TargetFile(object):
    def __init__(self,aFile_path, aKeyWordsList, aExcludedInst, aPrefix, aSuffix):
        self.file_object = None
        self.file_path = aFile_path
        self.fileArray = list()
        self.subFileArray = list()
        self.keyWordsFile = aKeyWordsList
        self.excludedInstructions = aExcludedInst
        self.prefix = aPrefix
        self.suffix = aSuffix

    def openTargetFile(self):
        self.file_object = open(self.file_path, 'r')

    def closeTargetFile(self):
        self.file_object.close()

    def checkLinesAst2Robt(self):
        pointnum = 1
        s = ''
        for line in range (len(self.fileArray)):
            if self.checkRulesAst2Robt( self.fileArray[line] ):
                s1 = self.fileArray[line]
                s2 = self.fileArray[line]
                start = s2.find('[[')
                end = s2.find(']]')
                s2 = s2[start:end + 2]
                self.subFileArray.append(s2)
                self.fileArray[line] = s1.replace(s2, self.prefix + str(pointnum) + self.suffix)
                pointnum = pointnum + 1

    def checkLinesRobt2Ast(self):
        dict = self.getRobtargetPoints()
        listPoints = dict.keys()
        matchedPoints = list()

        for line in range(len(self.fileArray)):
            if self.checkRulesRobt2Ast( self.fileArray[line],listPoints ):
                for point in listPoints:
                    if self.searchMatchWord(point,self.fileArray[line]):
                        self.fileArray[line] = self.fileArray[line].replace(point,dict.get(point))
                        matchedPoints.append(point)
        for line in range(len(self.fileArray)):
            if self.checkCharInStr('robtarget',self.fileArray[line]) and \
                self.checkCharInStrMatched(self.fileArray[line], matchedPoints):
                pass
            else:
                self.subFileArray.append(self.fileArray[line])


    def checkStrInLists(self, aStr, aList):
        return (any ( x in aStr for x in aList ))

    def checkCharInStr(self, aChar, aStr):
        return (aChar in aStr)

    def checkCharInStrMatched(self, aStr1, aList):
        result = False
        for str in aList:
            if self.searchMatchWord(str, aStr1):
                result = True
                break
        return result


    def searchMatchWord (self,string1, string2):
        if re.search(r"\b" + re.escape(string1) + r"\b", string2):
            return True
        return False

    def checkRulesRobt2Ast (self, aStr, Points):
        return self.checkStrInLists(aStr, self.keyWordsFile) and not \
            self.checkStrInLists(aStr, self.excludedInstructions) \
               and not self.checkCharInStr('robtarget', aStr.lower()) and self.checkStrInLists(aStr, Points)

    def checkRulesAst2Robt(self, aStr):
        return self.checkStrInLists(aStr, self.keyWordsFile) and not \
            self.checkStrInLists(aStr, self.excludedInstructions) \
            and not self.checkCharInStr('!', aStr) and self.checkCharInStr('[[', aStr)

    def readTargetFileLines(self):
        for line in self.file_object.readlines ():
            self.fileArray.append ( line )
            self.closeTargetFile()

    def getRobtargetPoints(self):
        dictPointCoord = dict()

        for line in range ( len ( self.fileArray ) ):
            if 'robtarget' in self.fileArray[line].lower():
                #################################
                s1 = self.fileArray[line]
                startRobt1 = s1.find('robtarget')
                endRobt1 = s1.find(':=')
                s1 = s1[startRobt1 + 9:endRobt1]
                s1 = s1.strip()
                #################################
                s2 = self.fileArray[line]
                startRobt2 = s2.find('[[')
                endRobt2 = s2.find(']]')
                s2 = s2[startRobt2:endRobt2 + 2]
                #################################
                dictPointCoord.update({s1: s2})
        return dictPointCoord

    def getFileArray(self):
        return self.fileArray

    def getSubFileArray(self):
        return self.subFileArray

    def processAst2RobtTargetFile(self):
        self.openTargetFile()
        self.readTargetFileLines()
        self.checkLinesAst2Robt()


    def processRobt2AstTargetFile(self):
        self.openTargetFile()
        self.readTargetFileLines()
        self.checkLinesRobt2Ast()


