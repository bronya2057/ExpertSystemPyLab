from pyknow import *
import re

RULE_NO = "0"


def create_rule(current_theme_questions, current_rule, output):
    def goal(self):
        print(output)

    current_rule = current_rule.replace(", ", ",")
    rules_list = current_rule.split(",")
    facts = Fact()

    for index, questions in enumerate(current_theme_questions):
        facts[questions] = rules_list[index]

    return Rule(facts)(goal)


class ExpertEngine(KnowledgeEngine):
    def __init__(self, current_theme_questions, current_theme_rules):
        for rule, output in current_theme_rules.items():
            self.add_method(current_theme_questions, rule, output)
        super().__init__()

    def add_method(self, current_theme_questions, rule, output):
        # self.name = set_goal()
        new_rule = create_rule(current_theme_questions, rule, output)
        setattr(self, output + RULE_NO, new_rule)  # insert fact parameters HERE!

    # @Rule(Fact(myFact="Brown", myFact2="Yes"))
    # def pr(self):
    #     print("WOR")


# if __name__ == '__main__':
    # engine = ExpertEngine()
    # engine.reset()

    # ask_eye = input("What is your eyes color?")
    # ask_hands = input("Did you Wash them with your hands? ")

    # engine.declare(Fact(myFact="Brown", myFact2="Yes"))

    # engine.run()

    # engine.facts
    # graph = engine.matcher.show_network()
    # graph.view()
