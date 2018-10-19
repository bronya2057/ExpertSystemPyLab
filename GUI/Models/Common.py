class ESTheme:
    def __init__(self, name="DummyName", questions_dictionary={}, rules_dictionary={}):
        self.name = name
        self.questions = questions_dictionary
        self.rules = rules_dictionary