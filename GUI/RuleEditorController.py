from PyQt5 import QtCore, Qt
from PyQt5.QtWidgets import QAction, QFileDialog, QApplication, QDialog, QToolBar

from GUI.Models.ColumnButtonDelegate import ColumnButtonDelegate
from GUI.Models.ExpertSystemSerializerListModel import ExpertSystemSerializerListModel
from GUI.RuleEditorView import Ui_RuleEditor


class RuleEditorController(QDialog):
    def __init__(self):
        super(RuleEditorController, self).__init__()
        self.ui = Ui_RuleEditor()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.show()
        self.ui.textEditThemeName.textChanged.connect(self.on_text_edit_theme_name_changed)

        self.ui.pbAddQuestion.clicked.connect(self.on_add_question_clicked)
        self.ui.pbRemoveQuestion.clicked.connect(self.on_remove_question_clicked)

        self.ui.pbAddVariable.clicked.connect(self.on_add_variable_clicked)
        self.ui.pbRemoveVariable.clicked.connect(self.on_remove_variable_clicked)

        self.ui.pbAddRule.clicked.connect(self.on_add_rule_clicked)
        self.ui.pbRemoveRule.clicked.connect(self.on_remove_rule_clicked)
        self.ui.pbRenameRule.clicked.connect(self.on_rename_rule_clicked)

        self.ui.pbSave.clicked.connect(self.on_save_clicked)

        self.model = ExpertSystemSerializerListModel(self)
        self.ui.listViewQuestions.setModel(self.model)
        self.ui.listViewVariables.setModel(self.model)
        #  self.ui.listViewVariables.setModelColumn(1)
        self.ui.tableViewRules.setModel(self.model)

        self.checkValues = ['TODO', 'WAITING', 'RETAKE', 'OK']

        self.ui.tableViewRules.setItemDelegateForColumn(1, ColumnButtonDelegate(self, self.checkValues))
        for row in range(0, self.model.rowCount()):
            self.ui.tableViewRules.openPersistentEditor(self.model.index(row, 1))
        #  FOR TEST ONLY
        self.ui.textEditThemeName.setText("My test theme")

    def on_text_edit_theme_name_changed(self):
        theme_name = self.ui.textEditThemeName.toPlainText()

        enable_all_elements = True if theme_name else False
        self.ui.gBAllInfo.setEnabled(enable_all_elements)

    def on_add_question_clicked(self):
        self.model.add_new_question()
        print("add question")

    def on_remove_question_clicked(self):
        index = self.ui.listViewQuestions.currentIndex()
        item_text = str(index.data())
        self.model.remove_question(item_text, index.row())

    def on_add_variable_clicked(self):
        print("add var")

    def on_remove_variable_clicked(self):
        print("rem var")

    def on_add_rule_clicked(self):
        print("add rule")

    def on_remove_rule_clicked(self):
        print("remove rule")

    def on_rename_rule_clicked(self):
        print("rename rule")

    def on_save_clicked(self):
        print("save")



def init_rule_editor_gui():
    import sys
    app = QApplication(sys.argv)
    rule_editor = RuleEditorController()
    app.exec_()


if __name__ == "__main__":
    init_rule_editor_gui()
