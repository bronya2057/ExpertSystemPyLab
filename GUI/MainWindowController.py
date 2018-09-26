from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction, QFileDialog, QMainWindow, QApplication, QDialog

from GUI.MainWindowView import Ui_MainWindow
from GUI.RuleEditorController import RuleEditorController


class MainWindowController(QMainWindow):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fillMenuBar()
        self.show()

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
        responce = rule_editor_controller.exec()
        if responce == QtWidgets.QDialog.Accepted:
            print("The Ok button clicked")
        else:
            print("Cancel Button")


    def fillMenuBar(self):
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


def init_gui():
    import sys
    app = QApplication(sys.argv)
    uiHandler = MainWindowController()
    app.exec_()


if __name__ == "__main__":
    init_gui()
