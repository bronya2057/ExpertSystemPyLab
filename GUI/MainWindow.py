from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import QDir, QIODevice, QFile
from PyQt5.QtWidgets import QDialog, QListView, QFileSystemModel, QTreeView
from PyQt5 import QtCore


# slot example
from GUI.TreeModel import ExpertTreeModel


def on_esdouble_spin_box_changed(value):
    print(value)
    print("Activate Double spinbox slot")


def on_checkbox_checked(value):
    print(value)
    print("Activate Double spinbox slot")
    dialog = MyExtraDialog.get_date_time()
    # date = dialog.dateTime()


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
        uic.loadUi('TreeView.ui', self)

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def get_date_time(parent=None):
        dialog = MyExtraDialog(parent)
        result = dialog.exec_()
        return result == QDialog.Accepted

    def load_example_file_system(self):
        treeView = self.findChild(QTreeView, "treeView")
        model = QFileSystemModel()

        model.setRootPath(QDir.currentPath())
        treeView.setModel(model)

    def load_example_custom_model(self):
        f = QFile(QDir.currentPath() + "/default.txt")
        f.open(QIODevice.ReadOnly)
        model = ExpertTreeModel(f.readAll())
        f.close()

        treeView = self.findChild(QTreeView, "treeView")
        treeView.setModel(model)
        self.treeView.setColumnWidth(0, 300)


def init_gui():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


def init_treeView():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyExtraDialog()
    #window.load_example_file_system()
    window.load_example_custom_model()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # init_gui() # Main window then TreeView
    init_treeView()  # only treeView
