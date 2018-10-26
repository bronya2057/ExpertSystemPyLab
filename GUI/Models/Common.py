class ESTheme:
    def __init__(self, name="DummyName", questions_dictionary={}, rules_dictionary={}):
        self.name = name
        self.questions = questions_dictionary
        self.rules = rules_dictionary


class ESThemeSimple:
    def __init__(self, name="DummyName"):
        self.theme_name = name
        self.questions_list = []
        self.answers_list = []
        self.rules_names = []
        self.rules_list = []
        self.rules_output = []
