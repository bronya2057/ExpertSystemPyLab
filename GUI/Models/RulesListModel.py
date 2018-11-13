from PyQt5.QtCore import QAbstractListModel, QModelIndex, QVariant, Qt

from GUI.Models.Helpers.ColumnButtonDelegate import ColumnButtonDelegate
from GUI.Models.Helpers.CommonSerializedData import CommonSerializedData


class RulesListModel(QAbstractListModel):
    NEW_RULE_STR = "New rule"

    def __init__(self, parent=None, *args):
        """ datain: a list where each item is a row
        """
        QAbstractListModel.__init__(self, parent, *args)

    def data(self, index, role=None):
        # if role == Qt.DisplayRole:
        #     print("Change Data")
        #     answers_list_at_selected_question = CommonSerializedData.get_answers_list_at_selected_index()
        #     print(answers_list_at_selected_question)
        #     row = index.row()
        #     return QVariant(answers_list_at_selected_question[row])
        # else:
        if role == Qt.DisplayRole or role == Qt.EditRole:
            data = CommonSerializedData.rules_name[index.row()]
            print(CommonSerializedData.rules_name)
            print(CommonSerializedData.rules_list)
            print(CommonSerializedData.rules_output)
            # print(CommonSerializedData.rules_output)

            return QVariant(data)

    def rowCount(self, parent=QModelIndex()):
        return len(CommonSerializedData.rules_name)
        # if CommonSerializedData.get_question_selection_validity():
        #     answers_list_at_selected_question = CommonSerializedData.get_answers_list_at_selected_index()
        #     return len(answers_list_at_selected_question)
        # else:
        #     return 0

    def insertRows(self, row, count, parent=None, *args, **kwargs):
        print("insert rows" + str(row) + str(count))
        self.beginInsertRows(QModelIndex(), row, count)

        self.endInsertRows()
        pass
        # self.beginInsertRows(QModelIndex(), row, row + count)
        #
        # self.endRemoveRows()

    def removeRows(self, row, count, parent=None, *args, **kwargs):
        self.beginRemoveRows(QModelIndex(), row, count)

        self.endRemoveRows()

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

        # return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def insertRow(self, row, parent=None, *args, **kwargs):
        self.beginInsertRows(QModelIndex(), row, 1)
        self.endInsertRows()

    def removeRow(self, index, parent=None, *args, **kwargs):
        self.beginRemoveRows(QModelIndex(), index, index)
        CommonSerializedData.remove_rule_at(index)
        self.endRemoveRows()

    def setData(self, index, value, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.EditRole and value:
            CommonSerializedData.update_rule_name(index.row(), value)

            self.dataChanged.emit(index, index, [])
            return True
        return False

    def set_all_combo_boxes_for_selected_rule(self, index):
        rules_list_at_index = CommonSerializedData.get_rules_list_at_index(index)
        for index, rule in enumerate(rules_list_at_index):
            print(index)
            print(rule)
            ColumnButtonDelegate.set_combo_item_at_index(index, rule)

    def add_rule(self):
        rules_names_list = CommonSerializedData.get_rules_names()
        if not (self.NEW_RULE_STR in rules_names_list):
            new_row_index = len(rules_names_list)

            rules_list = CommonSerializedData.get_rules_list()
            self.insertRow(new_row_index)
            rules_names_list.append(self.NEW_RULE_STR)
            CommonSerializedData.add_rule()
            print(rules_names_list)
            print(rules_list)

    def remove_rule(self, index):
        if index > -1:
            self.removeRow(index)

    def update_output_for_selected_rule(self, index, output):
        rules_outputs = CommonSerializedData.get_rules_outputs()
        if -1 < index < len (rules_outputs):
            rules_outputs[index] = output
            print(rules_outputs)

    def get_output_for_selected_rule(self, index):
        return CommonSerializedData.get_output_for_selected_rule(index)

    def update_rule_at(self, index, new_rule_data):
        CommonSerializedData.set_rule_data_at(index, new_rule_data)
        # self.dataChanged.emit(self.index(index, 0), self.index(index, 0), [])

    def remove_all_rules(self):
        for rule_index in range(len(CommonSerializedData.get_rules_list())):
            self.remove_rule(0)

    def add_rules_from_file(self, rules_struct):
        for index, rule_name in enumerate(rules_struct.rules_names):
            print(rules_struct.rules_names[index])
            print(rules_struct.rules_list[index])
            print(rules_struct.rules_output[index])
            names = CommonSerializedData.get_rules_names()
            outputs = CommonSerializedData.get_rules_outputs()
            rules = CommonSerializedData.get_rules_list()

            if not (rule_name in names):
                self.insertRow(len(names))
                CommonSerializedData.add_rule()
                names.append("")

                names[len(names) - 1] = rules_struct.rules_names[index]
                outputs[len(outputs) - 1] = rules_struct.rules_output[index]
                rule_as_list = rules_struct.rules_list[index]
                rule_as_list = rule_as_list.replace(", ", ",")
                rule_as_list = rule_as_list.split(',')
                print()
                rules[len(rules) - 1] = rule_as_list

        print (1)
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

