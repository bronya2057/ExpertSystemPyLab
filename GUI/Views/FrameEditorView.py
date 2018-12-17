# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\FrameEditor.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FrameEditor(object):
    def setupUi(self, FrameEditor):
        FrameEditor.setObjectName("FrameEditor")
        FrameEditor.setEnabled(True)
        FrameEditor.resize(1006, 623)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FrameEditor.sizePolicy().hasHeightForWidth())
        FrameEditor.setSizePolicy(sizePolicy)
        FrameEditor.setStyleSheet("QListView {\n"
"    alternate-background-color: yellow;\n"
"    background-color: #697378;\n"
"    margin-right:10px\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"     background-color: #96A4AD;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"     background-color: #96A4AD;\n"
"}\n"
"\n"
" QHeaderView::section {\n"
"     background-color: rgba(0,0,0,0%);\n"
"     color: white;\n"
"    padding:5px;\n"
"text-transform:uppercase;\n"
" }\n"
"\n"
"QTableCornerButton::section {background-color: rgba(0,0,0,0); }\n"
"\n"
"*::disabled\n"
"{\n"
"        background-color:#b4bdc6;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #475156, stop: 1 #74828B);\n"
"        color:black;\n"
"}\n"
"\n"
"QMainWindow, QWidget{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #697378, stop: 1 #96A4AD);\n"
"}\n"
"\n"
"*{\n"
"    font-size:14px;\n"
"    font-family:\"Bahnschrift\";\n"
"    /*padding:5px;*/\n"
"    color:white;\n"
"}\n"
"\n"
"*:diabled{\n"
"        background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #475156, stop: 1 #74828B);\n"
"}\n"
"\n"
"QLabel,QRadioButton{\n"
"    background-color: rgba(0,0,0,0%)\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #96A4AD, stop: 1 #697378 );\n"
"\n"
"border: 2px solid #96A4AD;\n"
"border-radius:6px;\n"
"\n"
"    min-width: 80px;\n"
"    min-height:30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #74828B, stop: 1 #697378 );\n"
"    /*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);*/\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: #535a66;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #475156, stop: 1 #74828B);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFOECE, stop: 1 #FFFFFF);\n"
"\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"     background-color: #96A4AD;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"     background-color: #96A4AD;\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(FrameEditor)
        self.gridLayout.setObjectName("gridLayout")
        self.gBConnections = QtWidgets.QGroupBox(FrameEditor)
        self.gBConnections.setObjectName("gBConnections")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gBConnections)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.treeViewFrames = QtWidgets.QTreeView(self.gBConnections)
        self.treeViewFrames.setObjectName("treeViewFrames")
        self.verticalLayout_3.addWidget(self.treeViewFrames)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pbAddNode = QtWidgets.QPushButton(self.gBConnections)
        self.pbAddNode.setObjectName("pbAddNode")
        self.horizontalLayout_4.addWidget(self.pbAddNode)
        self.pbAddChild = QtWidgets.QPushButton(self.gBConnections)
        self.pbAddChild.setObjectName("pbAddChild")
        self.horizontalLayout_4.addWidget(self.pbAddChild)
        self.pbRemoveObject = QtWidgets.QPushButton(self.gBConnections)
        self.pbRemoveObject.setObjectName("pbRemoveObject")
        self.horizontalLayout_4.addWidget(self.pbRemoveObject)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout.addWidget(self.gBConnections, 0, 1, 1, 5)
        self.pbGraph = QtWidgets.QPushButton(FrameEditor)
        self.pbGraph.setObjectName("pbGraph")
        self.gridLayout.addWidget(self.pbGraph, 1, 5, 1, 1)
        self.pbSave = QtWidgets.QPushButton(FrameEditor)
        self.pbSave.setObjectName("pbSave")
        self.gridLayout.addWidget(self.pbSave, 1, 4, 1, 1)
        self.pbLoad = QtWidgets.QPushButton(FrameEditor)
        self.pbLoad.setObjectName("pbLoad")
        self.gridLayout.addWidget(self.pbLoad, 1, 3, 1, 1)
        self.pbNewModel = QtWidgets.QPushButton(FrameEditor)
        self.pbNewModel.setObjectName("pbNewModel")
        self.gridLayout.addWidget(self.pbNewModel, 1, 1, 1, 2)

        self.retranslateUi(FrameEditor)
        QtCore.QMetaObject.connectSlotsByName(FrameEditor)

    def retranslateUi(self, FrameEditor):
        _translate = QtCore.QCoreApplication.translate
        FrameEditor.setWindowTitle(_translate("FrameEditor", "FrameEditor"))
        self.gBConnections.setTitle(_translate("FrameEditor", "Frame objects Editor"))
        self.pbAddNode.setText(_translate("FrameEditor", "Add Node"))
        self.pbAddChild.setText(_translate("FrameEditor", "Add Child"))
        self.pbRemoveObject.setText(_translate("FrameEditor", "Remove Object"))
        self.pbGraph.setText(_translate("FrameEditor", "Draw Frame Graph"))
        self.pbSave.setText(_translate("FrameEditor", "Save Frame Model"))
        self.pbLoad.setText(_translate("FrameEditor", "Load Frame Model"))
        self.pbNewModel.setText(_translate("FrameEditor", "New Frame Model"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrameEditor = QtWidgets.QDialog()
    ui = Ui_FrameEditor()
    ui.setupUi(FrameEditor)
    FrameEditor.show()
    sys.exit(app.exec_())

