from PyQt5 import QtGui, QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QItemDelegate, QComboBox, QStyle

from GUI.Models.CommonSerializedData import *


class ColumnButtonDelegate(QItemDelegate):
    editors_list = []
    def __init__(self, owner):
        QItemDelegate.__init__(self, owner)

    @staticmethod
    def get_combo_box_at_index(index):
        if index < len(ColumnButtonDelegate.editors_list) and not (index == -1):
            return ColumnButtonDelegate.editors_list[index]
        else:
            return -1

    @staticmethod
    def remove_combo_box_at_index(index):
        if index < len(ColumnButtonDelegate.editors_list):
            del ColumnButtonDelegate.editors_list[index]

    @staticmethod
    def remove_combo_box_item(question_index, answer_index):
        if question_index < len(ColumnButtonDelegate.editors_list):
            if answer_index < ColumnButtonDelegate.editors_list[question_index].count():
                ColumnButtonDelegate.editors_list[question_index].removeItem(answer_index)

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
        # AllItems = [editor.itemText(i) for i in range(editor.count())]
        editor.installEventFilter(self)
        ColumnButtonDelegate.editors_list.append(editor)
        # self.editors_list[0].addItems(["EWTWETWE"])  #  Store reference to every combo box and update it if needed
        return editor

    def setEditorData(self, editor, index):
        value = 0   # HERE SET combo box item index!!!
        editor.setCurrentIndex(value)

    def setModelData(self, editor, model, index):
        value = editor.currentIndex()
        model.setData(index, QtCore.QVariant(value))

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    @staticmethod
    def set_combo_item_at_index(index, rule):
        referenced_combo = ColumnButtonDelegate.get_combo_box_at_index(index)

        if -1 != referenced_combo:
            matched_text_index = referenced_combo.findText(rule, QtCore.Qt.MatchFixedString)

            if matched_text_index >= 0:
                referenced_combo.setCurrentIndex(matched_text_index)

    @staticmethod
    def get_all_combo_box_values_list():
        all_combo_box_values_list = []

        for combo_box in ColumnButtonDelegate.editors_list:
            # print(str(combo_box.currentText()))
            # combo_box_value = combo_box.itemData(combo_box.currentIndex())
            # print(combo_box_value)
            all_combo_box_values_list.append(str(combo_box.currentText()))
        return all_combo_box_values_list