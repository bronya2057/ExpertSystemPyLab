from pyknow import *

class Maximum(KnowledgeEngine):
    @Rule(NOT(Fact(max=W())))
    def init(self):
        self.declare(Fact(max=0))

    @Rule(Fact(val=MATCH.val),
          AS.m << Fact(max=MATCH.max),
          TEST(lambda max, val: val > max))
    def compute_max(self, m, val):
        self.modify(m, max=val)

    @Rule(AS.v << Fact(val=MATCH.val),
          Fact(max=MATCH.max),
          TEST(lambda max, val: val <= max))
    def remove_val(self, v):
        self.retract(v)

    @Rule(AS.v << Fact(max=W()),
          NOT(Fact(val=W())))
    def print_max(self, v):
        print("Max:", v['max'])

if __name__ == '__main__':
    m = Maximum()
    m.reset()
    m.declare(*[Fact(val=x) for x in (12, 33, 42, 99, 55, 11, 75)])
    # watch(RULES, FACTS, ACTIVATIONS)
    m.run()