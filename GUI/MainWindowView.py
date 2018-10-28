# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1171, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("QLabel, QRadioButton, QGroupBox{\n"
"    font-size:16px;\n"
"    font-family:\"Courier New\";\n"
"    padding:5px;\n"
"}\n"
"\n"
"QMainWindow::separator {\n"
"    background: yellow;\n"
"    width: 10px; /* when vertical */\n"
"    height: 10px; /* when horizontal */\n"
"}\n"
"\n"
"QMainWindow::separator:hover {\n"
"    background: red;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFOECE, stop: 1 #FFFFFF);\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"    min-height:40px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QListView {\n"
"    alternate-background-color: yellow;\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListView::item:alternate {\n"
"    background: #EEEEEE;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 1px solid #6a6ea9;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
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
"QMenu {\n"
"    background-color: #ABABAB; /* sets background of the menu */\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    /* sets background of menu item. set this to something non-transparent\n"
"        if you want menu color and menu item color to be different */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QMenu::item:selected { /* when user selects item using mouse or keyboard */\n"
"    background-color: #654321;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: white;\n"
"    margin: 2px; /* some spacing around the menu */\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 2px 25px 2px 20px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    border-color: darkblue;\n"
"    background: rgba(100, 100, 100, 150);\n"
"}\n"
"\n"
"QMenu::icon:checked { /* appearance of a \'checked\' icon */\n"
"    background: gray;\n"
"    border: 1px inset gray;\n"
"    position: absolute;\n"
"    top: 1px;\n"
"    right: 1px;\n"
"    bottom: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
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
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, x3:2, y3:2,\n"
"                                      stop: 0 #dce3f4, stop: 1 #c9d4ed, stop: 2 #fff);\n"
"    margin-right:10px\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListView::item:alternate {\n"
"    background: #EEEEEE;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 1px solid #6a6ea9;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
"}")
        self.listViewESThemes.setObjectName("listViewESThemes")
        self.gridLayout.addWidget(self.listViewESThemes, 1, 0, 1, 1)
        self.gBMain = QtWidgets.QGroupBox(self.centralwidget)
        self.gBMain.setStyleSheet("QGroupBox{\n"
"    padding:10px;\n"
"    margin-top:10px;\n"
"    text-transform: uppercase;\n"
"    font-family: \"Times New Roman\";\n"
"}")
        self.gBMain.setObjectName("gBMain")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gBMain)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gbQuestions = QtWidgets.QGroupBox(self.gBMain)
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
        self.gBAnswers.setObjectName("gBAnswers")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gBAnswers)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout.addWidget(self.gBAnswers)
        self.pBNextQuestion = QtWidgets.QPushButton(self.gBMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBNextQuestion.sizePolicy().hasHeightForWidth())
        self.pBNextQuestion.setSizePolicy(sizePolicy)
        self.pBNextQuestion.setStyleSheet("QPushButton\n"
"{\n"
"    margin-top:5px\n"
"}")
        self.pBNextQuestion.setObjectName("pBNextQuestion")
        self.verticalLayout.addWidget(self.pBNextQuestion)
        self.gridLayout.addWidget(self.gBMain, 0, 1, 2, 1)
        self.lblThemes = QtWidgets.QLabel(self.centralwidget)
        self.lblThemes.setAlignment(QtCore.Qt.AlignCenter)
        self.lblThemes.setObjectName("lblThemes")
        self.gridLayout.addWidget(self.lblThemes, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1171, 21))
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
        self.pBNextQuestion.setText(_translate("MainWindow", "Next Question"))
        self.lblThemes.setText(_translate("MainWindow", "EXPERT SYSTEM THEMES"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

