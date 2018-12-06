import json
import os

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

from Backend import Serializer
from GUI.Common import *
from GUI.Models.Helpers.CommonSerializedData import CommonSerializedData
from GUI.Models.AnswersListModel import AnswersListModel
from GUI.Models.Helpers.ColumnButtonDelegate import ColumnButtonDelegate
from GUI.Models.QuestionsListModel import QuestionsListModel
from GUI.Models.RulesListModel import RulesListModel
from GUI.Views.RuleEditorView import Ui_RuleEditor


class RuleEditorController(QDialog):
    def __init__(self):
        super(RuleEditorController, self).__init__()
        self.ui = Ui_RuleEditor()
        self.ui.setupUi(self)
        # self.setFixedSize(self.size())
        self.show()
        self.questions_model = QuestionsListModel(self)
        self.variables_model = AnswersListModel(self)
        self.rules_model = RulesListModel(self)
        self.init_models()
        self.init_ui_components()
        self.clear_all()

    def init_models(self):
        self.ui.listViewQuestions.setModel(self.questions_model)
        self.ui.listViewQuestions.clicked.connect(self.variables_model.request_variables_for_question)
        self.questions_model.dataChanged.connect(self.new_question_added)

        self.ui.listViewVariables.setModel(self.variables_model)
        self.ui.tableViewRules.setModel(self.questions_model)
        self.ui.listViewRules.setModel(self.rules_model)
        self.ui.listViewRules.clicked.connect(self.request_all_data_for_rule)

        # for col in range(self.questions_model.columnCount()):
            # self.ui.tableViewRules.setColumnWidth(col, 250)

        self.ui.tableViewRules.setColumnWidth(0, 200)
        self.ui.tableViewRules.setColumnWidth(1, 250)
        self.update_rule_components_state(False)

        self.ui.tableViewRules.setItemDelegateForColumn(1, ColumnButtonDelegate(self))
        for row in range(0, self.questions_model.rowCount()):
            self.ui.tableViewRules.openPersistentEditor(self.questions_model.index(row, 1))

    def init_ui_components(self):
        self.ui.textEditThemeName.textChanged.connect(self.on_text_edit_theme_name_changed)

        self.ui.pbAddQuestion.clicked.connect(self.on_add_question_clicked)
        self.ui.pbRemoveQuestion.clicked.connect(self.on_remove_question_clicked)

        self.ui.pbAddVariable.clicked.connect(self.on_add_variable_clicked)
        self.ui.pbRemoveVariable.clicked.connect(self.on_remove_variable_clicked)

        self.ui.pbAddRule.clicked.connect(self.on_add_rule_clicked)
        self.ui.pbRemoveRule.clicked.connect(self.on_remove_rule_clicked)

        self.ui.pbSave.clicked.connect(self.on_save_clicked)
        self.ui.pbLoad.clicked.connect(self.on_load_clicked)

        self.ui.pbUpdateRule.clicked.connect(self.on_pb_update_rule_clicked)
        self.ui.pbUpdateOutput.clicked.connect(self.update_output_for_selected_rule)

        self.ui.textEditThemeName.setText("")

    def on_text_edit_theme_name_changed(self):
        theme_name = self.ui.textEditThemeName.text()

        enable_all_elements = True if theme_name else False
        self.ui.gBAllInfo.setEnabled(enable_all_elements)
        self.ui.pbSave.setEnabled(enable_all_elements)
        CommonSerializedData.set_theme_name(theme_name)

    def on_add_question_clicked(self):
        self.questions_model.add_new_question()

    def on_remove_question_clicked(self):
        index = self.ui.listViewQuestions.currentIndex()
        self.questions_model.remove_question(index.row())
        self.ui.listViewQuestions.clearSelection()
        self.variables_model.clear_all_variables()

    def on_add_variable_clicked(self):
        self.variables_model.add_new_variable()

    def on_remove_variable_clicked(self):
        index = self.ui.listViewVariables.currentIndex()
        self.variables_model.remove_variable(index.row())
        self.ui.listViewVariables.clearSelection()

    def on_add_rule_clicked(self):
        self.rules_model.add_rule()

    def on_remove_rule_clicked(self):
        self.ui.listViewRules.clearSelection()
        self.update_rule_components_state(False)
        index = self.ui.listViewRules.currentIndex()
        self.rules_model.remove_rule(index.row())
        self.ui.textEditOutput.setText("")

    def new_question_added(self, index1, index2):
        for row in range(0, self.questions_model.rowCount()):
            self.ui.tableViewRules.openPersistentEditor(self.questions_model.index(row, 1))

    def request_all_data_for_rule(self):
        self.update_rule_components_state(True)
        index = self.ui.listViewRules.currentIndex()
        self.rules_model.set_all_combo_boxes_for_selected_rule(index.row())
        output = self.rules_model.get_output_for_selected_rule(index.row())
        self.ui.textEditOutput.setText(output)

    def update_rule_components_state(self, is_enabled):
        self.ui.tableViewRules.setEnabled(is_enabled)
        self.ui.textEditOutput.setEnabled(is_enabled)

    def update_output_for_selected_rule(self):
        index = self.ui.listViewRules.currentIndex()
        output = self.ui.textEditOutput.toPlainText()
        self.rules_model.update_output_for_selected_rule(index.row(), output)

    def on_pb_update_rule_clicked(self):
        complete_rule_list = ColumnButtonDelegate.get_all_combo_box_values_list()
        print(complete_rule_list)
        index = self.ui.listViewRules.currentIndex()
        self.rules_model.update_rule_at(index.row(), complete_rule_list)

    def on_save_clicked(self):
        data = Serializer.get_json_ready_data()

        json_str = json.dumps(data, indent=2)
        print(json_str)

        file_name = self.ui.textEditThemeName.text()
        file_path = os.path.join(os.path.dirname(os.getcwd()), es_knowledge_base_str_token)
        file_path = os.path.join(file_path, production_str_token)
        full_file_path = os.path.join(file_path, file_name  + extention_separator_token + es_extension_token)
        print(full_file_path)

        try:
            with open(full_file_path, "w") as write_file:
                json.dump(data, write_file, indent=2)
        except OSError as e:
            RuleEditorController.prompt_error("Theme name too big")

    def on_load_clicked(self):
        from PyQt5.QtWidgets import QFileDialog

        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, open_file_dialog_desc, "../" + es_knowledge_base_str_token + "/" + production_str_token,
                                                  open_file_dialog_label, options=options)
        if fileName:
            print(fileName)
            theme_struct = Serializer.de_serialize_to_internal_data(fileName)
            if not theme_struct == INVALID_INDEX:
                self.clear_all()

                CommonSerializedData.set_theme_name(theme_struct.theme_name)

                self.ui.textEditThemeName.setText(theme_struct.theme_name)
                self.questions_model.add_questions_from_file(theme_struct.questions_list)
                self.variables_model.add_variables_from_file(theme_struct.answers_list)
                self.rules_model.add_rules_from_file(theme_struct.rules_struct)
            else:
                RuleEditorController.prompt_error("Serialization failed due to file corruption")
        print("load")

    def clear_all(self):
        self.variables_model.remove_all_variables_in_all_questions()
        self.questions_model.remove_all_questions()
        self.rules_model.remove_all_rules()
        self.ui.textEditOutput.setText("")
        ColumnButtonDelegate.clear_editors_list()

    @staticmethod
    def prompt_error(error_text):
        msg = QMessageBox()
        msg.setText(error_text)
        retval = msg.exec_()

def init_rule_editor_gui():
    import sys
    app = QApplication(sys.argv)
    rule_editor = RuleEditorController()
    app.exec_()


if __name__ == "__main__":
    init_rule_editor_gui()
