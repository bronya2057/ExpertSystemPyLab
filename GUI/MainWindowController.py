from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QFileDialog, QMainWindow, QApplication, QRadioButton, QDialog, QMenu, QCheckBox, \
    QWidgetAction
from pyknow import Fact

from Backend.EmptyExpertEngine import ExpertEngine
from GUI.Common import *
from GUI.FrameEditorController import FrameEditorController
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
        self.current_theme_output = ""
        self.init_es_themes_model()
        self.show()
        self.selected_question = INVALID_INDEX
        self.current_theme_facts = Fact()
    #  TO DECOUPLE JUST CREATE ANOTHER CLASS AND PASS self of this class
        self.is_tooltip_needed = False
        self.set_all_tooltips()
        self.configure_ui_elements()

        #TEST
        # self.esThemesListModel.load_theme("c:/Users/ABrodskyi/Dropbox/ProgrammingMaterial/Python/ExpertSystem/ESKnowledgeBase/PersonalDetention.json")
        #self.esThemesListModel.load_theme("c:/Users/Alexander/Dropbox/ProgrammingMaterial/Python/ExpertSystem/ESKnowledgeBase/PersonalDetention.json")

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
        self.ui.pbGraph.setEnabled(False)
        self.ui.pBNextQuestion.clicked.connect(self.enable_next_question)
        self.ui.pbGraph.clicked.connect(self.build_decision_graph)

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

    def frame_editor_action(self):
        frame_editor_controller = FrameEditorController()
        response = frame_editor_controller.exec()
        frame_editor_controller.setAttribute(Qt.WA_DeleteOnClose)
        if response == QDialog.Accepted:
            print("The Ok button clicked")
        else:
            frame_editor_controller.deleteLater()
            print("Cancel Button")

    def fill_menu_bar(self):
        menu_bar = self.ui.menubar

        file = menu_bar.addMenu("File")
        tools = menu_bar.addMenu("Tools")
        help_menu = menu_bar.addMenu("Help")

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

        frame_editor_action = QAction("Frame Editor", menu_bar)
        frame_editor_action.setShortcut("Ctrl+Alt+F")
        tools.addAction(frame_editor_action)

        check_box_tooltips = QCheckBox(help_menu)
        check_box_tooltips.setText("Tooltips Enabled")
        chk_box_action = QWidgetAction(help_menu)
        chk_box_action.setDefaultWidget(check_box_tooltips)
        help_menu.addAction(chk_box_action)

        open_action.triggered.connect(self.open_action)
        exit_action.triggered.connect(self.exit_action)
        rule_editor_action.triggered.connect(self.rule_editor_action)
        semantic_editor_action.triggered.connect(self.semantic_editor_action)
        frame_editor_action.triggered.connect(self.frame_editor_action)
        check_box_tooltips.clicked.connect(self.on_check_box_tooltip_checked)

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
        self.current_theme_facts = Fact()
        self.ui.gbQuestions.setTitle("QUESTIONS")
        self.ui.gBAnswers.setTitle("ANSWERS")
        self.ui.gBMain.setTitle("Expert system theme is chosen, please answer all questions")
        self.ui.pbGraph.setEnabled(False)
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
        self.ui.pbGraph.setEnabled(False)

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
        self.current_theme_output = main_expert_engine.get_output()

        self.ui.lblQuestion.setText(main_expert_engine.get_output())
        self.ui.gbQuestions.setTitle("Your output:")
        self.ui.gBAnswers.setTitle("")
        self.ui.pBNextQuestion.setEnabled(False)
        self.ui.listViewESThemes.clearSelection()
        self.ui.gBMain.setTitle("Please choose one theme from the list")
        self.ui.pbGraph.setEnabled(True)

    def build_decision_graph(self):
        import pydotplus
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg

        graph = pydotplus.Dot(graph_type='digraph')
        node_a = pydotplus.Node("Node A", style="filled", fillcolor="red")
        node_b = pydotplus.Node("Node B", style="filled", fillcolor="green")
        node_c = pydotplus.Node("Node C", style="filled", fillcolor="#0000ff")
        node_d = pydotplus.Node("Node D", style="filled", fillcolor="#976856")

        graph.add_node(node_a)
        graph.add_node(node_b)
        graph.add_node(node_c)
        graph.add_node(node_d)

        graph.add_edge(pydotplus.Edge(node_a, node_b, label="Yes"))
        graph.add_edge(pydotplus.Edge(node_a, node_c, label="No"))
        graph.add_edge(pydotplus.Edge(node_b, node_c, label="No"))
        graph.add_edge(pydotplus.Edge(node_c, node_d, label="Maybe"))

        graph.add_edge(pydotplus.Edge(node_d, node_a, label="and back we go again", labelfontcolor="#009933", fontsize="10.0", color="blue"))

        questions_graph = pydotplus.Dot(graph_type='digraph')

        questions = self.esThemesListModel.get_current_questions_and_answers()
        # for question, answers in questions.items():
        #     # question = self.esThemesListModel.get_current_theme_question(question_index)
        #     print("GEW")

        # prev_node = pydotplus.Node()
        # prev_key = ""

        selected_prev_node = pydotplus.Node()
        ultimate_prev_node = pydotplus.Node()
        rootNode = pydotplus.Node("ROOT", style="filled", fillcolor="green")
        node_to_attach = rootNode
        questions_graph.add_node(rootNode)

        facts = self.current_theme_facts
        questions_and_selected_answer = {}

        for fact, value in facts.items():
            questions_and_selected_answer[fact] = value
            print(fact)

        for index, key in enumerate(questions):
            for answer in questions[key]:

                node = pydotplus.Node(answer, style="filled", fillcolor="green")
                questions_graph.add_node(node)

                fill_color = ""
                label_str = ""
                edge_color = ""

                if index > 0:
                    node_to_attach = ultimate_prev_node
                    if answer == facts[key] and selected_prev_node.get_name() != '""':
                        label_str = key
                        edge_color = "blue"
                        fill_color = "green"
                    else:
                        label_str = ""
                        edge_color = "white"
                else:
                    node_to_attach = rootNode
                    if answer == facts[key]:
                        edge_color = "blue"
                        label_str = key
                        fill_color = "green"
                    else:
                        label_str = ""
                        edge_color = "white"

                if answer == facts[key]:
                    selected_prev_node = node

                node = pydotplus.Node(answer, style="filled", fillcolor=fill_color)
                questions_graph.add_node(node)
                questions_graph.add_edge(pydotplus.Edge(node_to_attach, node, label=label_str, labelfontcolor="#009933", fontsize="10.0",color=edge_color))

            ultimate_prev_node = selected_prev_node

        node = pydotplus.Node(self.ui.lblQuestion.text(), style="filled", fillcolor="Grey")
        questions_graph.add_node(node)
        questions_graph.add_edge(pydotplus.Edge(ultimate_prev_node, node, label="RESULT", labelfontcolor="#009933", fontsize="10.0",color="blue"))

        facts = self.current_theme_facts
        for fact, value in facts.items():
            print(fact)
        questions_graph.write_png('example2_graph.png')
        img = mpimg.imread('example2_graph.png')
        plt.imshow(img)
        plt.show()

def init_gui():
    import sys
    app = QApplication(sys.argv)
    uiHandler = MainWindowController()
    app.exec_()


if __name__ == "__main__":
    init_gui()
