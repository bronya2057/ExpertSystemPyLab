from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QAction, QFileDialog, QMainWindow, QApplication, QDialog, QRadioButton, QVBoxLayout

from Backend.EmptyExpertEngine import ExpertEngine, set_goal
from GUI.MainWindowView import Ui_MainWindow
from GUI.Models.ESThemesListModel import ESThemesListModel, ESTheme
from GUI.RuleEditorController import RuleEditorController
from collections import OrderedDict

from pyknow import *
from types import MethodType


class MainWindowController(QMainWindow):
    INITIAL_QUESTION_INDEX = 0

    def __init__(self):
        super(MainWindowController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_theme_question_dict = OrderedDict()
        self.fill_menu_bar()
        self.esThemesListModel = ESThemesListModel(self)
        self.init_es_themes_model()
        self.show()
        self.selected_question = -1
        self.questions_number = 0
        self.current_theme_facts = Fact()
    #  TO DECOUPLE JUST CREATE ANOTHER CLASS AND PASS self of this class
        self.ui.pBNextQuestion.clicked.connect(self.enable_next_question)

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

        self.esThemesListModel.load_theme('PersonalDetentionTheme.json')
        es_themes_list_view.clicked.connect(self.esThemesListModel.request_theme_at_selected_index)
        self.esThemesListModel.theme_selected.connect(self.set_initial_question)
        es_themes_list_view.setModel(self.esThemesListModel)

        engine = ExpertEngine("methodName")  # PASS ALL Rules and fact parameters

        engine.reset()

        engine.declare(Fact(myFact="Brown", myFact2="Yes"))
        # engine.add_method("Method1")
        # setattr(engine, 'rule1', set_goal())
        engine.run()
        print(engine.get_rules())

    def set_initial_question(self):
        self.ui.pBNextQuestion.setEnabled(True)
        self.selected_question = self.INITIAL_QUESTION_INDEX
        self.set_next_question()

    def enable_next_question(self):
        self.selected_question += 1
        #  Check radio that is checked and cache answer
        self.cache_fact()

        if self.selected_question < self.esThemesListModel.get_current_theme_questions_number():
            self.set_next_question()
        else:
            answers_layout = self.ui.gBAnswers.layout()
            self.clear_answers_and_questions(answers_layout)

            engine = ExpertEngine("methodName")  # PASS ALL Rules and fact parameters
            engine.reset()
            engine.declare(self.current_theme_facts)
            engine.run()
            self.current_theme_facts = Fact()

            self.ui.pBNextQuestion.setEnabled(False)



    def set_next_question(self):
        question_name, answers = self.esThemesListModel.get_current_theme_question(self.selected_question)
        if not (question_name == "" and answers == []):
            self.reset_questions_and_answers(question_name, answers)

    def reset_questions_and_answers(self, selected_question_text, answers):
        layout = self.ui.gBAnswers.layout()
        self.clear_answers_and_questions(layout)

        self.ui.lblQuestion.setText(selected_question_text)
        first_radio_flag = False

        for index, answer in enumerate(answers):
            radio = QRadioButton(answer)
            if not first_radio_flag:
                radio.setChecked(True)
                first_radio_flag = True
            layout.addWidget(radio, index)  # ADDING PADDING??

    def clear_answers_and_questions(self, answers_layout):
        self.ui.lblQuestion.setText("")
        for i in reversed(range(answers_layout.count())):
            answers_layout.itemAt(i).widget().setParent(None)

    def cache_fact(self):
        buttons = self.ui.gBAnswers.findChildren(QRadioButton)
        for button in buttons:
            if button.isChecked():
                self.current_theme_facts[self.ui.lblQuestion.text()] = button.text()
                print(button.text())

def init_gui():
    import sys
    app = QApplication(sys.argv)
    uiHandler = MainWindowController()
    app.exec_()


if __name__ == "__main__":
    init_gui()
