from PyQt5 import QtWidgets, QtCore

from GUI.DragNDrop.DragNDrop import Ui_DragNDrop


#  CREATE CUSTOM QPUSHBUTTON and override dragEventMethods
class DragDropButton(QtWidgets.QPushButton):  # Subclass QPushButton
    def __init__(self, text, parent):  # ctor initilize QPushButton correctly
        super().__init__(text, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):  # Accept only if MimeData is text
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.setText(event.mimeData().text())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DragNDrop = QtWidgets.QWidget()
    ui = Ui_DragNDrop()
    ui.setupUi(DragNDrop)

    #  HIDE THE PREVIOUS BUTTON
    ui.pbDragNDrop.hide()

    #  ADD CUSTOM WIDGET TO UI
    ui.drop_button = DragDropButton('DropButton', DragNDrop)
    ui.drop_button.setMinimumSize(QtCore.QSize(0, 0))
    ui.horizontalLayout.addWidget(ui.drop_button)

    DragNDrop.show()
    sys.exit(app.exec_())
