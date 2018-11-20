# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SemanticEditor.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SemanticEditor(object):
    def setupUi(self, SemanticEditor):
        SemanticEditor.setObjectName("SemanticEditor")
        SemanticEditor.setEnabled(True)
        SemanticEditor.resize(1175, 624)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SemanticEditor.sizePolicy().hasHeightForWidth())
        SemanticEditor.setSizePolicy(sizePolicy)
        SemanticEditor.setStyleSheet("QListView {\n"
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
        self.gridLayout = QtWidgets.QGridLayout(SemanticEditor)
        self.gridLayout.setObjectName("gridLayout")
        self.gBConnections = QtWidgets.QGroupBox(SemanticEditor)
        self.gBConnections.setObjectName("gBConnections")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gBConnections)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listViewObjects = QtWidgets.QListView(self.gBConnections)
        self.listViewObjects.setObjectName("listViewObjects")
        self.verticalLayout_3.addWidget(self.listViewObjects)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pbAddObject = QtWidgets.QPushButton(self.gBConnections)
        self.pbAddObject.setObjectName("pbAddObject")
        self.horizontalLayout_4.addWidget(self.pbAddObject)
        self.pbRemoveObject = QtWidgets.QPushButton(self.gBConnections)
        self.pbRemoveObject.setObjectName("pbRemoveObject")
        self.horizontalLayout_4.addWidget(self.pbRemoveObject)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableViewInput = QtWidgets.QTableView(self.gBConnections)
        self.tableViewInput.setObjectName("tableViewInput")
        self.verticalLayout.addWidget(self.tableViewInput)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbAddInput = QtWidgets.QPushButton(self.gBConnections)
        self.pbAddInput.setObjectName("pbAddInput")
        self.horizontalLayout.addWidget(self.pbAddInput)
        self.pbRemoveInput = QtWidgets.QPushButton(self.gBConnections)
        self.pbRemoveInput.setObjectName("pbRemoveInput")
        self.horizontalLayout.addWidget(self.pbRemoveInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableViewOutput = QtWidgets.QTableView(self.gBConnections)
        self.tableViewOutput.setObjectName("tableViewOutput")
        self.verticalLayout_2.addWidget(self.tableViewOutput)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pbAddOutput = QtWidgets.QPushButton(self.gBConnections)
        self.pbAddOutput.setObjectName("pbAddOutput")
        self.horizontalLayout_3.addWidget(self.pbAddOutput)
        self.pbRemoveOutput = QtWidgets.QPushButton(self.gBConnections)
        self.pbRemoveOutput.setObjectName("pbRemoveOutput")
        self.horizontalLayout_3.addWidget(self.pbRemoveOutput)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addWidget(self.gBConnections, 0, 0, 1, 2)
        self.pbShowPlot = QtWidgets.QPushButton(SemanticEditor)
        self.pbShowPlot.setObjectName("pbShowPlot")
        self.gridLayout.addWidget(self.pbShowPlot, 1, 1, 1, 1)

        self.retranslateUi(SemanticEditor)
        QtCore.QMetaObject.connectSlotsByName(SemanticEditor)

    def retranslateUi(self, SemanticEditor):
        _translate = QtCore.QCoreApplication.translate
        SemanticEditor.setWindowTitle(_translate("SemanticEditor", "RuleEditor"))
        self.gBConnections.setTitle(_translate("SemanticEditor", "Semantic objects Editor"))
        self.pbAddObject.setText(_translate("SemanticEditor", "Add Object"))
        self.pbRemoveObject.setText(_translate("SemanticEditor", "Remove Object"))
        self.pbAddInput.setText(_translate("SemanticEditor", "Add Input"))
        self.pbRemoveInput.setText(_translate("SemanticEditor", "Remove Input"))
        self.pbAddOutput.setText(_translate("SemanticEditor", "Add Output"))
        self.pbRemoveOutput.setText(_translate("SemanticEditor", "Remove Output"))
        self.pbShowPlot.setText(_translate("SemanticEditor", "Show Plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SemanticEditor = QtWidgets.QDialog()
    ui = Ui_SemanticEditor()
    ui.setupUi(SemanticEditor)
    SemanticEditor.show()
    sys.exit(app.exec_())

