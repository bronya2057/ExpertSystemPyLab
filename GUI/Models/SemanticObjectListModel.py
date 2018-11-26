from PyQt5.QtCore import QAbstractListModel, QModelIndex, QVariant, Qt

from GUI.Models.Helpers.SemanticData import SemanticData
from GUI.Models.Helpers.ESTheme import SemanticNode


class SemanticObjectListModel(QAbstractListModel):
    NEW_OBJECT_STR = "New semantic object"

    def __init__(self, parent=None, *args):
        """ datain: a list where each item is a row
        """
        QAbstractListModel.__init__(self, parent, *args)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            new_data = SemanticData.get_name_at_index(index.row())
            return new_data
        return QVariant()

    def rowCount(self, parent=QModelIndex()):
        return SemanticData.get_len()

    def insertRows(self, row, count, parent=None, *args, **kwargs):
        print("insert rows" + str(row) + str(count))
        self.beginInsertRows(QModelIndex(), row, count)
        self.endInsertRows()

    def removeRows(self, row, count, parent=None, *args, **kwargs):
        self.beginRemoveRows(QModelIndex(), row, count)
        self.endRemoveRows()

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def insertRow(self, row, parent=None, *args, **kwargs):
        self.beginInsertRows(QModelIndex(), row, 1)
        self.endInsertRows()

    def removeRow(self, index, parent=None, *args, **kwargs):
        self.beginRemoveRows(QModelIndex(), index, index)
        SemanticData.remove_semantic_node_at(index)
        self.endRemoveRows()

    def setData(self, index, value, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.EditRole and value and not (value in SemanticData.get_names_list()):
            SemanticData.update_object_name(index.row(), value)
            self.dataChanged.emit(index, index, [])
            return True
        return False

    def add_semantic_object(self):
        if not (self.NEW_OBJECT_STR in SemanticData.get_names_list()):
            new_node = SemanticNode(self.NEW_OBJECT_STR, [], [], [], [])
            SemanticData.add_semantic_node(new_node)
            self.insertRow(SemanticData.get_len())

    def remove_semantic_object(self, selected_index):
        if -1 < selected_index:
            self.removeRow(selected_index)

    def set_selected_object(self, selected_object_index):
        SemanticData.selected_semantic_object_index = selected_object_index

        # rules_names_list = CommonSerializedData.get_rules_names()
        # if not (self.NEW_RULE_STR in rules_names_list):
        #     new_row_index = len(rules_names_list)
        #
        #     rules_list = CommonSerializedData.get_rules_list()
        #     self.insertRow(new_row_index)
        #     rules_names_list.append(self.NEW_RULE_STR)
        #     CommonSerializedData.add_rule()
        #     print(rules_names_list)
        #     print(rules_list)

    def add_net_from_file(self, semantic_net_struct):
        for index, node in enumerate(semantic_net_struct):
            self.insertRow(index)
            SemanticData.add_semantic_node(node)

    def clear_all_objects(self):
        obj_count = SemanticData.get_len()

        if obj_count > 0:
            for index in range(obj_count):
                self.remove_semantic_object(0)


