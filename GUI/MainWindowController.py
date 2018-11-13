from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QFileDialog, QMainWindow, QApplication, QRadioButton, QDialog, QMenu, QCheckBox, \
    QWidgetAction
from pyknow import Fact

from Backend.EmptyExpertEngine import ExpertEngine
from GUI.Common import *
from GUI.SemanticEditorController import SemanticEditorController
from GUI.Views.MainWindowView import Ui_MainWindow
from GUI.Models.Helpers.ColumnButtonDelegate import ColumnButtonDelegate
from GUI.Models.ESThemesListModel import ESThemesListModel
from GUI.RuleEditorController import RuleEditorController
from collections import OrderedDict


class MainWindowController(QMainWindow):
    INITIAL_QUESTION_INDEX = 0

    def __init__(self):
        super(MainWindowController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_theme_question_dict = OrderedDict()
        self.fill_menu_bar()
        self.esThemesListModel = ESThemesListModel(self)
        self.themes_list_menu = QMenu("Themes list menu", self)
        self.init_es_themes_model()
        self.show()
        self.selected_question = INVALID_INDEX
        self.current_theme_facts = Fact()
    #  TO DECOUPLE JUST CREATE ANOTHER CLASS AND PASS self of this class
        self.is_tooltip_needed = False
        self.set_all_tooltips()
        self.configure_ui_elements()


    ###############MENU ACTIONS###################
    def open_action(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, open_file_dialog_desc, "../" + es_knowledge_base_str_token,
                                                  open_file_dialog_label, options=options)
        if fileName:
            print(fileName)
            self.esThemesListModel.load_theme(fileName)

        self.ui.listViewESThemes.clearSelection()
        self.clear_answers_and_questions()

    def exit_action(self):
        self.close()
        pass

    def configure_ui_elements(self):
        self.ui.lblQuestion.setWordWrap(True)
        self.ui.pBNextQuestion.setEnabled(False)
        self.ui.pBNextQuestion.clicked.connect(self.enable_next_question)

    def rule_editor_action(self):
        rule_editor_controller = RuleEditorController()
        response = rule_editor_controller.exec()
        rule_editor_controller.setAttribute(Qt.WA_DeleteOnClose)
        if response == QDialog.Accepted:
            print("The Ok button clicked")
        else:
            rule_editor_controller.variables_model.remove_all_variables_in_all_questions()
            rule_editor_controller.questions_model.remove_all_questions()
            rule_editor_controller.rules_model.remove_all_rules()
            ColumnButtonDelegate.clear_editors_list()
            rule_editor_controller.deleteLater()
            print("Cancel Button")

    def semantic_editor_action(self):
        semantic_editor_controller = SemanticEditorController()
        response = semantic_editor_controller.exec()
        semantic_editor_controller.setAttribute(Qt.WA_DeleteOnClose)
        if response == QDialog.Accepted:
            print("The Ok button clicked")
        else:
            semantic_editor_controller.deleteLater()
            print("Cancel Button")

    def fill_menu_bar(self):
        menu_bar = self.ui.menubar

        file = menu_bar.addMenu("File")
        tools = menu_bar.addMenu("Tools")
        help_menu = menu_bar.addMenu("Help")

        # new_action = QAction("New", menu_bar)
        # new_action.setShortcut("Ctrl+N")
        # file.addAction(new_action)

        open_action = QAction("Open", menu_bar)
        open_action.setShortcut("Ctrl+O");
        file.addAction(open_action)

        exit_action = QAction("Exit", menu_bar)
        exit_action.setShortcut("Ctrl+Q")
        file.addAction(exit_action)

        rule_editor_action = QAction("Rule Editor", menu_bar)
        rule_editor_action.setShortcut("Ctrl+R")
        tools.addAction(rule_editor_action)

        semantic_editor_action = QAction("Semantic Editor", menu_bar)
        semantic_editor_action.setShortcut("Ctrl+Alt+S")
        tools.addAction(semantic_editor_action)

        check_box_tooltips = QCheckBox(help_menu)
        check_box_tooltips.setText("Tooltips Enabled")
        chk_box_action = QWidgetAction(help_menu)
        chk_box_action.setDefaultWidget(check_box_tooltips)
        help_menu.addAction(chk_box_action)

        open_action.triggered.connect(self.open_action)
        exit_action.triggered.connect(self.exit_action)
        rule_editor_action.triggered.connect(self.rule_editor_action)
        semantic_editor_action.triggered.connect(self.semantic_editor_action)
        check_box_tooltips.clicked.connect(self.on_check_box_tooltip_checked)


    ###############MODELS INIT###################
    def init_es_themes_model(self):
        es_themes_list_view = self.ui.listViewESThemes

        # self.esThemesListModel.load_theme('PersonalDetentionTheme.json')  # TEST ONLY
        es_themes_list_view.clicked.connect(self.esThemesListModel.request_theme_at_selected_index)
        self.esThemesListModel.theme_selected.connect(self.set_initial_question)
        es_themes_list_view.setModel(self.esThemesListModel)

        es_themes_list_view.setContextMenuPolicy(Qt.CustomContextMenu)
        es_themes_list_view.customContextMenuRequested.connect(self.on_context_menu_called)

        remove_action = QAction("Remove theme", self.themes_list_menu)
        self.themes_list_menu.addAction(remove_action)
        remove_action.triggered.connect(self.remove_menu_action_triggered)

    def set_initial_question(self):
        self.ui.gbQuestions.setTitle("QUESTIONS")
        self.ui.gBAnswers.setTitle("ANSWERS")
        self.ui.gBMain.setTitle("Expert system theme is chosen, please answer all questions")
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
            self.prepare_theme_output()

    def set_next_question(self):
        question_name, answers = self.esThemesListModel.get_current_theme_question(self.selected_question)
        if not (question_name == "" and answers == []):
            self.reset_questions_and_answers(question_name, answers)

    def reset_questions_and_answers(self, selected_question_text, answers):
        layout = self.ui.gBAnswers.layout()
        self.clear_answers_and_questions()

        self.ui.lblQuestion.setText(selected_question_text)
        first_radio_flag = False

        for index, answer in enumerate(answers):
            radio = QRadioButton(answer)
            if not first_radio_flag:
                radio.setChecked(True)
                first_radio_flag = True
            layout.addWidget(radio, index)

    def clear_answers_and_questions(self):
        answers_layout = self.ui.gBAnswers.layout()
        self.ui.lblQuestion.setText("")
        for i in reversed(range(answers_layout.count())):
            answers_layout.itemAt(i).widget().setParent(None)

    def cache_fact(self):
        buttons = self.ui.gBAnswers.findChildren(QRadioButton)
        for button in buttons:
            if button.isChecked():
                self.current_theme_facts[self.ui.lblQuestion.text()] = button.text()
                print(button.text())

    def on_context_menu_called(self, point):
        rows = self.esThemesListModel.rowCount()
        selected_theme_index = self.ui.listViewESThemes.currentIndex().row()
        print(point.y())
        if selected_theme_index >= 0 and point.y() < (remove_theme_context_menu_line_height * rows):
            self.themes_list_menu.exec_(self.ui.listViewESThemes.mapToGlobal(point))

    def remove_menu_action_triggered(self):
        selected_theme_index = self.ui.listViewESThemes.currentIndex().row()

        self.esThemesListModel.remove_theme_at(selected_theme_index)
        self.clear_answers_and_questions()
        self.ui.pBNextQuestion.setEnabled(False)

    def on_check_box_tooltip_checked(self, checked):
        self.is_tooltip_needed = checked

    def set_all_tooltips(self):
        if self.is_tooltip_needed:
            self.ui.pBNextQuestion.setToolTip("This button will be enabled when")
        else:
            self.ui.pBNextQuestion.setToolTip("")

    def prepare_theme_output(self):
        self.clear_answers_and_questions()

        current_theme_rules = self.esThemesListModel.get_current_theme_rules(self.selected_question)
        current_theme_questions = self.esThemesListModel.get_current_theme_questions()

        main_expert_engine = ExpertEngine(current_theme_questions, current_theme_rules)
        main_expert_engine.reset()
        main_expert_engine.declare(self.current_theme_facts)
        main_expert_engine.run()
        self.current_theme_facts = Fact()

        self.ui.lblQuestion.setText(main_expert_engine.get_output())
        self.ui.gbQuestions.setTitle("Your output:")
        self.ui.gBAnswers.setTitle("")
        self.ui.pBNextQuestion.setEnabled(False)
        self.ui.listViewESThemes.clearSelection()
        self.ui.gBMain.setTitle("Please choose one theme from the list")


def init_gui():
    import sys
    app = QApplication(sys.argv)
    # translator = QTranslator()
    # print("Translator")
    # print(translator.load("qt_ru", QLibraryInfo.location(QLibraryInfo.TranslationsPath)))
    # app.installTranslator(translator)
    uiHandler = MainWindowController()
    app.exec_()


if __name__ == "__main__":
    init_gui()
