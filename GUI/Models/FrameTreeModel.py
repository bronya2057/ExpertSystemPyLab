from json import JSONDecodeError
import json

from PyQt5 import QtCore
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtWidgets import QApplication, QTreeView, QMessageBox
import inspect

from GUI.Models.FrameItem import FrameItem


class FrameTreeModel(QtCore.QAbstractItemModel):
    def __init__(self, parent=None):
        super(FrameTreeModel, self).__init__(parent)
        self.rootItem = FrameItem("ROOT")
        # self.data = {}
        self.all_items = []
        self.full_path = ""

    def load_frame_file(self, full_path):
        with open(full_path) as f:
            try:
                self.data = json.load(f)
                self.parse_data()
            except JSONDecodeError:
                msg = QMessageBox()
                msg.setText("Serialization failed due to file corruption")
                retval = msg.exec_()
                print("JSON file contains malicious content")

    def parse_data(self):
        all_root_nodes = self.data["ROOT"]
        self.all_items.append(self.rootItem)

        current_node = self.rootItem

        for key in all_root_nodes:
            new_node = FrameItem(key, all_root_nodes[key]["slots"], current_node)
            self.rootItem.appendChild(new_node)
            print()

            # current_node = all_root_nodes[key]
            # node_slots = list(current_node["slots"])
            # for key,val in current_node.items():
            #     FrameItem(key, list(val), key)

            # self.rootItem.appendChild(FrameItem(key, all_root_nodes[key].values(), self.rootItem))
            # pass
        # self.roost_node.add_child()

        # self.root_node = FrameItem(QModelIndex(), "ROOT")

    def getItem(self, index):
        if not index is None:
            if index.isValid():
                item = index.internalPointer()
                if item:
                    return item

        return self.rootItem

    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index, role):
        print("data:")
        if not index.isValid():
            return None

        if role != QtCore.Qt.DisplayRole and role != Qt.EditRole:
            return None

        item = self.getItem(index)
        return item.data(index.column())

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.NoItemFlags

        flags_result = QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        if index.column() == 0:
            flags_result = flags_result | QtCore.Qt.ItemIsEditable
        return flags_result

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.rootItem.header_data_val(section)

        return None

    def index(self, row, column, parent):
        print("index:")
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()
        if not parent.isValid():

            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        childItem = self.getItem(index)
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.childNumber(), 0, parentItem)

    def rowCount(self, parent):
        print("rowCount:")
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem

        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def setData(self, index, value, role=None):
        if index.isValid() and role == Qt.EditRole and value:
            index.internalPointer().set_name(value)
            self.dataChanged.emit(index, index, [])
            return True
        else:
            return False

    def add_child_at(self, index):
        if index.isValid():
            node = index.internalPointer()
            self.insertRow(0, index)
            print()
        pass

    def add_item_at(self, index):
        if index.isValid():
            node = index.internalPointer()
            self.insertRow(index.row() + 1, index.parent())
            print()

    def remove_item_at(self, index):
        self.removeRow(index.row(), index.parent())

    def insertRows(self, position, rows, parent=None, *args, **kwargs):
        parent_item = self.getItem(parent)

        self.beginInsertRows(parent, position, position + rows - 1)
        success = parent_item.insertChildren(position, 1)
        self.endInsertRows()

        return True

    def removeRows(self, position, rows, parent=None, *args, **kwargs):
        parentItem = self.getItem(parent)

        self.beginRemoveRows(parent, position, position + rows - 1)
        success = parentItem.removeChildren(position, rows)
        self.endRemoveRows()

        return success

        # if parent.isValid():
        #     this_item = parent.internalPointer()
        #     this_parent = this_item.parent()
        #     self.beginRemoveRows(parent, position, position + rows - 1)
        #     this_parent.remove_children_at(position)
        #     print("REMOVE CHILDREN:")
        #     self.endRemoveRows()
        #     return True

    def clear_all(self):
        if len(self.rootItem.frame_items) > 0:
            self.removeRows(0, len(self.rootItem.frame_items))
            # self.rootItem.removeChildren(0, len(self.rootItem.frame_items))
            self.all_items = []


def getLineInfo():
    print(inspect.stack()[1][1], ":", inspect.stack()[1][2], ":",
          inspect.stack()[1][3])


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    'c:/Users/ABrodskyi/Dropbox/ProgrammingMaterial/Python/ExpertSystem/ESKnowledgeBase/Frame.json'
    folder = 'C:/Users/Alexander/Dropbox/ProgrammingMaterial/Python/ExpertSystem/ESKnowledgeBase/Frame.json'
    # with open(folder) as f:
    #     data = json.load(f)

    model = FrameTreeModel()
    model.load_frame_file(folder)

    view = QTreeView()
    view.setModel(model)
    view.setWindowTitle("Simple Tree Model")
    view.show()
    sys.exit(app.exec_())
