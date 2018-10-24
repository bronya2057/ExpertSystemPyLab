from GUI.Models.Common import ESTheme


class CommonSerializedData:
    INVALID_INDEX = -1
    # es_theme = ESTheme("", {}, {})
    # es_theme = ESTheme("SOME NAME",
    #                      {"How many calories": ["1000-2000", "3000-4000"],
    #                       "Veg?": ["Veg", "NotVeg", "Never thought about it"]},
    #                      {"1000-2000": "Oh My"})

    es_theme_name = "Some Name"
    es_questions_list = ["How many calories", "Veg?", "Are you working out?"]
    es_answers_list = [["1000-2000", "3000-4000"], ["Veg", "NotVeg", "Never Thought"], ["Yes", "No", "Sometimes"]]

    rules_name = []
    rules_list = []
    rules_output = []

    #rules_name = ["DummyRule"]
    #rules_list = [["1000-2000", "Veg", "Yes"]]
    # rules_list = [["1000-2000", "Veg", "Yes"]# , ["3000-4000", "NotVeg", "No"], ["1000-2000", "NotVeg", "Sometimes"], ["3000-4000", "Veg", "Yes"]]
    # rules_output = ["Not so fat", "Fat", "You are not fat at all", "Very fat"]

    selected_answer_index = INVALID_INDEX
    selected_question_index = INVALID_INDEX

    @staticmethod
    def add_theme_name(theme_name):
        CommonSerializedData.es_theme_name = theme_name

    @staticmethod
    def update_question(question_index, question_text):
        CommonSerializedData.es_questions_list[question_index] = question_text
        # old_key = list(CommonSerializedData.es_theme.questions.keys())[old_key_index]
        # CommonSerializedData.es_theme.questions[new_key] = CommonSerializedData.es_theme.questions[old_key]
        # del CommonSerializedData.es_theme.questions[old_key]

    @staticmethod
    def update_answer(index, value):
        answers_list = CommonSerializedData.get_answers_list_at_selected_index()
        if answers_list:
            answers_list[index] = value

    @staticmethod
    def add_variable_for_selected_question(answer):
        if not CommonSerializedData.selected_question_index == CommonSerializedData.INVALID_INDEX:
            CommonSerializedData.es_answers_list[CommonSerializedData.selected_question_index] = answer

    @staticmethod
    def get_question_selection_validity():
        return not (CommonSerializedData.selected_question_index == CommonSerializedData.INVALID_INDEX)

    @staticmethod
    def set_selected_question_index(index):
        CommonSerializedData.selected_question_index = index

    @staticmethod
    def get_answers_list_at_selected_index():
        if CommonSerializedData.get_question_selection_validity():
            return CommonSerializedData.es_answers_list[CommonSerializedData.selected_question_index]
        else:
            return []

    @staticmethod
    def get_answers_list_at_index(index):
        if index < len(CommonSerializedData.es_answers_list):
            return CommonSerializedData.es_answers_list[index]
        else:
            return []

    @staticmethod
    def get_rules_list_at_index(index):
        if index < len(CommonSerializedData.rules_list):
            return CommonSerializedData.rules_list[index]

    @staticmethod
    def get_rules_names():
        return CommonSerializedData.rules_name

    @staticmethod
    def get_rules_list():
        return CommonSerializedData.rules_list

    @staticmethod
    def get_rules_outputs():
        return CommonSerializedData.rules_output

    @staticmethod
    def add_rule():
        rule_list_to_add = []
        for question_index, answer_list in enumerate(CommonSerializedData.es_answers_list):
            if len(answer_list) > 0:
                print("Answer")
                print(answer_list)
                print("question")
                print(question_index)
                rule_list_to_add.append(answer_list[0])

        CommonSerializedData.rules_list.append(rule_list_to_add)
        CommonSerializedData.rules_output.append("")

    @staticmethod
    def update_rule_name(index, value):
        rules_names = CommonSerializedData.rules_name
        if index < len(rules_names):
            rules_names[index] = value

    @staticmethod
    def remove_rule_at(index):
        if index < len(CommonSerializedData.rules_name) and \
                index < len(CommonSerializedData.rules_list) and \
                index < len(CommonSerializedData.rules_output):
            del CommonSerializedData.rules_name[index]
            del CommonSerializedData.rules_list[index]
            del CommonSerializedData.rules_output[index]

    @staticmethod
    def remove_rule_variable_at(selected_index):
        for rule_array in CommonSerializedData.rules_list:
            del rule_array[selected_index]


    @staticmethod
    def get_output_for_selected_rule(index):
        if index < len(CommonSerializedData.rules_output):
            return CommonSerializedData.rules_output[index]

