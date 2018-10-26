from PyQt5.QtCore import QModelIndex, QVariant, Qt, QAbstractTableModel

from GUI.Models.ColumnButtonDelegate import ColumnButtonDelegate
from GUI.Models.CommonSerializedData import CommonSerializedData

questions_list = CommonSerializedData.es_questions_list
answers_list = CommonSerializedData.es_answers_list


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
                return QVariant(questions_list[index.row()])
            elif index.column() == 1:
                return QVariant()
        else:
            return QVariant()

    def rowCount(self, parent=QModelIndex()):
        return len(questions_list)

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

    def flags(self, index):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def insertRow(self, row, parent=None, *args, **kwargs):
        self.beginInsertRows(QModelIndex(), row, row)
        self.endInsertRows()

    def removeRow(self, row, parent=None, *args, **kwargs):
        self.beginRemoveRows(QModelIndex(), row, row)

        self.endRemoveRows()

    def add_new_question(self, new_question_text=NEW_QUESTION_STR):
        if not (new_question_text in questions_list):
            new_row_index = len(questions_list)
            self.insertRow(new_row_index)
            questions_list.insert(new_row_index, new_question_text)
            # CommonSerializedData.set_selected_question_index(new_row_index)
            answers_list.insert(new_row_index, ["New answer"])
            CommonSerializedData.add_variable_to_all_rules_to(new_row_index)
            self.dataChanged.emit(self.index(new_row_index, 0), self.index(new_row_index, 0), [])

    def add_question_from_file(self, new_question_text):
        if not (new_question_text in questions_list):
            new_row_index = len(questions_list)
            self.insertRow(new_row_index)
            questions_list.insert(new_row_index, new_question_text)
            self.dataChanged.emit(self.index(new_row_index, 0), self.index(new_row_index, 0), [])

    def remove_question(self, selected_index):
        if selected_index > -1:
            self.removeRow(selected_index)
            ColumnButtonDelegate.remove_combo_box_at_index(selected_index)
            del questions_list[selected_index]
            del answers_list[selected_index]
            CommonSerializedData.remove_rule_variable_at(selected_index)
            CommonSerializedData.selected_question_index = -1

    def setData(self, index, value, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.EditRole and value and not (value in questions_list):
            CommonSerializedData.update_question(index.row(), value)
            self.dataChanged.emit(index, index, [])
            return True
        return False

    def remove_all_questions(self):
        for question in range(CommonSerializedData.get_questions_len()):
            self.remove_question(0)

    def add_questions_from_file(self, all_questions):
        for question in all_questions:
            self.add_question_from_file(question)