from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QListView


# slot example
def on_esdouble_spin_box_changed(value):
    print(value)
    print("Activate Double spinbox slot")


def on_checkbox_checked(value):
    print(value)
    print("Activate Double spinbox slot")
    ok = MyExtraDialog.get_date_time()


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):  # ctor
        super(MyWindow, self).__init__()  # parent ctor
        uic.loadUi('Test.ui', self)

        # double spin box slot for sending value to function func
        self.doubleSBEyeSeparation.valueChanged[float].connect(on_esdouble_spin_box_changed)
        # check box slot clicked
        self.checkBoxStereoscopyOnOff.clicked[bool].connect(on_checkbox_checked)

        # GET WIDGET FROM existing UI
        widget = self.findChild(QListView, "listViewContext")
        # insert model and one item to list view
        model = QtGui.QStandardItemModel()
        widget.setModel(model)
        item = QtGui.QStandardItem('one')
        model.appendRow(item)


class MyExtraDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MyExtraDialog, self).__init__(parent)
        uic.loadUi('Dialog.ui', self)

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def get_date_time(parent=None):
        dialog = MyExtraDialog(parent)
        result = dialog.exec_()
        return result == QDialog.Accepted


def init_gui():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    init_gui()
