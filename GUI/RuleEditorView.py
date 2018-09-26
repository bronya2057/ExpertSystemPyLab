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
        RuleEditor.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(RuleEditor)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(RuleEditor)
        self.buttonBox.accepted.connect(RuleEditor.accept)
        self.buttonBox.rejected.connect(RuleEditor.reject)
        QtCore.QMetaObject.connectSlotsByName(RuleEditor)

    def retranslateUi(self, RuleEditor):
        _translate = QtCore.QCoreApplication.translate
        RuleEditor.setWindowTitle(_translate("RuleEditor", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RuleEditor = QtWidgets.QDialog()
    ui = Ui_RuleEditor()
    ui.setupUi(RuleEditor)
    RuleEditor.show()
    sys.exit(app.exec_())

