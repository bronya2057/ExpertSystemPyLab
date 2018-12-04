# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\RuleEditor.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RuleEditor(object):
    def setupUi(self, RuleEditor):
        RuleEditor.setObjectName("RuleEditor")
        RuleEditor.setEnabled(True)
        RuleEditor.resize(1175, 724)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RuleEditor.sizePolicy().hasHeightForWidth())
        RuleEditor.setSizePolicy(sizePolicy)
        RuleEditor.setStyleSheet("QMainWindow, QWidget{\n"
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
"QRadioButton::indicator\n"
"{\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked\n"
"{\n"
"   image: url(\"images/Radio_Off.PNG\");\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(\"images/Radio_Hover.PNG\");\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"    image: url(\"images/Radio_Off.PNG\");\n"
"}\n"
"\n"
"QRadioButton::indicator::checked \n"
"{\n"
"    image: url(\"images/Radio_On.PNG\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover \n"
"{\n"
"    image: url(\"images/Radio_On.PNG\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed \n"
"{\n"
"    image: url(\"images/Radio_Off.PNG\");\n"
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
        self.gridLayout = QtWidgets.QGridLayout(RuleEditor)
        self.gridLayout.setObjectName("gridLayout")
        self.gBAllInfo = QtWidgets.QGroupBox(RuleEditor)
        self.gBAllInfo.setEnabled(False)
        self.gBAllInfo.setMinimumSize(QtCore.QSize(0, 50))
        self.gBAllInfo.setStyleSheet("QGroupBox{\n"
"        background-color: #697378;\n"
"            border: 2px solid #96A4AD;\n"
"    border-radius: 5px;\n"
"    margin-top: 3ex;\n"
"text-transform: uppercase;\n"
"}")
        self.gBAllInfo.setObjectName("gBAllInfo")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gBAllInfo)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lblVariables = QtWidgets.QLabel(self.gBAllInfo)
        self.lblVariables.setObjectName("lblVariables")
        self.verticalLayout_5.addWidget(self.lblVariables)
        self.listViewVariables = QtWidgets.QListView(self.gBAllInfo)
        self.listViewVariables.setObjectName("listViewVariables")
        self.verticalLayout_5.addWidget(self.listViewVariables)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pbAddVariable = QtWidgets.QPushButton(self.gBAllInfo)
        self.pbAddVariable.setObjectName("pbAddVariable")
        self.horizontalLayout_7.addWidget(self.pbAddVariable)
        self.pbRemoveVariable = QtWidgets.QPushButton(self.gBAllInfo)
        self.pbRemoveVariable.setObjectName("pbRemoveVariable")
        self.horizontalLayout_7.addWidget(self.pbRemoveVariable)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblQuestions = QtWidgets.QLabel(self.gBAllInfo)
        self.lblQuestions.setObjectName("lblQuestions")
        self.verticalLayout_3.addWidget(self.lblQuestions)
        self.listViewQuestions = QtWidgets.QListView(self.gBAllInfo)
        self.listViewQuestions.setStyleSheet("")
        self.listViewQuestions.setObjectName("listViewQuestions")
        self.verticalLayout_3.addWidget(self.listViewQuestions)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pbAddQuestion = QtWidgets.QPushButton(self.gBAllInfo)
        self.pbAddQuestion.setObjectName("pbAddQuestion")
        self.horizontalLayout_6.addWidget(self.pbAddQuestion)
        self.pbRemoveQuestion = QtWidgets.QPushButton(self.gBAllInfo)
        self.pbRemoveQuestion.setObjectName("pbRemoveQuestion")
        self.horizontalLayout_6.addWidget(self.pbRemoveQuestion)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblOutput = QtWidgets.QLabel(self.gBAllInfo)
        self.lblOutput.setObjectName("lblOutput")
        self.verticalLayout.addWidget(self.lblOutput)
        self.textEditOutput = QtWidgets.QTextEdit(self.gBAllInfo)
        self.textEditOutput.setObjectName("textEditOutput")
        self.verticalLayout.addWidget(self.textEditOutput)
        self.pbUpdateOutput = QtWidgets.QPushButton(self.gBAllInfo)
        self.pbUpdateOutput.setObjectName("pbUpdateOutput")
        self.verticalLayout.addWidget(self.pbUpdateOutput)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.gbRules = QtWidgets.QGroupBox(self.gBAllInfo)
        self.gbRules.setMinimumSize(QtCore.QSize(0, 50))
        self.gbRules.setObjectName("gbRules")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gbRules)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listViewRules = QtWidgets.QListView(self.gbRules)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewRules.sizePolicy().hasHeightForWidth())
        self.listViewRules.setSizePolicy(sizePolicy)
        self.listViewRules.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listViewRules.setObjectName("listViewRules")
        self.verticalLayout_4.addWidget(self.listViewRules)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pbAddRule = QtWidgets.QPushButton(self.gbRules)
        self.pbAddRule.setObjectName("pbAddRule")
        self.horizontalLayout_5.addWidget(self.pbAddRule)
        self.pbUpdateRule = QtWidgets.QPushButton(self.gbRules)
        self.pbUpdateRule.setObjectName("pbUpdateRule")
        self.horizontalLayout_5.addWidget(self.pbUpdateRule)
        self.pbRemoveRule = QtWidgets.QPushButton(self.gbRules)
        self.pbRemoveRule.setObjectName("pbRemoveRule")
        self.horizontalLayout_5.addWidget(self.pbRemoveRule)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.tableViewRules = QtWidgets.QTableView(self.gbRules)
        self.tableViewRules.setEnabled(False)
        self.tableViewRules.setStyleSheet(" QHeaderView::section {\n"
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
"}")
        self.tableViewRules.setObjectName("tableViewRules")
        self.horizontalLayout_2.addWidget(self.tableViewRules)
        self.gridLayout_2.addWidget(self.gbRules, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.gBAllInfo, 1, 0, 1, 3)
        self.lblThemeName = QtWidgets.QLabel(RuleEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblThemeName.sizePolicy().hasHeightForWidth())
        self.lblThemeName.setSizePolicy(sizePolicy)
        self.lblThemeName.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lblThemeName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblThemeName.setObjectName("lblThemeName")
        self.gridLayout.addWidget(self.lblThemeName, 0, 0, 1, 1)
        self.pbSave = QtWidgets.QPushButton(RuleEditor)
        self.pbSave.setObjectName("pbSave")
        self.gridLayout.addWidget(self.pbSave, 4, 0, 1, 1)
        self.pbLoad = QtWidgets.QPushButton(RuleEditor)
        self.pbLoad.setAutoDefault(True)
        self.pbLoad.setDefault(True)
        self.pbLoad.setObjectName("pbLoad")
        self.gridLayout.addWidget(self.pbLoad, 4, 1, 1, 1)
        self.textEditThemeName = QtWidgets.QLineEdit(RuleEditor)
        self.textEditThemeName.setObjectName("textEditThemeName")
        self.gridLayout.addWidget(self.textEditThemeName, 0, 1, 1, 1)

        self.retranslateUi(RuleEditor)
        QtCore.QMetaObject.connectSlotsByName(RuleEditor)

    def retranslateUi(self, RuleEditor):
        _translate = QtCore.QCoreApplication.translate
        RuleEditor.setWindowTitle(_translate("RuleEditor", "RuleEditor"))
        self.gBAllInfo.setTitle(_translate("RuleEditor", "Expert System Knowlege Base Creation Elements:"))
        self.lblVariables.setText(_translate("RuleEditor", "Variables:"))
        self.pbAddVariable.setText(_translate("RuleEditor", "Add New Variable"))
        self.pbRemoveVariable.setText(_translate("RuleEditor", "Remove Selected Variable"))
        self.lblQuestions.setText(_translate("RuleEditor", "Questions:"))
        self.pbAddQuestion.setText(_translate("RuleEditor", "Add New Question"))
        self.pbRemoveQuestion.setText(_translate("RuleEditor", "Remove Selected Question"))
        self.lblOutput.setText(_translate("RuleEditor", "Output Info:"))
        self.pbUpdateOutput.setText(_translate("RuleEditor", "Update output for selected rule"))
        self.gbRules.setTitle(_translate("RuleEditor", "Rules"))
        self.pbAddRule.setText(_translate("RuleEditor", "Add New Rule"))
        self.pbUpdateRule.setText(_translate("RuleEditor", "UpdateRule"))
        self.pbRemoveRule.setText(_translate("RuleEditor", "Remove Selected Rule"))
        self.lblThemeName.setText(_translate("RuleEditor", "Enter your theme name to start"))
        self.pbSave.setText(_translate("RuleEditor", "Save Expert System Base"))
        self.pbLoad.setText(_translate("RuleEditor", "Load Expert System Base"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RuleEditor = QtWidgets.QDialog()
    ui = Ui_RuleEditor()
    ui.setupUi(RuleEditor)
    RuleEditor.show()
    sys.exit(app.exec_())

