from PyQt5.QtCore import QAbstractListModel, QModelIndex, QVariant, Qt, pyqtSignal
from pyknow import Rule, Fact

class ESTheme:
    def __init__(self, name="DummyName", questions_dictionary={}):
        self.name = name
        self.questions = questions_dictionary
        # self.rule = Fact(eye_color="Blue", washed_with_hands="Yes")


class ESThemesListModel(QAbstractListModel):
    theme_selected = pyqtSignal(dict)  # define new signal

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

    def request_theme_at_selected_index(self, index):
        try:
            self.selected_theme_index = index.row()
            print(self.es_themes[index.row()].name)
            self.theme_selected.emit(self.es_themes[index.row()].questions)
        except LookupError:
            print("Invalid index for selected theme")

    def load_theme(self, file_path):
        import json
        import copy
        with open(file_path) as f:
            data = json.load(f)

        for themeName in data:
            self.es_themes.append(ESTheme(themeName, {}))
            for i, questionText in enumerate(data[themeName]["Questions"]):
                #  print(str(i) + " " + questionText)
                my_list = list()
                for variable in data[themeName]["Variables"][i]:
                   my_list.append(variable)
                print(variable)
                self.es_themes[-1].questions[questionText] = my_list

            #  print(data[themeName]["Variables"])

    def get_current_theme_question(self, question_number):
        questionList = list(self.es_themes[self.selected_theme_index].questions)
        questionVal = list(self.es_themes[self.selected_theme_index].questions.values())
        myQuestion = {}
        myQuestion[questionList[question_number]] = questionVal[question_number]
        print(myQuestion)

