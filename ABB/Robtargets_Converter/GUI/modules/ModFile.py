#!/usr/bin/env python
"""
Docstring
"""

#===============================================================================
class ModFile(object):
    def __init__(self, file_path, aFileArray, aSubFileArray, aPrefix='', aSuffix=''):
        self.file_object = None
        self.file_path = file_path
        self.fileArrayList = list( aFileArray )
        self.subFileArrayList = list( aSubFileArray )
        self.prefix = aPrefix
        self.suffix = aSuffix

    def openModFile(self):
        self.file_object = open(self.file_path + '/' + 'ModFile.mod', 'w+')

    def closeModFile(self):
        self.file_object.close()

    def writeToModAst2RobtFile(self):
        for line in range ( len( self.fileArrayList ) ):
            if('MODULE' in self.fileArrayList[line].upper() and 'ENDMODULE' not in self.fileArrayList[line].upper()):
                self.file_object.write( self.fileArrayList[line] )
                for line1 in range( len( self.subFileArrayList ) ):
                    self.file_object.write('LOCAL CONST robtarget ' + self.prefix + str(line1 + 1)
                                           + self.suffix + ':=' + self.subFileArrayList[line1] + ';' + '\n' )
            else:
                self.file_object.write( self.fileArrayList[line] )
        self.closeModFile()

    def writeToModRobt2AstFile (self):
        for line in range ( len( self.subFileArrayList ) ):
            self.file_object.write( self.subFileArrayList[line] )
        self.closeModFile()


    def processAst2RobtModFile(self):
        self.openModFile()
        self.writeToModAst2RobtFile()

    def processRobt2AstModFile(self):
        self.openModFile()
        self.writeToModRobt2AstFile()
