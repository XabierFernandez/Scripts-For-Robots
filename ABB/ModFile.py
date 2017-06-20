#!/usr/bin/env python
"""
Docstring
"""

#===============================================================================
class ModFile(object):
    def __init__(self):
        self.file_object = None
        self.fileArray = list()
        self.subFileArray = list()
        self.prefix = ''
        self.suffix = ''

    def openModFile(self, file_path):
        self.file_object = open(file_path, 'w+')

    def closeModFile(self):
        self.file_object.close()

    def writeToModFile(self):
        for line in range ( len ( self.fileArray ) ):
            if('MODULE' in self.fileArray[line].upper() and 'ENDMODULE' not in self.fileArray[line].upper()):
                self.file_object.write(self.fileArray[line])
                for line1 in range(len(self.subFileArray)):
                    self.file_object.write('LOCAL CONST robtarget ' + self.prefix + str(line1 + 1)
                                           + self.suffix + ':=' + self.subFileArray[line1] + '\n')
            else:
                self.file_object.write(self.fileArray[line])
        self.close_TargetFile()

    def setSubArray(self,aList):
        self.subFileArray = aList

    def setFileArray(self,aList):
        self.fileArray = aList

    def setPrefix(self,aStr):
        self.prefix = aStr

    def setSuffix(self,aStr):
        self.suffix = aStr
