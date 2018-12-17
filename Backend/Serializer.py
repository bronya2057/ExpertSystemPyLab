from collections import OrderedDict
from json import JSONDecodeError

from GUI import Common
from GUI.Models.Helpers.SemanticData import SemanticData
from GUI.Models.Helpers.ESTheme import ESThemeSimple, SemanticNode
from GUI.Models.Helpers.CommonSerializedData import CommonSerializedData

def get_json_ready_data():
    name = CommonSerializedData.es_theme_name
    questions = CommonSerializedData.es_questions_list
    answers = CommonSerializedData.es_answers_list
    rules_list = CommonSerializedData.rules_list
    rules_output = CommonSerializedData.rules_output
    rules_names = CommonSerializedData.rules_name.copy()

    rules_in_order = OrderedDict()

    for index, unused in enumerate(rules_list):
        rule_key = ", ".join(rules_list[index])
        if rule_key in rules_in_order:
            del rules_names[index]
            continue
            # del rules_output[index]
            # del rules_list[index]
        rules_in_order[rule_key] = rules_output[index]
        # remove rule_name if index exists

    print(rules_in_order)

    data = {name: {"Questions": questions,
                   "Variables": answers,
                   "Rules": rules_in_order,
                   "RulesNames": rules_names}, Common.TYPE_TOKEN: Common.production_str_token}

    return data

def get_json_ready_semantic_data():
    all_nodes = SemanticData.semantic_nodes

    result = []
    node_dict = {}
    data ={}

    for node in all_nodes:
        name = node.name
        in_objects = node.in_objects
        in_interactions = node.in_interactions
        out_objects = node.out_objects
        out_interactions = node.out_interactions

        data = {name: {"in_obj": in_objects,
                       "in_interaction": in_interactions,
                       "out_interactions": out_objects,
                       "out_obj": out_interactions}}
        node_dict.update(data)

    node_dict[Common.TYPE_TOKEN] = Common.semantic_str_token

    return node_dict


def de_serialize_to_internal_data(file_path):
    import json

    theme = -1

    with open(file_path) as f:
        try:
            data = json.load(f)
            lst = list(data.keys())
            if "TYPE" in list(data.keys()):
                if data[Common.TYPE_TOKEN] == Common.production_str_token:
                    del data[Common.TYPE_TOKEN]
                    theme = ESThemeSimple("")

                    themes = data.keys()
                    if len(themes) > 0:
                        FIRST_THEME_TO_SERIALIZE = 0
                        all_themes = list(themes)

                        print(all_themes[FIRST_THEME_TO_SERIALIZE])
                        theme.theme_name = all_themes[FIRST_THEME_TO_SERIALIZE]
                        value_struct = list(data.values())[0]

                        theme.questions_list = value_struct["Questions"]
                        theme.answers_list = value_struct["Variables"]

                        theme.rules_struct.rules_list = list(value_struct["Rules"].keys())
                        theme.rules_struct.rules_output = list(value_struct["Rules"].values())
                        theme.rules_struct.rules_names = list(value_struct["RulesNames"])

                        print(theme)

                    if len(theme.questions_list) == len(theme.answers_list) and \
                            len(theme.rules_struct.rules_names) == len(theme.rules_struct.rules_output) == len(
                        theme.rules_struct.rules_list):
                        for variable_rules in theme.rules_struct.rules_list:
                            variable_rules = variable_rules.replace(", ", ",")
                            variable_rules = variable_rules.split(',')
                            if not len(variable_rules) == len(theme.answers_list):
                                theme = -1
                                break
                    else:
                        theme = -1

        except JSONDecodeError:
            print("JSON file contains malicious content")

    return theme

def de_serialize_semantic_to_internal_data(file_path):
    import json

    semantic_net = []

    with open(file_path) as f:
        try:
            data = json.load(f)
            lst = list(data.keys())
            if "TYPE" in list(data.keys()):
                if data[Common.TYPE_TOKEN] == Common.semantic_str_token:
                    del data[Common.TYPE_TOKEN]
                    for index, data_value in enumerate(data):
                        obj = list(data.keys())[index]
                        values = list(data.values())[index]


                        in_obj = values["in_obj"]
                        in_interaction = values["in_interaction"]
                        out_interactions = values["out_interactions"]
                        out_obj = values["out_obj"]

                        if (len(in_obj) == len(in_interaction) and len(out_interactions) == len(out_obj)):
                            semantic_net.append(SemanticNode(obj, in_obj, in_interaction, out_interactions, out_obj))
        except JSONDecodeError:
            print("JSON file contains malicious content")

    return semantic_net

if __name__ == "__main__":
    de_serialize_semantic_to_internal_data("C:/Users/Alexander/Dropbox/ProgrammingMaterial/Python/ExpertSystem/ESKnowledgeBase/Semantic/data_file.json")
    de_serialize_semantic_to_internal_data("C:/Users/Alexander/Dropbox/ProgrammingMaterial/Python/ExpertSystem/ESKnowledgeBase/DUMMY NET.json")