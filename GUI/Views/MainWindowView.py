# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1157, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("QMainWindow, QWidget{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #697378, stop: 1 #96A4AD);\n"
"\n"
"    \n"
"\n"
"}\n"
"\n"
"*{\n"
"    font-size:14px;\n"
"    font-family:\"Bahnschrift\";\n"
"    padding:5px;\n"
"    color:white;\n"
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
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listViewESThemes = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewESThemes.sizePolicy().hasHeightForWidth())
        self.listViewESThemes.setSizePolicy(sizePolicy)
        self.listViewESThemes.setStyleSheet("QListView {\n"
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
"}")
        self.listViewESThemes.setObjectName("listViewESThemes")
        self.gridLayout.addWidget(self.listViewESThemes, 1, 0, 1, 1)
        self.gBMain = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gBMain.sizePolicy().hasHeightForWidth())
        self.gBMain.setSizePolicy(sizePolicy)
        self.gBMain.setStyleSheet("QGroupBox{\n"
"        background-color: #697378;\n"
"            border: 2px solid #96A4AD;\n"
"    border-radius: 5px;\n"
"    margin-top: 3ex; /* leave space at the top for the title */\n"
"text-transform: uppercase;\n"
"}")
        self.gBMain.setAlignment(QtCore.Qt.AlignCenter)
        self.gBMain.setObjectName("gBMain")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gBMain)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gbQuestions = QtWidgets.QGroupBox(self.gBMain)
        self.gbQuestions.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #697378, stop: 1 #96A4AD);\n"
"}")
        self.gbQuestions.setAlignment(QtCore.Qt.AlignCenter)
        self.gbQuestions.setObjectName("gbQuestions")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gbQuestions)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblQuestion = QtWidgets.QLabel(self.gbQuestions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblQuestion.sizePolicy().hasHeightForWidth())
        self.lblQuestion.setSizePolicy(sizePolicy)
        self.lblQuestion.setStyleSheet("")
        self.lblQuestion.setText("")
        self.lblQuestion.setObjectName("lblQuestion")
        self.verticalLayout_2.addWidget(self.lblQuestion)
        self.verticalLayout.addWidget(self.gbQuestions)
        self.gBAnswers = QtWidgets.QGroupBox(self.gBMain)
        self.gBAnswers.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #697378, stop: 1 #96A4AD);\n"
"}")
        self.gBAnswers.setAlignment(QtCore.Qt.AlignCenter)
        self.gBAnswers.setObjectName("gBAnswers")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gBAnswers)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout.addWidget(self.gBAnswers)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbGraph = QtWidgets.QPushButton(self.gBMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbGraph.sizePolicy().hasHeightForWidth())
        self.pbGraph.setSizePolicy(sizePolicy)
        self.pbGraph.setObjectName("pbGraph")
        self.horizontalLayout.addWidget(self.pbGraph)
        self.pBNextQuestion = QtWidgets.QPushButton(self.gBMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBNextQuestion.sizePolicy().hasHeightForWidth())
        self.pBNextQuestion.setSizePolicy(sizePolicy)
        self.pBNextQuestion.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pBNextQuestion.setStyleSheet("")
        self.pBNextQuestion.setObjectName("pBNextQuestion")
        self.horizontalLayout.addWidget(self.pBNextQuestion)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.gBMain, 0, 1, 2, 1)
        self.lblThemes = QtWidgets.QLabel(self.centralwidget)
        self.lblThemes.setAlignment(QtCore.Qt.AlignCenter)
        self.lblThemes.setObjectName("lblThemes")
        self.gridLayout.addWidget(self.lblThemes, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1157, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ExpertS"))
        self.gBMain.setTitle(_translate("MainWindow", "Please choose one theme from the list"))
        self.gbQuestions.setTitle(_translate("MainWindow", "Questions"))
        self.gBAnswers.setTitle(_translate("MainWindow", "Answers"))
        self.pbGraph.setText(_translate("MainWindow", "Show Graph"))
        self.pBNextQuestion.setText(_translate("MainWindow", "Next\n"
"Question"))
        self.lblThemes.setText(_translate("MainWindow", "EXPERT SYSTEM THEMES"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

