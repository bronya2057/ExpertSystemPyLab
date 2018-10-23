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
    es_answers_list = [["1000-2000", "3000-4000"], ["Veg", "NotVeg", "Never Thought"], ["Yes, No, Sometimes"]]

    rules_list = [["1000-2000", "Veg", "Yes"], ["3000-4000", "NotVeg", "No"], ["1000-2000", "NotVeg", "Sometimes"], ["3000-4000", "Veg", "Yes"]]
    rules_output = ["Not so fat", "Fat", "You are not fat at all", "Very fat"]

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
            # current_question_answers = list(CommonSerializedData.es_theme.questions.values())
            # current_question_answers.append(answer)

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
        #     all_answers_list = list(CommonSerializedData.es_theme.questions.values())
        #     if CommonSerializedData.selected_question_index < len(all_answers_list):
        #         res = all_answers_list[CommonSerializedData.selected_question_index]


    @staticmethod
    def get_answers_list_at_index(index):
        if index < len(CommonSerializedData.es_answers_list):
            return CommonSerializedData.es_answers_list[index]
        else:
            return []




