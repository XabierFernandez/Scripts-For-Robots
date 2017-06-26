# -*- coding: utf-8 -*-
__author__ = 'Xabier Fernandez Gutierrez'
__copyright__ = 'Copyright (C) 2017,Xabier Fernandez Gutierrez'
__credits__ = 'Xabier Fernandez Gutierrez'
__license__ = 'GNU GPL v3.0 '
__version__ = '2017.01'
__maintainer__ = 'Xabier Fernandez Gutierrez'
__email__ = 'xabier.fernandez@outlook.com'

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from modules import xml_file, ModFile, TargetFile
from modules import MyMessages


class Ui_MainWindow(object):
    def setupUi (self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(730, 467)
        MainWindow.setMaximumSize(MainWindow.size())
        MainWindow.setStyleSheet("background-color: rgb(129, 124, 129);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 391, 421))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 182, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 182, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 182, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 196))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 182, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 182, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 182, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 196))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 182, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 182, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 182, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame.setPalette(palette)
        self.frame.setStyleSheet("background-color: rgb(255, 182, 65);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pbRobt2Ast = QtWidgets.QPushButton(self.frame)
        # !!
        self.pbRobt2Ast.clicked.connect(self.runConvertRobt2Ast)
        # !!
        self.pbRobt2Ast.setGeometry(QtCore.QRect(10, 360, 211, 24))
        self.pbRobt2Ast.setStyleSheet("color: rgb(170, 0, 0);\n"
                                      "font: 75 11pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(193, 193, 193);")
        self.pbRobt2Ast.setObjectName("pbRobt2Ast")
        self.pbAst2Robt = QtWidgets.QPushButton(self.frame)
        # !!
        self.pbAst2Robt.clicked.connect(self.runConvertAst2Robt)
        # !!
        self.pbAst2Robt.setGeometry(QtCore.QRect(10, 320, 211, 26))
        self.pbAst2Robt.setStyleSheet("color: rgb(0, 85, 255);\n"
                                      "font: 75 11pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(193, 193, 193);")
        self.pbAst2Robt.setObjectName("pbAst2Robt")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 120, 201, 118))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(199, 32))
        self.label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "font: 75 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textPrefix = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textPrefix.setStyleSheet("border-color: rgb(170, 0, 0);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "")
        self.textPrefix.setObjectName("textPrefix")
        self.verticalLayout.addWidget(self.textPrefix)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.textSuffix = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textSuffix.setStyleSheet("border-color: rgb(170, 0, 0);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(255, 255, 255);")
        self.textSuffix.setObjectName("textSuffix")
        self.verticalLayout.addWidget(self.textSuffix)
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 361, 66))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.pbTarget = QtWidgets.QPushButton(self.formLayoutWidget)
        # !!
        self.pbTarget.clicked.connect(self.handlePbTarget)
        # !!
        self.pbTarget.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(193, 193, 193);")
        self.pbTarget.setObjectName("pbTarget")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pbTarget)
        self.pbMod = QtWidgets.QPushButton(self.formLayoutWidget)
        # !!
        self.pbMod.clicked.connect(self.handlePbMod)
        # !!
        self.pbMod.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(193, 193, 193);")
        self.pbMod.setObjectName("pbMod")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pbMod)
        self.lineMod = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineMod.setStyleSheet("border-color: rgb(170, 0, 0);\n"
                                   "font: 10pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "")
        self.lineMod.setReadOnly(True)
        self.lineMod.setObjectName("lineMod")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineMod)
        self.lineTarget = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineTarget.setStyleSheet("border-color: rgb(170, 0, 0);\n"
                                      "font: 10pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "")
        self.lineTarget.setReadOnly(True)
        self.lineTarget.setObjectName("lineTarget")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineTarget)
        self.pbRobt2Ast.raise_()
        self.pbAst2Robt.raise_()
        self.verticalLayoutWidget.raise_()
        self.formLayoutWidget.raise_()
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(430, 20, 281, 421))
        self.frame_2.setStyleSheet("background-color: rgb(205, 52, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 258, 231))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.listUserMove = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        # !!
        self.filledListUserMove()
        # !!
        self.listUserMove.setMouseTracking(False)
        self.listUserMove.setStyleSheet("background-color: rgb(205, 52, 255);")
        self.listUserMove.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listUserMove.setViewMode(QtWidgets.QListView.ListMode)
        self.listUserMove.setObjectName("listUserMove")
        self.verticalLayout_2.addWidget(self.listUserMove)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 260, 169, 129))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.lineNewInst = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineNewInst.setStyleSheet("border-color: rgb(170, 0, 0);\n"
                                       "font: 10pt \"MS Shell Dlg 2\";\n"
                                       "background-color: rgb(255, 255, 255);")
        self.lineNewInst.setObjectName("lineNewInst")
        self.verticalLayout_3.addWidget(self.lineNewInst)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_3.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_3.addWidget(self.radioButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pbAddMove = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        # !!
        self.pbAddMove.clicked.connect(self.handlePbAddMove)
        # !!
        self.pbAddMove.setStyleSheet("color: rgb(0, 85, 255);\n"
                                     "font: 75 11pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(193, 193, 193);")
        self.pbAddMove.setObjectName("pbAddMove")
        self.horizontalLayout_2.addWidget(self.pbAddMove)
        self.pbDelMove = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        # !!
        self.pbDelMove.clicked.connect(self.handlePbDelMove)
        # !!
        self.pbDelMove.setStyleSheet("color: rgb(170, 0, 0);\n"
                                     "font: 75 11pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(193, 193, 193);")
        self.pbDelMove.setObjectName("pbDelMove")
        self.horizontalLayout_2.addWidget(self.pbDelMove)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.label_4.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUser_motion_instructions = QtWidgets.QAction(MainWindow)
        self.actionUser_motion_instructions.setObjectName("actionUser_motion_instructions")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi (self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ABB RapidTools_v2017.01 [by X.Fernandez]"))
        self.pbRobt2Ast.setText(_translate("MainWindow", "Convert from Robtarget to *"))
        self.pbAst2Robt.setText(_translate("MainWindow", "Convert from * to Robtarget"))
        self.label.setText(_translate("MainWindow", "Prefix"))
        self.label_2.setText(_translate("MainWindow", "Suffix"))
        self.pbTarget.setText(_translate("MainWindow", "Select target file"))
        self.pbMod.setText(_translate("MainWindow", "Save modified file to:"))
        self.label_3.setText(_translate("MainWindow", "User Motion Instructions"))
        self.label_4.setText(_translate("MainWindow", "New motion instruction"))
        self.radioButton_2.setText(_translate("MainWindow", "Joint"))
        self.radioButton.setText(_translate("MainWindow", "Lineal"))
        self.pbAddMove.setText(_translate("MainWindow", "Add"))
        self.pbDelMove.setText(_translate("MainWindow", "Del"))
        self.actionUser_motion_instructions.setText(_translate("MainWindow", "User motion instructions"))

    def handlePbTarget (self):
        """
        Method that handles the click action of the 'Select target file' button.
        Opens a dialog in order to select the target file.
        """
        filename = QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Open file", "C://",
                                                         "ABB Files (*.mod)")
        if filename:
            self.lineTarget.setText(filename[0])

    def handlePbMod (self):
        """
        Method that handles the click action of the 'Save Modified file to' button.
        Opens a dialog in order to select the dir where the modified file will be store.
        """
        dir = QtWidgets.QFileDialog.getExistingDirectory(MainWindow, "Open a folder", "C:/",
                                                         QtWidgets.QFileDialog.ShowDirsOnly)
        if dir:
            self.lineMod.setText(dir)

    def handlePbAddMove (self):
        """
        Method that handles the click action of the 'Add' button.
        Add instruction given in textfield of the user interface.
        """
        strInst = self.lineNewInst.text()
        strType = ''

        if self.radioButton.isChecked():
            strType = 'Lineal'

        if self.radioButton_2.isChecked():
            strType = 'Joint'

        if strType and strInst and not xml_file.findDuplicates(strInst):
            xml_file.appendMovement(strInst, strType)
            item = QtWidgets.QListWidgetItem(self.listUserMove)
            ch = QtWidgets.QCheckBox()
            ch.setText(strInst)
            self.listUserMove.setItemWidget(item, ch)
            self.lineNewInst.setText('')
            self.listUserMove.repaint()

    def handlePbDelMove (self):
        """
        Method that handles the click action of the 'Del' button.
        Deletes instruction checked in the user interface list.
        """
        removeList = list()
        for index in range(self.listUserMove.count()):
            check_box = self.listUserMove.itemWidget(self.listUserMove.item(index))
            state = check_box.checkState()
            if state == 2:
                removeList.append(check_box.text())
        for strRemove in removeList:
            xml_file.removeMovement(strRemove)
        self.listUserMove.clear()
        self.filledListUserMove()
        self.listUserMove.repaint()

    def filledListUserMove (self):
        """
        Method that fills the list of keyword or instruction
        in the user interface.
        """
        for aItem in xml_file.getMovements():
            item = QtWidgets.QListWidgetItem(self.listUserMove)
            ch = QtWidgets.QCheckBox()
            ch.setText(aItem)
            self.listUserMove.setItemWidget(item, ch)

    def getCheckedItems (self):
        """
        Method that returns a list of the keyword or instruction
        checked in the user interface.
        """
        chekedList = list()

        for index in range(self.listUserMove.count()):
            check_box = self.listUserMove.itemWidget(self.listUserMove.item(index))
            state = check_box.checkState()
            if state == 2:
                chekedList.append(check_box.text())

        return chekedList

    def getKeywordList (self):
        """
        Method that returns a list of the keyword or instruction
        in the user interface.
        """
        listItems = list()

        for index in range(self.listUserMove.count()):
            check_box = self.listUserMove.itemWidget(self.listUserMove.item(index))
            listItems.append(check_box.text())
        return listItems

    def runConvertAst2Robt (self):
        """
        Method that runs * to robtarget conversion.
        Method call when pbAst2Robt button clicked
        """
        msgBox = MyMessages.MyMsg()
        try:
            keywordList = self.getKeywordList()
            excludedList = self.getCheckedItems()
            strTarget = self.lineTarget.text()
            strMod = self.lineMod.text()
            strPrefix = self.textPrefix.text()
            strSuffix = self.textSuffix.text()
            # ===================================
            if not strTarget:
                raise MyMessages.MyError(1)
            if not strMod:
                raise MyMessages.MyError(2)
            if not strPrefix:
                raise MyMessages.MyError(3)
            # ====================================================================================================
            targetFileObject = TargetFile.TargetFile(strTarget, keywordList, excludedList, strPrefix, strSuffix)
            targetFileObject.processAst2RobtTargetFile()
            # ====================================================================================================
            modFileObject = ModFile.ModFile(strMod, targetFileObject.getFileArray(),
                                            targetFileObject.getSubFileArray(), strPrefix, strSuffix)
            modFileObject.processAst2RobtModFile()
            # ====================================================================================================
            msgBox.msgBoxInfo("Asterisk to robtarget converted", "Process finish", "Convert asterisk2robtarget")
            # ====================================================================================================
        except FileNotFoundError:
            msgBox.msgBoxWarning("WARNING!, Target file or dir missing. ", "Error", "Convert asterisk2robtarget")
        except PermissionError:
            msgBox.msgBoxWarning("WARNING!, Target file or dir missing. ", "Error", "Convert asterisk2robtarget")
        except MyMessages.MyError as e:
            exceptValue = e.value
            if exceptValue == 1:
                msgBox.msgBoxWarning("WARNING!, Setting the target-file path required. ",
                                     "Error", "Convert asterisk2robtarget")
            elif exceptValue == 2:
                msgBox.msgBoxWarning("WARNING!, Setting the modified-file dir path required. ",
                                     "Error", "Convert asterisk2robtarget")
            elif exceptValue == 3:
                msgBox.msgBoxWarning("WARNING!, Setting the prefix-field required. ",
                                     "Error", "Convert asterisk2robtarget")

    def runConvertRobt2Ast (self):
        """
        Method that runs robtarget to * conversion.
        Method call when pbRobt2Ast button clicked
        """
        msgBox = MyMessages.MyMsg()
        try:
            keywordList = self.getKeywordList()
            excludedList = self.getCheckedItems()
            strTarget = self.lineTarget.text()
            strMod = self.lineMod.text()
            # ===================================
            if not strTarget:
                raise MyMessages.MyError(1)
            if not strMod:
                raise MyMessages.MyError(2)
            # ====================================================================================================
            targetFileObject = TargetFile.TargetFile(strTarget, keywordList, excludedList)
            targetFileObject.processRobt2AstTargetFile()
            # ====================================================================================================
            modFileObject = ModFile.ModFile(strMod, targetFileObject.getFileArray(),
                                            targetFileObject.getSubFileArray())
            modFileObject.processRobt2AstModFile()
            # ====================================================================================================
            msgBox.msgBoxInfo("Robtarget to asterisk converted", "Process finish", "Convert robtarget2asterisk")
            # ====================================================================================================
        except FileNotFoundError:
            msgBox.msgBoxWarning("WARNING!, Target file or dir missing. ", "Error", "Convert robtarget2asterisk")
        except PermissionError:
            msgBox.msgBoxWarning("WARNING!, Target file or dir missing. ", "Error", "Convert robtarget2asterisk")
        except MyMessages.MyError as e:
            exceptValue = e.value
            if exceptValue == 1:
                msgBox.msgBoxWarning("WARNING!, Setting the target-file path required. ",
                                     "Error", "Convert robtarget2asterisk")
            elif exceptValue == 2:
                msgBox.msgBoxWarning("WARNING!, Setting the modified-file dir path required. ",
                                     "Error", "Convert robtarget2asterisk")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
