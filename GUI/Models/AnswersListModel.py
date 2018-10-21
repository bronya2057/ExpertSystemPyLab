from PyQt5.QtCore import QAbstractListModel, QModelIndex, QVariant, Qt, pyqtSignal, QAbstractTableModel

from GUI.Models.CommonSerializedData import *


class AnswersListModel(QAbstractListModel):
    def __init__(self, parent=None, *args):
        """ datain: a list where each item is a row
        """
        QAbstractListModel.__init__(self, parent, *args)

    def data(self, index, role=None):
        if role == Qt.DisplayRole:
            print("Change Data")
            answers_list = CommonSerializedData.get_answers_list_at_selected_index()
            print(answers_list)
            return QVariant(answers_list[index.row()])
        else:
            return QVariant()

    def rowCount(self, parent=QModelIndex()):
        if CommonSerializedData.get_question_selection_validity():
            answers_list = CommonSerializedData.get_answers_list_at_selected_index()
            return len(answers_list)
        else:
            return 0


    def request_variables_for_question(self, index):
        CommonSerializedData.set_selected_question_index(index.row())

        print("Question Selected" + str(index.row()))
        answers_list = CommonSerializedData.get_answers_list_at_selected_index()
        self.insertRows(0, len(answers_list))
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
        pass

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

        # return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def insertRow(self, row, parent=None, *args, **kwargs):
        self.beginInsertRows(QModelIndex(), row, row)

        self.endInsertRows()

    def removeRow(self, row, parent=None, *args, **kwargs):
        self.beginInsertRows(QModelIndex(), row, row)

        self.endInsertRows()

    def add_new_variable(self):
        self.insertRow(len(self.es_themes.questions))
        # es_theme.["NewQuestion"] = []

    def remove_variable(self, question_text, selected_index):
        if selected_index > -1:
            pass
            # self.removeRow(selected_index)
            # del es_theme.questions[question_text]

    def setData(self, index, value, role=Qt.DisplayRole):
        print("setData")