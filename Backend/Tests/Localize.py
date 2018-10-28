from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QDialogButtonBox, QApplication, QPushButton


class MyWindow(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.hbox = QHBoxLayout(self)
        self.myButtons = QPushButton()
        self.myButtons.setText(QPushButton.tr(self.myButtons, "Hello world!"))
        self.hbox.addWidget(self.myButtons)
        # button = self.myButtons.addButton(QDialogButtonBox.Open)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    translator = QTranslator()
    print(translator.load("translation"))
    app.installTranslator(translator)
    ui = MyWindow()
    ui.show()
    sys.exit(app.exec_())