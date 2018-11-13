from GUI.Common import INVALID_INDEX
from GUI.Models.Helpers.ESTheme import SemanticNode
from enum import Enum


class SemanticDataType(Enum):
    IN = 1
    OUT = 2


class SemanticNodeType(Enum):
    object = 1
    interaction = 2


class SemanticData:

    node1 = SemanticNode("Candy", ["Lion", "Man", "Caramel"], ["dont like", "eats", "Ingredient of"], ["made of"], ["soup"])
    node2 = SemanticNode("Man", ["Lion", "Flesh"], ["like", "Ingredient of"], ["made of", "eats"], ["soup", "Lion"])

    semantic_nodes = [node1, node2]
    selected_semantic_object_index = INVALID_INDEX

    # OBJECTS
    @staticmethod
    def get_index_validity(index):
        return INVALID_INDEX < index < len(SemanticData.semantic_nodes)

    @staticmethod
    def add_semantic_node(node):
        SemanticData.semantic_nodes.append(node)

    @staticmethod
    def remove_semantic_node_at(index):
        if SemanticData.get_index_validity(index):
            del SemanticData.semantic_nodes[index]
            SemanticData.selected_semantic_object_index = INVALID_INDEX

    @staticmethod
    def get_node_at_index(index):
        if SemanticData.get_index_validity(index):
            return SemanticData.semantic_nodes[index]
        else:
            return []

    @staticmethod
    def get_len():
        return len(SemanticData.semantic_nodes)

    @staticmethod
    def get_name_at_index(index):
        if SemanticData.get_index_validity(index):
            return SemanticData.semantic_nodes[index].name

    @staticmethod
    def get_names_list():
        names_list = []

        for index, node in enumerate(SemanticData.semantic_nodes):
            names_list.append(node.name)

        return names_list

    @staticmethod
    def update_object_name(index, name):
        if SemanticData.get_index_validity(index):
            SemanticData.semantic_nodes[index].name = name

    # INPUTS and OUTPUTS
    @staticmethod
    def get_semantic_type_len_at_selected(data_type):
        result = 0
        if SemanticData.get_index_validity(SemanticData.selected_semantic_object_index):
            current_semantic_object = SemanticData.semantic_nodes[SemanticData.selected_semantic_object_index]

            if data_type == SemanticDataType.IN:
                result = len(current_semantic_object.in_objects)
            elif data_type == SemanticDataType.OUT:
                result = len(current_semantic_object.out_objects)
        return result

    @staticmethod
    def get_semantic_type_object_at(index, data_type):
        result = ""
        node_at_current_index = SemanticData.get_node_at_index(SemanticData.selected_semantic_object_index)

        if node_at_current_index:
            if data_type == SemanticDataType.IN:
                if index < len(node_at_current_index.in_objects):
                    result = node_at_current_index.in_objects[index]
            elif data_type == SemanticDataType.OUT:
                if index < len(node_at_current_index.out_objects):
                    result = node_at_current_index.out_objects[index]

        return result

    @staticmethod
    def get_semantic_type_interaction_at(index, data_type):
        result = ""

        node_at_current_index = SemanticData.get_node_at_index(SemanticData.selected_semantic_object_index)
        if node_at_current_index:
            if data_type == SemanticDataType.IN:
                if  index < len(node_at_current_index.in_interactions):
                    result = node_at_current_index.in_interactions[index]
            elif data_type == SemanticDataType.OUT:
                if index < len(node_at_current_index.out_interactions):
                    result = node_at_current_index.out_interactions[index]

        return result

    @staticmethod
    def remove_selected_semantic_type_at(index, data_type):
        if SemanticData.get_index_validity(SemanticData.selected_semantic_object_index):
            current_semantic_object = SemanticData.semantic_nodes[SemanticData.selected_semantic_object_index]
            if data_type == SemanticDataType.IN:
                del current_semantic_object.in_objects[index]
                del current_semantic_object.in_interactions[index]
            elif data_type == SemanticDataType.OUT:
                del current_semantic_object.out_objects[index]
                del current_semantic_object.out_interactions[index]

    @staticmethod
    def update_semantic_type_at(index, data_type, node_type, new_value):
        if SemanticData.get_index_validity(SemanticData.selected_semantic_object_index):
            current_semantic_object = SemanticData.semantic_nodes[SemanticData.selected_semantic_object_index]
            if data_type == SemanticDataType.IN:
                if node_type == SemanticNodeType.object:
                    current_semantic_object.in_objects[index] = new_value
                elif node_type == SemanticNodeType.interaction:
                    current_semantic_object.in_interactions[index] = new_value
            elif data_type == SemanticDataType.OUT:
                if node_type == SemanticNodeType.object:
                    current_semantic_object.out_objects[index] = new_value
                elif node_type == SemanticNodeType.interaction:
                    current_semantic_object.out_interactions[index] = new_value

    @staticmethod
    def add_new_semantic_type(data_type):
        if SemanticData.get_index_validity(SemanticData.selected_semantic_object_index):
            current_semantic_object = SemanticData.semantic_nodes[SemanticData.selected_semantic_object_index]
            if data_type == SemanticDataType.IN:
                current_semantic_object.in_objects.append("My new")
                current_semantic_object.in_interactions.append("My new")
            elif data_type == SemanticDataType.OUT:
                current_semantic_object.out_objects.append("My new")
                current_semantic_object.out_interactions.append("My new")