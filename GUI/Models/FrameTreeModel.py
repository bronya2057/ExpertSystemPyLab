from json import JSONDecodeError
import json

from PyQt5 import QtCore
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtWidgets import QApplication, QTreeView, QMessageBox
import inspect

from GUI import Common
from GUI.Models.FrameItem import FrameItem
from GUI.Models.Helpers.CommonWidgetOp import CommonWidgetOp

FRAME_TOKEN = "Frame"
ROOT_TOKEN = "ROOT"

class FrameTreeModel(QtCore.QAbstractItemModel):
    def __init__(self, parent=None):
        super(FrameTreeModel, self).__init__(parent)
        self.rootItem = FrameItem(ROOT_TOKEN)
        # self.data = {}
        self.all_items = []
        self.full_path = ""

        self.all_graph_frames = []
        self.connected_subgraph_names = []

    def load_frame_file(self, full_path):
        with open(full_path) as f:
            try:
                temp_data = json.load(f)
                result = False
                lst = list(temp_data.keys())
                if "TYPE" in list(temp_data.keys()):
                    if temp_data[Common.TYPE_TOKEN] == Common.frame_str_token:
                        self.data = temp_data
                        self.parse_data()
                        result = True
                if not result:
                    CommonWidgetOp.prompt_error("Not a Frame file", "File extension error")

            except JSONDecodeError:
                CommonWidgetOp.prompt_error("Serialization failed due to file corruption", "JSON serialization fail")
                print("JSON file contains malicious content")

    def parse_data(self):
        all_root_nodes = self.data[ROOT_TOKEN]
        self.all_items.append(self.rootItem)

        current_node = self.rootItem

        for key in all_root_nodes:
            new_node = FrameItem(key, all_root_nodes[key]["slots"], current_node)
            self.rootItem.appendChild(new_node)

    def init_new_model(self):
        self.all_items.append(self.rootItem)
        self.rootItem.appendChild(FrameItem("NEW FRAME", {}, self.rootItem))  # ADD PARENT FOR TREE


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
        # print("data:")
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
        if index.column() == 1 and index.internalPointer().childCount() == 0 or index.column() == 0:
            flags_result = flags_result | QtCore.Qt.ItemIsEditable
        return flags_result

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.rootItem.header_data_val(section)

        return None

    def index(self, row, column, parent):
        # print("index:")
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()
        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)

        if childItem.childCount() > 0:
            childItem.set_value(FRAME_TOKEN)

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
        # print("rowCount:")
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem

        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def setData(self, index, value, role=None):
        if index.isValid() and role == Qt.EditRole: #and value: Slots could be actually empty
            if index.column() == 0 and value:
                index.internalPointer().set_name(value)
                self.dataChanged.emit(index, index, [])
                return True
            elif index.column() == 1:
                index.internalPointer().set_value(value)
                self.dataChanged.emit(index, index, [])
                return True
        else:
            return False

    def add_child_at(self, index):
        if index.isValid():
            node = index.internalPointer()
            self.insertRow(0, index)
            # print()
        pass

    def add_item_at(self, index):
        if index.isValid():
            node = index.internalPointer()
            self.insertRow(index.row() + 1, index.parent())
            # print()

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

    def clear_all(self):
        if len(self.rootItem.frame_items) > 0:
            self.rootItem = FrameItem(ROOT_TOKEN)
            self.data = {}
            self.all_items = []
            self.dataChanged.emit(QModelIndex(), QModelIndex(), [])
            self.all_items = []

    def get_json_ready_data(self):
        json_data = {}
        json_data[ROOT_TOKEN] = {}
        for frame in self.rootItem.frame_items:
            current_item = frame
            if len(frame.frame_items) > 0:
                json_data[ROOT_TOKEN][frame.name]={"slots":{}}
                current_dict_item = json_data[ROOT_TOKEN][frame.name]
                self.construct_json_frame(current_dict_item, current_item)
            else:
                json_data[ROOT_TOKEN][frame.name] = frame.slot_value()
        json_data[Common.TYPE_TOKEN] = FRAME_TOKEN
        return json_data

    def construct_json_frame(self,current_dict_item, node):
        for child in node.frame_items:
            if (len(child.frame_items) > 0):
                new_dict_item = current_dict_item["slots"][child.name]={"slots":{}}
                self.construct_json_frame(new_dict_item, child)
            else:
                current_dict_item["slots"][child.name] = child.slot_value

    def construct_graph_frame(self, node):
        for frame_item in node.frame_items:
            self.construct_graph_frame(frame_item)

            if len(frame_item.frame_items) > 0:
                slot_val = "Connect"
            else:
                slot_val = frame_item.slot_value
            self.all_graph_frames.append(GraphNodeData(frame_item.name, slot_val, node.name))

