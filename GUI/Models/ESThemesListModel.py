from json import JSONDecodeError

from PyQt5.QtCore import QAbstractListModel, QModelIndex, QVariant, Qt, pyqtSignal
from PyQt5.QtWidgets import QMessageBox

from GUI.Models.Helpers.ESTheme import ESTheme


class ESThemesListModel(QAbstractListModel):
    theme_selected = pyqtSignal()  # define new signal

    def __init__(self, parent=None, *args):
        """ datain: a list where each item is a row
        """
        QAbstractListModel.__init__(self, parent, *args)
        self.es_themes = []
        self.selected_theme_index = 0

    def rowCount(self, parent=QModelIndex()):
        return len(self.es_themes)

    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.es_themes[index.row()].name)
        else:
            return QVariant()

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def insertRow(self, row, parent=None, *args, **kwargs):
        self.beginInsertRows(QModelIndex(), row, row)

        self.endInsertRows()

    def removeRow(self, row, parent=None, *args, **kwargs):
        self.beginRemoveRows(QModelIndex(), row, row)

        self.endRemoveRows()


    def request_theme_at_selected_index(self, index):
        try:
            self.selected_theme_index = index.row()
            self.theme_selected.emit()
        except LookupError:
            print("Invalid index for selected theme")

    def load_theme(self, file_path):
        try:
            import json
            with open(file_path) as f:
                data = json.load(f)

            add_theme = True

            for themeName in data:
                for index, theme in enumerate(self.es_themes):
                    if theme.name == themeName:
                        self.removeRow(index)
                        del self.es_themes[index]

                if add_theme:
                    self.insertRow(len(self.es_themes))
                    self.es_themes.append(ESTheme(themeName, {}, {}))
                    for i, questionText in enumerate(data[themeName]["Questions"]):
                        #  print(str(i) + " " + questionText)
                        my_list = list()
                        for variable in data[themeName]["Variables"][i]:
                            my_list.append(variable)
                        print(variable)
                        self.es_themes[-1].questions[questionText] = my_list

                    for facts, rule_output in data[themeName]["Rules"].items():
                        self.es_themes[-1].rules[facts] = rule_output
                        print(facts + " " + rule_output)
        except JSONDecodeError:
            msg = QMessageBox()
            msg.setText("Serialization failed due to file corruption")
            retval = msg.exec_()
            print("JSON file contains malicious content")



            #  print(data[themeName]["Variables"])

    def get_current_theme_question(self, question_number):
        question_list = list(self.es_themes[self.selected_theme_index].questions)
        question_val_list = list(self.es_themes[self.selected_theme_index].questions.values())

        question_text = ""
        answers_list = []

        if question_number < len(question_list):
            question_text = question_list[question_number]
            answers_list = question_val_list[question_number]

        return question_text, answers_list

    def get_current_theme_questions(self):
        return list(self.es_themes[self.selected_theme_index].questions)

    def get_current_theme_questions_number(self):
        return len(list(self.es_themes[self.selected_theme_index].questions))

    def get_current_theme_rules(self, question_number):
        return self.es_themes[self.selected_theme_index].rules

    def remove_theme_at(self, selected_theme_index):
        if len(self.es_themes) > selected_theme_index > -1:
            self.removeRow(selected_theme_index)
            del self.es_themes[selected_theme_index]


