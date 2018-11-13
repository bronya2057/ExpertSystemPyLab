from PyQt5.QtCore import QModelIndex, QVariant, Qt, QAbstractTableModel

from GUI.Models.Helpers.SemanticData import SemanticData, SemanticDataType, SemanticNodeType

OUT_TYPE = SemanticDataType.OUT

class SemanticOutputTableModel(QAbstractTableModel):
    def __init__(self, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)

    def data(self, index, role=None):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if index.column() == 0:
                interaction = SemanticData.get_semantic_type_interaction_at(index.row(), OUT_TYPE)
                return QVariant(interaction)
            elif index.column() == 1:
                semantic_object = SemanticData.get_semantic_type_object_at(index.row(), OUT_TYPE)
                return QVariant(semantic_object)
        else:
            return QVariant()

    def rowCount(self, parent=QModelIndex()):
        return SemanticData.get_semantic_type_len_at_selected(OUT_TYPE)

    def columnCount(self, *args, **kwargs):
        return 2

    def headerData(self, section, orientation, role=None):
        if not (role == Qt.DisplayRole):
            return QVariant()
        else:
            if orientation == Qt.Horizontal:
                if section == 0:
                    return "Object"
                elif section == 1:
                    return "Interaction"

    def flags(self, index):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def insertRow(self, row, parent=None, *args, **kwargs):
        self.beginInsertRows(QModelIndex(), row, row)
        self.endInsertRows()

    def removeRow(self, row, parent=None, *args, **kwargs):
        self.beginRemoveRows(QModelIndex(), row, row)

        self.endRemoveRows()

    def insertRows(self, row, count, parent=None, *args, **kwargs):
        print("insert rows" + str(row) + str(count))
        self.beginInsertRows(QModelIndex(), row, count)
        self.endInsertRows()

    def removeRows(self, row, count, parent=None, *args, **kwargs):
        self.beginRemoveRows(QModelIndex(), row, count)
        self.endRemoveRows()

    def setData(self, index, value, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.EditRole and value:
            node_type = SemanticNodeType.object
            if index.column() == 0:
                node_type = SemanticNodeType.interaction
            elif index.column() == 1:
                node_type = SemanticNodeType.object

            SemanticData.update_semantic_type_at(index.row(), OUT_TYPE, node_type, value)
            self.dataChanged.emit(index, index, [])
            return True
        return False

    def clear_all_inputs(self):
        # remove rows workaround
        a = 0
        if -1 != SemanticData.get_semantic_type_len_at_selected(OUT_TYPE) - 1:
            a = SemanticData.get_semantic_type_len_at_selected(OUT_TYPE) - 1
        # SELECTED INDEX IS MODIFIED BY inPUT
        self.removeRows(0, a)

    def request_output_for_selected(self):
        self.insertRows(0, SemanticData.get_semantic_type_len_at_selected(OUT_TYPE) - 1)
        self.dataChanged.emit(QModelIndex(), QModelIndex(), [])


    def remove_output_at(self, index):
        if index > -1:
            self.removeRow(index)
            SemanticData.remove_selected_semantic_type_at(index, OUT_TYPE)

    def insert_new_input(self):
        self.insertRow(SemanticData.get_semantic_type_len_at_selected(OUT_TYPE))
        SemanticData.add_new_semantic_type(OUT_TYPE)