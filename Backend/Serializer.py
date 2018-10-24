from collections import OrderedDict

from GUI.Models.CommonSerializedData import CommonSerializedData

es_theme_name = "Some Name"
es_questions_list = ["How many calories", "Veg?", "Are you working out?"]
es_answers_list = [["1000-2000", "3000-4000"], ["Veg", "NotVeg", "Never Thought"], ["Yes", "No", "Sometimes"]]

rules_name = []
rules_list = []
rules_output = []

def get_json_ready_data():
    name = CommonSerializedData.es_theme_name
    questions = CommonSerializedData.es_questions_list
    answers = CommonSerializedData.es_answers_list
    rules_list = CommonSerializedData.rules_list
    rules_output = CommonSerializedData.rules_output

    rules_in_order = OrderedDict()

    for index, unused in enumerate(rules_list):
        rule_key = ", ".join(rules_list[index])
        rules_in_order[rule_key] = rules_output[index]

    print(rules_in_order)

    data = {name: {"Questions": questions,
                "Variables": answers,
                "Rules": rules_in_order}}

    return data



