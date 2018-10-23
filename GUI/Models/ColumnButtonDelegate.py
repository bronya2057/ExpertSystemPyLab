from PyQt5 import QtGui, QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QItemDelegate, QComboBox, QStyle

from GUI.Models.CommonSerializedData import *


class ColumnButtonDelegate(QItemDelegate):
    editors_list = []
    def __init__(self, owner):
        QItemDelegate.__init__(self, owner)

    @staticmethod
    def get_combo_box_at_index(index):
        if index < len(ColumnButtonDelegate.editors_list):
            return ColumnButtonDelegate.editors_list[index]
        else:
            return -1

    @staticmethod
    def remove_combo_box_at_index(index):
        if index < len(ColumnButtonDelegate.editors_list):
            del ColumnButtonDelegate.editors_list[index]

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
        answers_for_indexed_question = CommonSerializedData.get_answers_list_at_index(index.row())
        editor.addItems(answers_for_indexed_question)
        editor.setCurrentIndex(0)
        editor.installEventFilter(self)
        ColumnButtonDelegate.editors_list.append(editor)
        # self.editors_list[0].addItems(["EWTWETWE"])  #  Store reference to every combo box and update it if needed
        return editor

    def setEditorData(self, editor, index):
        value = 1
        editor.setCurrentIndex(value)

    def setModelData(self, editor, model, index):
        value = editor.currentIndex()
        model.setData(index, QtCore.QVariant(value))

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)