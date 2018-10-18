from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction, QFileDialog, QMainWindow, QApplication, QDialog, QRadioButton, QVBoxLayout

from Backend.EmptyExpertEngine import ExpertEngine, set_goal
from GUI.MainWindowView import Ui_MainWindow
from GUI.Models.ESThemesListModel import ESThemesListModel, ESTheme
from GUI.RuleEditorController import RuleEditorController
from collections import OrderedDict

from pyknow import *
from types import MethodType


class MainWindowController(QMainWindow):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_theme_question_dict = OrderedDict()
        self.fill_menu_bar()
        self.init_es_themes_model()
        self.show()
        self.selected_question = -1

    ###############MENU ACTIONS###################
    def new_action(self):
        pass

    def open_action(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Json Files (*.json)", options=options)
        if fileName:
            print(fileName)

    def exit_action(self):
        self.close()
        pass

    def rule_editor_action(self):
        rule_editor_controller = RuleEditorController()
        response = rule_editor_controller.exec()
        if response == QtWidgets.QDialog.Accepted:
            print("The Ok button clicked")
        else:
            print("Cancel Button")

    def fill_menu_bar(self):
        menu_bar = self.ui.menubar

        file = menu_bar.addMenu("File")
        tools = menu_bar.addMenu("Tools")

        new_action = QAction("New", menu_bar)
        new_action.setShortcut("Ctrl+N")
        file.addAction(new_action)

        open_action = QAction("Open", menu_bar)
        open_action.setShortcut("Ctrl+O")
        file.addAction(open_action)

        exit_action = QAction("Exit", menu_bar)
        exit_action.setShortcut("Ctrl+Q")
        file.addAction(exit_action)

        rule_editor_action = QAction("Rule Editor", menu_bar)
        rule_editor_action.setShortcut("Ctrl+R")
        tools.addAction(rule_editor_action)

        # edit = file.addMenu("Edit")
        # edit.addAction("copy")
        # edit.addAction("paste")

        new_action.triggered.connect(self.new_action)
        open_action.triggered.connect(self.open_action)
        exit_action.triggered.connect(self.exit_action)
        rule_editor_action.triggered.connect(self.rule_editor_action)

    ###############MODELS INIT###################
    def init_es_themes_model(self):
        es_themes_list_view = self.ui.listViewESThemes

        # ESThemeStructure = [
        #     ESTheme("Eyes Infection Detect", OrderedDict({
        #         "What is your eyes color": ["Black", "Blue", "Brown"],
        #         "Did you Wash them with your hands": ["Yes", "No"]
        #     })
        #             ),
        #     ESTheme("ComputerProblems Detect", OrderedDict({
        #         "What is your eyes color": ["Black", "Blue", "Brown"]
        #     })
        #             )
        # ]


        esThemesListModel = ESThemesListModel(self)
        esThemesListModel.load_theme('PersonalDetentionTheme.json')
        es_themes_list_view.clicked.connect(esThemesListModel.request_theme_at_selected_index)
        esThemesListModel.theme_selected.connect(self.recieve_questions_for_current_theme)
        es_themes_list_view.setModel(esThemesListModel)

        engine = ExpertEngine("methodName")  # PASS ALL Rules and fact parameters

        engine.reset()

        engine.declare(Fact(myFact="Brown", myFact2="Yes"))
        # engine.add_method("Method1")
        # setattr(engine, 'rule1', set_goal())
        engine.run()
        print(engine.get_rules())

    def recieve_questions_for_current_theme(self, questions):
        # for k in questions.keys():
        #     print(k)
        questionList = list(questions.keys())
        answerInQuestion = list(questions.values())

        # self.ui.gBAnswers.deleteLater()
        print(questions)
        self.selected_question = 0
        self.ui.lblQuestion.setText(questionList[self.selected_question])

        #  self.ui.gBAnswers.
        # for answer in answerInQuestion:

        layout = self.ui.gBAnswers.layout()

        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

        for answer in answerInQuestion:
            layout.addWidget(QRadioButton(answer))


        #layout.addWidget(QRadioButton(answer))
        #layout.addWidget(self.ui.radioButtonTEMP)
        self.current_theme_question_dict = questions
        # self.ui.lblQuestion.setText(lisst[0])


def init_gui():
    import sys
    app = QApplication(sys.argv)
    uiHandler = MainWindowController()
    app.exec_()


if __name__ == "__main__":
    init_gui()
