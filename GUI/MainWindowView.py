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
        MainWindow.resize(1020, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lblThemes = QtWidgets.QLabel(self.centralwidget)
        self.lblThemes.setObjectName("lblThemes")
        self.gridLayout.addWidget(self.lblThemes, 0, 0, 1, 1)
        self.listViewESThemes = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewESThemes.sizePolicy().hasHeightForWidth())
        self.listViewESThemes.setSizePolicy(sizePolicy)
        self.listViewESThemes.setObjectName("listViewESThemes")
        self.gridLayout.addWidget(self.listViewESThemes, 1, 0, 1, 1)
        self.gBQuestions = QtWidgets.QGroupBox(self.centralwidget)
        self.gBQuestions.setObjectName("gBQuestions")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gBQuestions)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblQuestion = QtWidgets.QLabel(self.gBQuestions)
        self.lblQuestion.setObjectName("lblQuestion")
        self.verticalLayout.addWidget(self.lblQuestion)
        self.gBAnswers = QtWidgets.QGroupBox(self.gBQuestions)
        self.gBAnswers.setObjectName("gBAnswers")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gBAnswers)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButtonTEMP = QtWidgets.QRadioButton(self.gBAnswers)
        self.radioButtonTEMP.setObjectName("radioButtonTEMP")
        self.gridLayout_2.addWidget(self.radioButtonTEMP, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.gBAnswers)
        self.pBNextQuestion = QtWidgets.QPushButton(self.gBQuestions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBNextQuestion.sizePolicy().hasHeightForWidth())
        self.pBNextQuestion.setSizePolicy(sizePolicy)
        self.pBNextQuestion.setObjectName("pBNextQuestion")
        self.verticalLayout.addWidget(self.pBNextQuestion)
        self.gridLayout.addWidget(self.gBQuestions, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 21))
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
        self.lblThemes.setText(_translate("MainWindow", "EXPERT SYSTEM THEMES"))
        self.gBQuestions.setTitle(_translate("MainWindow", "Please choose one theme from the list"))
        self.lblQuestion.setText(_translate("MainWindow", "QuestionText:"))
        self.gBAnswers.setTitle(_translate("MainWindow", "Answers"))
        self.radioButtonTEMP.setText(_translate("MainWindow", "Answer1"))
        self.pBNextQuestion.setText(_translate("MainWindow", "Next Question"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

