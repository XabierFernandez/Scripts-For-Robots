#!/usr/bin/env python
"""
Docstring
"""

#===============================================================================
class ModFile(object):
    def __init__(self, file_path, aFileArray, aSubFileArray, aPrefix='', aSuffix=''):
        """
        Constructor and initializer of the modified file.
        The name of the file is ModFile.mod
        :param file_path:
        :param aFileArray:
        :param aSubFileArray:
        :param aPrefix: default value =''
        :param aSuffix: default value =''
        """
        self.file_object = None
        self.file_path = file_path
        self.fileArrayList = list( aFileArray )
        self.subFileArrayList = list( aSubFileArray )
        self.prefix = aPrefix
        self.suffix = aSuffix

    def openModFile(self):
        """Method that opens the modified file, with writting permission"""
        self.file_object = open(self.file_path + '/' + 'ModFile.mod', 'w+')

    def closeModFile(self):
        """Method that closes the modified file."""
        self.file_object.close()

    def writeToModAst2RobtFile(self):
        """
        Method that writes to the modified file.
        Method call during * to robtarget conversion.
        """
        for line in self.fileArrayList:
            if('MODULE' in line.upper() and 'ENDMODULE' not in line.upper()):
                self.file_object.write(line)
                #==============================================================================
                for idx,line1 in enumerate(self.subFileArrayList):
                    self.file_object.write('LOCAL CONST robtarget ' + self.prefix + str(idx + 1)
                                           + self.suffix + ':=' + line1 + ';' + '\n' )
            else:
                self.file_object.write(line)
        self.closeModFile()

    def writeToModRobt2AstFile (self):
        """
        Method that writes to the modified file.
        Method call during robtarget to * conversion.
        """
        for line in self.subFileArrayList:
            self.file_object.write(line)
        self.closeModFile()


    def processAst2RobtModFile(self):
        """
        Method that processes * to robtarget conversion.
        """
        self.openModFile()
        self.writeToModAst2RobtFile()

    def processRobt2AstModFile(self):
        """
        Method that processes robtarget to ^ conversion.
        """
        self.openModFile()
        self.writeToModRobt2AstFile()
