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
        self.rules_struct = RulesContainer()


class RulesContainer:
    def __init__(self):
        self.rules_names = []
        self.rules_list = []
        self.rules_output = []


class SemanticNode:
    def __init__(self, name="DummyName", in_objects=[], in_interactions=[], out_objects=[], out_interactions=[]):
        self.name = name
        self.in_objects = in_objects
        self.in_interactions = in_interactions
        self.out_objects = out_objects
        self.out_interactions = out_interactions