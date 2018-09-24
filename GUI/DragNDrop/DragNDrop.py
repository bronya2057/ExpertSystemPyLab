# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DragNDrop.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DragNDrop(object):
    def setupUi(self, DragNDrop):
        DragNDrop.setObjectName("DragNDrop")
        DragNDrop.resize(881, 472)
        self.gridLayout_4 = QtWidgets.QGridLayout(DragNDrop)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget = QtWidgets.QWidget(DragNDrop)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TabWidget = QtWidgets.QTabWidget(self.widget)
        self.TabWidget.setObjectName("TabWidget")
        self.tabDragNDrop = QtWidgets.QWidget()
        self.tabDragNDrop.setObjectName("tabDragNDrop")
        self.layoutWidget = QtWidgets.QWidget(self.tabDragNDrop)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(133, 0))
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(69, 0))
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pbDragNDrop = QtWidgets.QPushButton(self.layoutWidget)
        self.pbDragNDrop.setObjectName("pbDragNDrop")
        self.horizontalLayout.addWidget(self.pbDragNDrop)
        self.TabWidget.addTab(self.tabDragNDrop, "")
        self.tabCss = QtWidgets.QWidget()
        self.tabCss.setStyleSheet("QWidget{\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(255, 170, 127);\n"
"}\n"
"\n"
"QPushButton#pushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"}")
        self.tabCss.setObjectName("tabCss")
        self.pushButton = QtWidgets.QPushButton(self.tabCss)
        self.pushButton.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tabCss)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 60, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.TabWidget.addTab(self.tabCss, "")
        self.gridLayout_2.addWidget(self.TabWidget, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(DragNDrop)
        self.TabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(DragNDrop)

    def retranslateUi(self, DragNDrop):
        _translate = QtCore.QCoreApplication.translate
        self.pbDragNDrop.setText(_translate("DragNDrop", "DragToMe"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tabDragNDrop), _translate("DragNDrop", "Drag && Drop"))
        self.pushButton.setText(_translate("DragNDrop", "PushButton"))
        self.pushButton_2.setText(_translate("DragNDrop", "PushButton"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tabCss), _translate("DragNDrop", "CSS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DragNDrop = QtWidgets.QWidget()
    ui = Ui_DragNDrop()
    ui.setupUi(DragNDrop)
    DragNDrop.show()
    sys.exit(app.exec_())

