from PyQt5.QtCore import QAbstractListModel, QModelIndex, QVariant, Qt, pyqtSignal


class ESTheme:
    def __init__(self, name="DummyName", questions_dictionary={}):
        self.name = name
        self.questions = questions_dictionary


class ESThemesListModel(QAbstractListModel):
    theme_selected = pyqtSignal(dict)  # define new signal

    def __init__(self, all_es_themes_data, parent=None, *args):
        """ datain: a list where each item is a row
        """
        QAbstractListModel.__init__(self, parent, *args)
        self.es_themes = all_es_themes_data

    def rowCount(self, parent=QModelIndex()):
        return len(self.es_themes)

    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.es_themes[index.row()].name)
        else:
            return QVariant()

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def request_theme_at_selected_index(self, index):
        try:
            print(self.es_themes[index.row()].name)
            self.theme_selected.emit(self.es_themes[index.row()].questions)
        except LookupError:
            print("Invalid index for selected theme")
