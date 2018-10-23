from PyQt5.QtCore import QAbstractListModel, QModelIndex, QVariant, Qt, pyqtSignal, QAbstractTableModel

from GUI.Models.ColumnButtonDelegate import ColumnButtonDelegate
from GUI.Models.CommonSerializedData import *
es_theme = CommonSerializedData.es_theme


class QuestionsListModel(QAbstractTableModel):
    #  theme_selected = pyqtSignal()  # define new signal
    NEW_QUESTION_STR = "NewQuestion"

    def __init__(self, parent=None, *args):
        """ datain: a list where each item is a row
        """
        QAbstractTableModel.__init__(self, parent, *args)

    def data(self, index, role=None):
        if role == Qt.DisplayRole:
            if index.column() == 0:
                questions_list = list(es_theme.questions.keys())
                return QVariant(questions_list[index.row()])
            elif index.column() == 1:
                return QVariant()
        else:
            return QVariant()

    def rowCount(self, parent=QModelIndex()):
        return len(CommonSerializedData.es_theme.questions)

    def columnCount(self, *args, **kwargs):
        return 2

    def headerData(self, section, orientation, role=None):
        if not (role == Qt.DisplayRole):
            return QVariant()
        else:
            if orientation == Qt.Horizontal:
                if section == 0:
                    return "Questions"
                elif section == 1:
                    return "Facts"


    # def columnCount(self, parent=QModelIndex()):
    #     return 2  # len(self.es_themes)

    def flags(self, index):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

        # return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def insertRow(self, row, parent=None, *args, **kwargs):
        self.beginInsertRows(QModelIndex(), row, row)
        self.endInsertRows()

    def removeRow(self, row, parent=None, *args, **kwargs):
        self.beginRemoveRows(QModelIndex(), row, row)

        self.endRemoveRows()

    def add_new_question(self):
        if not (self.NEW_QUESTION_STR in es_theme.questions):
            new_row_index = len(es_theme.questions)
            self.insertRow(new_row_index)
            es_theme.questions[self.NEW_QUESTION_STR] = []
            self.dataChanged.emit(self.index(new_row_index, 0), self.index(new_row_index, 0), [])

    def remove_question(self, question_text, selected_index):
        if selected_index > -1:
            self.removeRow(selected_index)
            ColumnButtonDelegate.remove_combo_box_at_index(selected_index)
            del es_theme.questions[question_text]

    def setData(self, index, value, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.EditRole and value and not (value in es_theme.questions):
            CommonSerializedData.update_question(index.row(), value)
            self.dataChanged.emit(index, index, [])
            return True
        return False