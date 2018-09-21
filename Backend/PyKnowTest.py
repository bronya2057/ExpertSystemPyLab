from pyknow import *


@DefFacts()
def needed_data():
    yield Fact(best_color="red")
    yield Fact(best_body="medium")
    yield Fact(best_sweetness="dry")


class MyFact(Fact):  # subclass Fact
    """The alert level."""
    pass


@Rule(MyFact())  # LHS of RULE
def match_with_every_myfact():
    """This rule will match with every instance of `MyFact`."""
    # This is the RHS
    pass


@Rule(Fact('animal', family='felinae'))
def match_with_cats():
    """
    Match with every `Fact` which:

      * f[0] == 'animal'
      * f['family'] == 'felinae'

    """
    print("Meow!")


@Rule(
    AND(
        OR(MyFact('admin'),
           MyFact('root')),
        NOT(Fact('drop-privileges'))
    )
)
def the_user_has_power():
    """
    The user is a privileged one and we are not dropping privileges.

    """
    enable_superpowers()


class Greetings(KnowledgeEngine):  # KnowledgeEngine
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="greet")  # First action

    @Rule(Fact(action='greet'),  #  IF action=greet and fact about name is not given
          NOT(Fact(name=W())))
    def ask_name(self):
        self.declare(Fact(name=input("What's your name? ")))

    @Rule(Fact(action='greet'),
          NOT(Fact(location=W())))
    def ask_location(self):
        self.declare(Fact(location=input("Where are you? ")))

    @Rule(Fact(action='greet'),
          Fact(name=MATCH.name),
          Fact(location=MATCH.location))
    def greet(self, name, location):
        print("Hi %s! How is the weather in %s?" % (name, location))


if __name__ == '__main__':
    f = Fact('x', 'y', 'z', a=1, b=2)  # FACTS
    print(f[0])
    print(f['b'])

    # subclass
    f1 = MyFact('red')
    print(f1[0])

    pureEngine = KnowledgeEngine()
    pureEngine.reset()
    pureEngine.declare(Fact(score=5))
    print(pureEngine.facts)

    engine = Greetings()
    engine.reset()  # Prepare the engine for the execution.
    print(engine.facts)
    engine.run()  # Run it!
