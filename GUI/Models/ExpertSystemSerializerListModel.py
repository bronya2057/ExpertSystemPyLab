from PyQt5.QtCore import QAbstractListModel, QModelIndex, QVariant, Qt, pyqtSignal, QAbstractTableModel
from pyknow import Rule, Fact

from GUI.Models.Common import ESTheme


class ExpertSystemSerializerListModel(QAbstractTableModel):
    #  theme_selected = pyqtSignal()  # define new signal

    def __init__(self, parent=None, *args):
        """ datain: a list where each item is a row
        """
        QAbstractListModel.__init__(self, parent, *args)
        self.es_themes = ESTheme("SOME NAME",
                                 {"How many calories" : ["1000-2000", "3000-4000"],
                                  "Veg?": ["Veg", "NotVeg"]},
                                 {"1000-2000" : "Oh My"})

    def data(self, index, role=None):
        if role == Qt.DisplayRole:
            if index.column() == 0:
                questions_list = list(self.es_themes.questions.keys())
                return QVariant(questions_list[index.row()])
            elif index.column() == 1:
                return QVariant()
        else:
            return QVariant()

    def rowCount(self, parent=QModelIndex()):
        return len(self.es_themes.questions)

    def columnCount(self, *args, **kwargs):
        return 2

    # def columnCount(self, parent=QModelIndex()):
    #     return 2  # len(self.es_themes)

    def flags(self, index):
        if index.column() == 1:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable
        return QAbstractTableModel.flags(self, index)

        # return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def insertRow(self, row, parent=None, *args, **kwargs):
        self.beginInsertRows(QModelIndex(), row, row)

        self.endInsertRows()

    def removeRow(self, row, parent=None, *args, **kwargs):
        self.beginInsertRows(QModelIndex(), row, row)

        self.endInsertRows()

    def add_new_question(self):
        self.insertRow(len(self.es_themes.questions))
        self.es_themes.questions["NewQuestion"] = []

    def remove_question(self, question_text,selected_index):
        if selected_index > -1:
            self.removeRow(selected_index)
            del self.es_themes.questions[question_text]

    def setData(self, index, value, role=Qt.DisplayRole):
        print("setData")