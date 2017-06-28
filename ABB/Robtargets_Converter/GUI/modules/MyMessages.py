

from PyQt5.QtWidgets import QMessageBox

class MyError(Exception):
    def __init__(self, value=0):
        self.value = value

    def __str__(self):
        return repr(self.value)

class MyMsg():
    def __init__(self):
        self.msgBox = QMessageBox()

    def msgBoxInfo(self,aText,aInfoText, aTitle):
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText(aText)
        self.msgBox.setInformativeText(aInfoText)
        self.msgBox.setWindowTitle(aTitle)
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()

    def msgBoxWarning(self,aText,aInfoText, aTitle):
        self.msgBox.setIcon(QMessageBox.Warning)
        self.msgBox.setText(aText)
        self.msgBox.setInformativeText(aInfoText)
        self.msgBox.setWindowTitle(aTitle)
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()
