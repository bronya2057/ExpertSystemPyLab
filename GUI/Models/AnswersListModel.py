from PyQt5.QtCore import QAbstractListModel, QModelIndex, QVariant, pyqtSignal, QAbstractTableModel, Qt

from GUI.Models.ColumnButtonDelegate import ColumnButtonDelegate
from GUI.Models.CommonSerializedData import *

answers_list = CommonSerializedData.es_answers_list


class AnswersListModel(QAbstractListModel):
    NEW_ANSWER_STR = "New answer"

    def __init__(self, parent=None, *args):
        """ datain: a list where each item is a row
        """
        QAbstractListModel.__init__(self, parent, *args)

    def data(self, index, role=None):
        if role == Qt.DisplayRole:
            print("Change Data")
            answers_list_at_selected_question = CommonSerializedData.get_answers_list_at_selected_index()
            print(answers_list_at_selected_question)
            row = index.row()
            return QVariant(answers_list_at_selected_question[row])
        else:
            return QVariant()

    def rowCount(self, parent=QModelIndex()):
        if CommonSerializedData.get_question_selection_validity():
            answers_list_at_selected_question = CommonSerializedData.get_answers_list_at_selected_index()
            return len(answers_list_at_selected_question)
        else:
            return 0

    def request_variables_for_question(self, index):
        CommonSerializedData.set_selected_question_index(index.row())

        print("Question Selected" + str(index.row()))
        answers_list_at_selected_question = CommonSerializedData.get_answers_list_at_selected_index()
        self.insertRows(0, len(answers_list_at_selected_question))
        #  self.dataChanged.emit(QModelIndex(), [])

        # self.dataChanged.emit(self.index(index.row(), 0), [])
        # if get_question_selection_validity():
    # def columnCount(self, parent=QModelIndex()):
    #     return 2  # len(self.es_themes)

    def insertRows(self, row, count, parent=None, *args, **kwargs):
        print("insert rows" + str(row) + str(count))
        self.beginInsertRows(QModelIndex(), row, count)

        self.endInsertRows()
        pass
        # self.beginInsertRows(QModelIndex(), row, row + count)
        #
        # self.endRemoveRows()

    def removeRows(self, row, count, parent=None, *args, **kwargs):
        self.beginRemoveRows(QModelIndex(), row, count)

        self.endRemoveRows()

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

        # return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def insertRow(self, row, parent=None, *args, **kwargs):
        self.beginInsertRows(QModelIndex(), row, 1)
        self.endInsertRows()

    def removeRow(self, answer, parent=None, *args, **kwargs):
        self.beginRemoveRows(QModelIndex(), answer, answer)
        temp_answer_list = CommonSerializedData.get_answers_list_at_selected_index()
        if temp_answer_list:
            del temp_answer_list[answer]
        # del answers_list[CommonSerializedData.selected_question_index][answer]
            ColumnButtonDelegate.remove_combo_box_item(CommonSerializedData.selected_question_index, answer)
        # CommonSerializedData.selected_question_index = -1
        self.endRemoveRows()

    def add_new_variable(self):
        if not (self.NEW_ANSWER_STR in CommonSerializedData.get_answers_list_at_selected_index()) and CommonSerializedData.get_question_selection_validity():
            new_row_index = len(CommonSerializedData.get_answers_list_at_selected_index())
            self.insertRow(new_row_index)
            answers_list_at_selected_question = CommonSerializedData.get_answers_list_at_selected_index()
            answers_list_at_selected_question.append(self.NEW_ANSWER_STR)
            self.set_rule_combo_box_at_index(CommonSerializedData.selected_question_index)
            self.dataChanged.emit(self.index(new_row_index, 0), self.index(new_row_index, 0), [])

    def remove_variable(self, selected_answer_index):
        if selected_answer_index > 0:
            self.removeRow(selected_answer_index)

    def setData(self, index, value, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.EditRole and value and not (value in CommonSerializedData.get_answers_list_at_selected_index()):
            CommonSerializedData.update_answer(index.row(), value)

            self.set_rule_combo_box_at_index(CommonSerializedData.selected_question_index)

            self.dataChanged.emit(index, index, [])
            return True
        return False

    def set_rule_combo_box_at_index(self, index):
        combo_box = ColumnButtonDelegate.get_combo_box_at_index(index)
        answers_list_at_selected_question = CommonSerializedData.get_answers_list_at_selected_index()
        if not (-1 == combo_box):
            combo_box.clear()
            combo_box.addItems(answers_list_at_selected_question)

    def clear_all_variables(self):
        self.removeRow(0)