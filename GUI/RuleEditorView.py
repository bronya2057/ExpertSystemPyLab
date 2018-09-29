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
        RuleEditor.resize(1006, 586)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RuleEditor.sizePolicy().hasHeightForWidth())
        RuleEditor.setSizePolicy(sizePolicy)
        self.formLayout = QtWidgets.QFormLayout(RuleEditor)
        self.formLayout.setObjectName("formLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(RuleEditor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeViewDesicions = QtWidgets.QTreeView(RuleEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeViewDesicions.sizePolicy().hasHeightForWidth())
        self.treeViewDesicions.setSizePolicy(sizePolicy)
        self.treeViewDesicions.setMinimumSize(QtCore.QSize(0, 500))
        self.treeViewDesicions.setObjectName("treeViewDesicions")
        self.horizontalLayout.addWidget(self.treeViewDesicions)
        self.tableView = QtWidgets.QTableView(RuleEditor)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        self.tableView_2 = QtWidgets.QTableView(RuleEditor)
        self.tableView_2.setObjectName("tableView_2")
        self.horizontalLayout.addWidget(self.tableView_2)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 50, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelDecisionTree = QtWidgets.QLabel(RuleEditor)
        self.labelDecisionTree.setObjectName("labelDecisionTree")
        self.horizontalLayout_2.addWidget(self.labelDecisionTree)
        self.labelRules = QtWidgets.QLabel(RuleEditor)
        self.labelRules.setObjectName("labelRules")
        self.horizontalLayout_2.addWidget(self.labelRules)
        self.label = QtWidgets.QLabel(RuleEditor)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)

        self.retranslateUi(RuleEditor)
        self.buttonBox.accepted.connect(RuleEditor.accept)
        self.buttonBox.rejected.connect(RuleEditor.reject)
        QtCore.QMetaObject.connectSlotsByName(RuleEditor)

    def retranslateUi(self, RuleEditor):
        _translate = QtCore.QCoreApplication.translate
        RuleEditor.setWindowTitle(_translate("RuleEditor", "RuleEditor"))
        self.labelDecisionTree.setText(_translate("RuleEditor", "Desicion Tree"))
        self.labelRules.setText(_translate("RuleEditor", "Rules"))
        self.label.setText(_translate("RuleEditor", "Facts"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RuleEditor = QtWidgets.QDialog()
    ui = Ui_RuleEditor()
    ui.setupUi(RuleEditor)
    RuleEditor.show()
    sys.exit(app.exec_())

