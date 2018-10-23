from GUI.Models.Common import ESTheme

class CommonSerializedData:
    INVALID_INDEX = -1
    # es_theme = ESTheme("", {}, {})
    es_theme = ESTheme("SOME NAME",
                         {"How many calories": ["1000-2000", "3000-4000"],
                          "Veg?": ["Veg", "NotVeg", "Never thought about it"]},
                         {"1000-2000": "Oh My"})
    selected_question_index = INVALID_INDEX

    @staticmethod
    def add_theme_name(theme_name):
        CommonSerializedData.es_theme.name = theme_name

    @staticmethod
    def update_question(old_key_index, new_key):
        old_key = list(CommonSerializedData.es_theme.questions.keys())[old_key_index]
        CommonSerializedData.es_theme.questions[new_key] = CommonSerializedData.es_theme.questions[old_key]
        del CommonSerializedData.es_theme.questions[old_key]

    @staticmethod
    def update_answer(index, value):
        answers_list = CommonSerializedData.get_answers_list_at_selected_index()
        answers_list[index] = value

    @staticmethod
    def add_variable_for_selected_question(answer):
        if not CommonSerializedData.selected_question_index == CommonSerializedData.INVALID_INDEX:
            current_question_answers = list(CommonSerializedData.es_theme.questions.values())
            current_question_answers.append(answer)

    @staticmethod
    def get_question_selection_validity():
        return not (CommonSerializedData.selected_question_index == CommonSerializedData.INVALID_INDEX)

    @staticmethod
    def set_selected_question_index(index):
        CommonSerializedData.selected_question_index = index
        print("Selected" + str(CommonSerializedData.selected_question_index))

    @staticmethod
    def get_answers_list_at_selected_index():
        res = []

        if CommonSerializedData.get_question_selection_validity():
            all_answers_list = list(CommonSerializedData.es_theme.questions.values())
            if CommonSerializedData.selected_question_index < len(all_answers_list):
                res = all_answers_list[CommonSerializedData.selected_question_index]

        return res

    @staticmethod
    def get_answers_list_at_index(index):
            all_answers_list = list(CommonSerializedData.es_theme.questions.values())
            if index < len(all_answers_list):
                return all_answers_list[index]
            else:
                return []




