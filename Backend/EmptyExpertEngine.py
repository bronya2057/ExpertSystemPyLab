from pyknow import *


def set_goal():  # ADDING RULES!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def goal(self):
        print("GOAL REACHED")

    factTest = Fact(myFact="Brown")
    factTest["myFact2"] = "Yes"
    return Rule(factTest)(goal)


class ExpertEngine(KnowledgeEngine):
    def __init__(self, name):
        #self.rule2 = set_goal()
        self.add_method(name)
        super().__init__()

    def add_method(self, name):
        # self.name = set_goal()
        setattr(self, name, set_goal())# insert fact parameters HERE!
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
