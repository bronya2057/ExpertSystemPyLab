from PyQt5 import QtGui, QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QItemDelegate, QComboBox, QStyle


class ColumnButtonDelegate(QItemDelegate):
    def __init__(self, owner, itemslist):
        QItemDelegate.__init__(self, owner)
        self.itemslist = itemslist

    def paint(self, painter, option, index):
        # Get Item Data
        #  value = str(index.data(Qt.DisplayRole))
        # fill style options with item data
        style = Qt.QApplication.style()
        opt = QtWidgets.QStyleOptionComboBox()
        opt.currentText = "HI"
        opt.rect = option.rect

        # draw item data as ComboBox
        style.drawComplexControl(QStyle.CC_ComboBox, opt, painter)

    def createEditor(self, parent, option, index):
        # create the ProgressBar as our editor.
        print(index.row())  # just get the needed row data from common
        editor = QComboBox(parent)
        editor.addItems(self.itemslist)
        editor.setCurrentIndex(0)
        editor.installEventFilter(self)
        return editor

    def setEditorData(self, editor, index):
        value = 1
        editor.setCurrentIndex(value)

    def setModelData(self, editor, model, index):
        value = editor.currentIndex()
        model.setData(index, QtCore.QVariant(value))

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
