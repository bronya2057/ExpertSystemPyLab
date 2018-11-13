from collections import OrderedDict
from json import JSONDecodeError

from GUI.Models.Helpers.ESTheme import ESThemeSimple
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
                "RulesNames": rules_names}}

    return data

def de_serialize_to_internal_data(file_path):
    import json

    theme = -1

    with open(file_path) as f:
        try:
            data = json.load(f)

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

if __name__ == "__main__":
    de_serialize_to_internal_data("c:/Users/ABrodskyi/Dropbox/ProgrammingMaterial/Python/ExpertSystem/GUI/data_file.json")