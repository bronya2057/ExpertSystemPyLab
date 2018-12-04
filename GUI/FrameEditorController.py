import os

from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QFileDialog

from GUI.Common import *
from GUI.Models.FrameTreeModel import FrameTreeModel
from GUI.Views.FrameEditorView import Ui_FrameEditor


class FrameEditorController(QDialog):
    def __init__(self):
        super(FrameEditorController, self).__init__()
        self.ui = Ui_FrameEditor()
        self.ui.setupUi(self)
        self.init_gui()
        self.show()
        self.frame_model = FrameTreeModel()

    def init_gui(self):

        # self.ui.listViewESThemes.clearSelection()
        # self.clear_answers_and_questions()
        self.ui.pbLoad.clicked.connect(self.on_pb_load_clicked)
        self.ui.pbAddObject.clicked.connect(self.on_pb_add_new_item_clicked)
        self.ui.pbRemoveObject.clicked.connect(self.on_pb_remove_item_clicked)

    def on_pb_load_clicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, open_file_dialog_desc, "../" + es_knowledge_base_str_token + "/" + frame_str_token,
                                                  open_file_dialog_label, options=options)
        if fileName:
            print(fileName)
            self.frame_model.load_frame_file(fileName)
            self.ui.treeViewFrames.setModel(self.frame_model)

    def on_pb_add_new_item_clicked(self):
        index = self.ui.treeViewFrames.currentIndex()
        self.frame_model.add_item_at(index)

    def on_pb_remove_item_clicked(self):
        index = self.ui.treeViewFrames.currentIndex()
        self.frame_model.remove_item_at(index)

    def clear_all(self):
        pass

    @staticmethod
    def prompt_error(error_text):
        msg = QMessageBox()
        msg.setText(error_text)
        retval = msg.exec_()



def init_frame_editor_gui():
    import sys
    app = QApplication(sys.argv)
    frame_editor = FrameEditorController()
    app.exec_()


if __name__ == "__main__":
    init_frame_editor_gui()
