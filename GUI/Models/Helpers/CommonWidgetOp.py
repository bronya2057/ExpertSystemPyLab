from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from GUI.Common import *


class CommonWidgetOp(QObject):
    def __init__(self):
        super(QObject, self).__init__()
        # print("INIT")

    @staticmethod
    def prompt_error(message, window_title="ExpertS", css="QLabel{min-width: 150px;}"):
        msg = QMessageBox()
        msg.setStyleSheet(css)
        msg.setWindowTitle(window_title)
        msg.setText(message)
        retval = msg.exec_()

    @staticmethod
    def prompt_save_dialog(description, default_path, caller_object):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(caller_object, description, default_path,
                                                   open_file_dialog_label, options=options)
        return file_name

    @staticmethod
    def prompt_open_dialog(description, default_path, caller_object):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(caller_object, description, default_path,
                                                   open_file_dialog_label, options=options)
        return file_name
