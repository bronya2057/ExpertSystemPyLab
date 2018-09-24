from pyknow import *


class Factorial(Fact):
    #  TEST SECTION OF VALUES
    n = Field(lambda n: isinstance(n, int) and n >= 0, mandatory=True)  # if n < 0 then the program will not start!!!
    result = Field(int, mandatory=True)


class ComputeFactorial(KnowledgeEngine):
    @DefFacts()
    def first(self):
        yield Factorial(n=0, result=1)  # RUNS AT START

    @Rule(
        AS.f << Factorial(  # AS.f     f is just a name for the FactStructure
            n=MATCH.n,  # MATCH.n  when yielded a fact MATCH.n equal 0
            result=MATCH.r))  # Factorial(n=Match.n, result=Match.r) result is FACT, and Factorial is compound fact
    def factorial(self, f, n, r):
        print('f' + str(f))  # current fact
        print('n' + str(n))  # Fact value of key n
        print('r' + str(r))  # Fact value of key r
        self.declare(
            Factorial(
                n=n + 1,
                result=(n + 1) * r))  # add Fact where n = n + 1 and result = (n+1)*r to memory
        self.retract(f)  # Delete fact <n> not necessary actually


if __name__ == '__main__':
    cf = ComputeFactorial()
    cf.reset()
    cf.run(5)  # limit the number with run(n)
    print(cf.facts)
