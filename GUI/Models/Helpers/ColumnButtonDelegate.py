from PyQt5.QtCore import Qt, QVariant
from PyQt5.QtWidgets import QItemDelegate, QComboBox

from GUI.Models.Helpers.CommonSerializedData import CommonSerializedData


class ColumnButtonDelegate(QItemDelegate):
    editors_list = []

    def __init__(self, owner):
        QItemDelegate.__init__(self, owner)

    @staticmethod
    def clear_editors_list():
        ColumnButtonDelegate.editors_list = []

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

    def createEditor(self, parent, option, index):
        # create the ProgressBar as our editor.
        print(index.row())  # just get the needed row data from common
        editor = QComboBox(parent)
        answers_for_indexed_question = CommonSerializedData.get_answers_list_at_index(index.row())
        editor.addItems(answers_for_indexed_question)
        editor.installEventFilter(self)
        ColumnButtonDelegate.editors_list.append(editor)
        return editor

    def setEditorData(self, editor, index):
        value = 0   # HERE SET combo box item index!!!
        editor.setCurrentIndex(value)

    def setModelData(self, editor, model, index):
        value = editor.currentIndex()
        model.setData(index, QVariant(value))

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    @staticmethod
    def set_combo_item_at_index(index, rule):
        referenced_combo = ColumnButtonDelegate.get_combo_box_at_index(index)

        if -1 != referenced_combo:
            matched_text_index = referenced_combo.findText(rule, Qt.MatchFixedString)

            if matched_text_index >= 0:
                referenced_combo.setCurrentIndex(matched_text_index)

    @staticmethod
    def get_all_combo_box_values_list():
        all_combo_box_values_list = []

        for combo_box in ColumnButtonDelegate.editors_list:
            all_combo_box_values_list.append(str(combo_box.currentText()))
        return all_combo_box_values_list