def getLineInfo():
    print(inspect.stack()[1][1], ":", inspect.stack()[1][2], ":",
          inspect.stack()[1][3])

class GraphNodeData:
    def __init__(self, name,val,frame_name):
        self.name = name
        self.value = val
        self.frame_name = frame_name

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    folder = 'c:/Users/ABrodskyi/Dropbox/ProgrammingMaterial/Python/ExpertSystem/ESKnowledgeBase/Frame/MainTree.json'
    'C:/Users/Alexander/Dropbox/ProgrammingMaterial/Python/ExpertSystem/ESKnowledgeBase/Frame.json'
    # with open(folder) as f:
    #     data = json.load(f)

    model = FrameTreeModel()
    model.load_frame_file(folder)

    view = QTreeView()
    view.setModel(model)
    view.setWindowTitle("Simple Tree Model")
    root_item = model.rootItem
    root_frames = []
    data = model.get_json_ready_data()
    for node in root_item.frame_items:
        root_frames.append(node.name)
        model.construct_graph_frame(node)

    from graphviz import Digraph

    g = Digraph('G', filename='cluster.gv')
    g.attr(compound='true')
    # NOTE: the subgraph name needs to begin with 'cluster' (all lowercase)
    #       so that Graphviz recognizes it as a special cluster subgraph

    for node in model.all_graph_frames:
        with g.subgraph(name="cluster_" + node.frame_name) as c:
            slot_full_description = ""
            if node.value == "Connect":
                slot_full_description = node.name
            else:
                slot_full_description = node.name + "_" + node.value

            c.node(slot_full_description)
            c.attr(style='filled')
            c.attr(color='lightgrey')
            c.node_attr.update(style='filled', color='white')
            # c.edges([('a0', 'a1'), ('a1', 'a2'), ('a2', 'a3')])
            c.attr(label=node.frame_name)
            # g.edge(slot_full_description, 'b0', lhead="cluster_" + slot_full_description)

            if not node.frame_name == "Connect" and node.frame_name not in model.connected_subgraph_names and node.frame_name not in root_frames:
                g.edge(node.frame_name, slot_full_description, lhead="cluster_" + node.frame_name)
                model.connected_subgraph_names.append(node.frame_name)


    # with g.subgraph(name='cluster_0') as c:
    #     c.node("GEw3")
    #     c.node("GEw23")
    #     c.attr(style='filled')
    #     c.attr(color='lightgrey')
    #     c.node_attr.update(style='filled', color='white')
    #     # c.edges([('a0', 'a1'), ('a1', 'a2'), ('a2', 'a3')])
    #     c.attr(label='process #1')
    #
    # with g.subgraph(name='cluster_0') as c:
    #     c.node("GEw3444")
    #     c.node("GEw23555")
    #     c.attr(style='filled')
    #     c.attr(color='lightgrey')
    #     c.node_attr.update(style='filled', color='white')
    #     # c.edges([('a0', 'a1'), ('a1', 'a2'), ('a2', 'a3')])
    #     c.attr(label='process #1')
    # #
    # with g.subgraph(name='cluster_1') as c:
    #     c.node_attr.update(style='filled')
    #     c.edges([('b0', 'b1'), ('b1', 'b2'), ('b2', 'b3')])
    #     c.attr(label='process #2')
    #     c.attr(color='blue')

    # g.edge('GEw', 'b0', ltail='cluster_0', lhead='cluster_1')  # cluster to cluster
    # g.edge('GEw', 'b0', lhead='cluster_1')  # node to cluster
    # g.edge('start', 'b0')
    # g.edge('a1', 'b3')
    # g.edge('b2', 'a3')
    # g.edge('a3', 'a0')
    # g.edge('a3', 'end')
    # g.edge('b3', 'end')

    # g.node('start', shape='Mdiamond')
    # g.node('end', shape='Msquare')

    #data = model.get_json_ready_data()
    g.view()




    # view.show()
    sys.exit(app.exec_())
