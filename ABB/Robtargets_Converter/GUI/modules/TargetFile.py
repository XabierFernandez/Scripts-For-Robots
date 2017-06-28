#!/usr/bin/env python
"""
Docstring
"""

#===============================================================================
import re


class TargetFile(object):
    def __init__(self,aFile_path, aKeyWordsList, aExcludedInst, aPrefix='', aSuffix=''):
        """
        Constructor and initializer of the target file. File with extension .MOD
        This is the file we want to modify.
        :param aFile_path:
        :param aKeyWordsList:
        :param aExcludedInst:
        :param aPrefix: default value =''
        :param aSuffix: default value =''
        """
        self.file_object = None
        self.file_path = aFile_path
        self.fileArray = list()
        self.subFileArray = list()
        self.keyWordsFile = aKeyWordsList
        self.excludedInstructions = aExcludedInst
        self.prefix = aPrefix
        self.suffix = aSuffix

    def openTargetFile(self):
        """Method that opens the target file, with read-only permission"""
        self.file_object = open(self.file_path, 'r')

    def closeTargetFile(self):
        """Method that closes the target file."""
        self.file_object.close()

    def checkLinesAst2Robt(self):
        """
        Method that searches and checks if any line of the target file meets
        with the rules(patterns) given. This is use during * to robtarget conversion.
        If a string meets the rules, it is store in a list declared as SubFileArray.
        """
        pointnum = 1
        for idx,line in enumerate(self.fileArray):
            if self.checkRulesAst2Robt(line):
                s1 = line
                s2 = line
                start = s2.find('[[')
                end = s2.find(']]')
                s2 = s2[start:end + 2]
                self.subFileArray.append(s2)
                self.fileArray[idx] = s1.replace(s2, self.prefix + str(pointnum) + self.suffix)
                pointnum = pointnum + 1

    def checkLinesRobt2Ast(self):
        """Method that searches and checks if any line of the target file meets
        with the rules(patterns) given. This is use when robtarget to * conversion
        """
        dictionary = self.getRobtargetPoints()
        listPoints = dictionary.keys()
        matchedPoints = list()

        for idx,line in enumerate(self.fileArray):
            if self.checkRulesRobt2Ast(line,listPoints):
                for point in listPoints:
                    if self.searchMatchWord(point,line):
                        self.fileArray[idx] = line.replace(point,dictionary.get(point))
                        matchedPoints.append(point)
        for line in self.fileArray:
            if self.checkStrInStr('robtarget', line) and self.checkStrInStrMatched(line, matchedPoints):
                pass
            else:
                self.subFileArray.append(line)

    @classmethod
    def checkStrInLists(cls, aStr, aList):
        """
        Method that checks if an element of a List is found inside a String.
        Returns True/False
        """
        return (any ( x in aStr for x in aList ))

    @classmethod
    def checkStrInStr(cls, aChar, aStr):
        """
        Method that checks if a character or string is found inside another String.
        Returns True/False
        """
        return (aChar in aStr)

    def checkStrInStrMatched(self, aStr1, aList):
        """
        Method that checks if a character or string is found inside another String.
        The search considers the whole word.
        Returns True/False
        """
        result = False
        for aStr in aList:
            if self.searchMatchWord(aStr, aStr1):
                result = True
                break
        return result

    @classmethod
    def searchMatchWord (cls,string1, string2):
        """
        Method that search for whole word match
        Returns True/False
        """
        if re.search(r"\b" + re.escape(string1) + r"\b", string2):
            return True
        return False

    def checkRulesRobt2Ast (self, aStr, aListPoints):
        """
        Method that check a string against the rules for robtarget to * conversion.
        -rule1: keywords must be in the aStr.
        -rule2: excluded keywords(instructions) must not be in the aStr.
        -rule3: list of points declared as robtarget must be in the aStr.
        Returns True/False
        """
        return self.checkStrInLists(aStr, self.keyWordsFile) and not \
            self.checkStrInLists(aStr, self.excludedInstructions) \
               and not self.checkStrInStr('robtarget', aStr.lower()) and self.checkStrInLists(aStr, aListPoints)

    def checkRulesAst2Robt(self, aStr):
        """
        Method that check a string against the rules for * to robtarget conversion.
        -rule1: keywords must be in the aStr.
        -rule2: excluded keywords(instructions) must not be in the aStr.
        -rule3: String must contain '[[' characters and not '!' character(comment symbol).
        Returns True/False
        """
        return self.checkStrInLists(aStr, self.keyWordsFile) and not \
            self.checkStrInLists(aStr, self.excludedInstructions) \
            and not self.checkStrInStr('!', aStr) and self.checkStrInStr('[[', aStr)

    def readTargetFileLines(self):
        """
        Method that reads a file line by line and stores this lines in a list.
        """
        for line in self.file_object.readlines ():
            self.fileArray.append(line)
            self.closeTargetFile()

    def getRobtargetPoints(self):
        """
        Method that reads a list of strings and searches if robtarget declaration keyword is in it.
        """
        dictPointCoord = dict()

        for line in self.fileArray:
            if 'robtarget' in line.lower():
                #################################
                s1 = line
                startRobt1 = s1.find('robtarget')
                endRobt1 = s1.find(':=')
                s1 = s1[startRobt1 + 9:endRobt1]
                s1 = s1.strip()
                #################################
                s2 = line
                startRobt2 = s2.find('[[')
                endRobt2 = s2.find(']]')
                s2 = s2[startRobt2:endRobt2 + 2]
                #################################
                dictPointCoord.update({s1: s2})
        return dictPointCoord

    def getFileArray(self):
        """
        Method that returns a list of strings.
        In this case, the list represents the file's line.
        Returns list
        """
        return self.fileArray

    def getSubFileArray(self):
        """
        Method that returns a list of strings.
        In this case, SubFileArray list.
        Returns list
        """
        return self.subFileArray

    def processAst2RobtTargetFile(self):
        """
        Method that processes * to robtarget conversion.
        """
        self.openTargetFile()
        self.readTargetFileLines()
        self.checkLinesAst2Robt()


    def processRobt2AstTargetFile(self):
        """
        Method that processes robtarget to ^ conversion.
        """
        self.openTargetFile()
        self.readTargetFileLines()
        self.checkLinesRobt2Ast()


