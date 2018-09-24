from pyknow import *
import schema


class Guest(Fact):
    name = Field(int, mandatory=True)
    sex = Field(schema.Or("m", "f"), mandatory=True)
    hobby = Field(int, mandatory=True)


class LastSeat(Fact):
    pass


class Seating(Fact):
    pass


class Context(Fact):
    pass


class Path(Fact):
    pass


class Chosen(Fact):
    pass


class Count(Fact):
    pass


class Manners(KnowledgeEngine):
    @DefFacts(order=0)
    def declare_guests(self, number_of_seats):
        if number_of_seats == 8:
            yield Guest(name=1, sex="m", hobby=3)
            yield Guest(name=1, sex="m", hobby=2)
            yield Guest(name=2, sex="m", hobby=2)
            yield Guest(name=2, sex="m", hobby=3)
            yield Guest(name=3, sex="m", hobby=1)
            yield Guest(name=3, sex="m", hobby=2)
            yield Guest(name=3, sex="m", hobby=3)
            yield Guest(name=4, sex="f", hobby=3)
            yield Guest(name=4, sex="f", hobby=2)
            yield Guest(name=5, sex="f", hobby=1)
            yield Guest(name=5, sex="f", hobby=2)
            yield Guest(name=5, sex="f", hobby=3)
            yield Guest(name=6, sex="f", hobby=3)
            yield Guest(name=6, sex="f", hobby=1)
            yield Guest(name=6, sex="f", hobby=2)
            yield Guest(name=7, sex="f", hobby=3)
            yield Guest(name=7, sex="f", hobby=2)
            yield Guest(name=8, sex="m", hobby=3)
            yield Guest(name=8, sex="m", hobby=1)
        elif number_of_seats == 16:
            yield Guest(name=1, sex="f", hobby=3)
            yield Guest(name=1, sex="f", hobby=1)
            yield Guest(name=1, sex="f", hobby=2)
            yield Guest(name=2, sex="f", hobby=3)
            yield Guest(name=2, sex="f", hobby=2)
            yield Guest(name=3, sex="m", hobby=1)
            yield Guest(name=3, sex="m", hobby=3)
            yield Guest(name=4, sex="m", hobby=2)
            yield Guest(name=4, sex="m", hobby=1)
            yield Guest(name=5, sex="m", hobby=2)
            yield Guest(name=5, sex="m", hobby=3)
            yield Guest(name=6, sex="m", hobby=2)
            yield Guest(name=6, sex="m", hobby=1)
            yield Guest(name=7, sex="f", hobby=2)
            yield Guest(name=7, sex="f", hobby=1)
            yield Guest(name=7, sex="f", hobby=3)
            yield Guest(name=8, sex="f", hobby=3)
            yield Guest(name=8, sex="f", hobby=2)
            yield Guest(name=9, sex="f", hobby=1)
            yield Guest(name=9, sex="f", hobby=3)
            yield Guest(name=9, sex="f", hobby=2)
            yield Guest(name=10, sex="m", hobby=2)
            yield Guest(name=10, sex="m", hobby=3)
            yield Guest(name=11, sex="m", hobby=3)
            yield Guest(name=11, sex="m", hobby=2)
            yield Guest(name=11, sex="m", hobby=1)
            yield Guest(name=12, sex="m", hobby=3)
            yield Guest(name=12, sex="m", hobby=1)
            yield Guest(name=13, sex="m", hobby=2)
            yield Guest(name=13, sex="m", hobby=3)
            yield Guest(name=13, sex="m", hobby=1)
            yield Guest(name=14, sex="f", hobby=3)
            yield Guest(name=14, sex="f", hobby=1)
            yield Guest(name=15, sex="f", hobby=3)
            yield Guest(name=15, sex="f", hobby=1)
            yield Guest(name=15, sex="f", hobby=2)
            yield Guest(name=16, sex="f", hobby=3)
            yield Guest(name=16, sex="f", hobby=2)
            yield Guest(name=16, sex="f", hobby=1)
        elif number_of_seats == 32:
            yield Guest(name=1, sex="m", hobby=1)
            yield Guest(name=1, sex="m", hobby=3)
            yield Guest(name=2, sex="f", hobby=3)
            yield Guest(name=2, sex="f", hobby=2)
            yield Guest(name=2, sex="f", hobby=1)
            yield Guest(name=3, sex="f", hobby=1)
            yield Guest(name=3, sex="f", hobby=2)
            yield Guest(name=4, sex="f", hobby=3)
            yield Guest(name=4, sex="f", hobby=1)
            yield Guest(name=5, sex="f", hobby=1)
            yield Guest(name=5, sex="f", hobby=2)
            yield Guest(name=6, sex="m", hobby=1)
            yield Guest(name=6, sex="m", hobby=2)
            yield Guest(name=6, sex="m", hobby=3)
            yield Guest(name=7, sex="f", hobby=2)
            yield Guest(name=7, sex="f", hobby=1)
            yield Guest(name=7, sex="f", hobby=3)
            yield Guest(name=8, sex="f", hobby=1)
            yield Guest(name=8, sex="f", hobby=3)
            yield Guest(name=8, sex="f", hobby=2)
            yield Guest(name=9, sex="f", hobby=1)
            yield Guest(name=9, sex="f", hobby=3)
            yield Guest(name=9, sex="f", hobby=2)
            yield Guest(name=10, sex="m", hobby=2)
            yield Guest(name=10, sex="m", hobby=1)
            yield Guest(name=11, sex="m", hobby=2)
            yield Guest(name=11, sex="m", hobby=1)
            yield Guest(name=12, sex="m", hobby=3)
            yield Guest(name=12, sex="m", hobby=2)
            yield Guest(name=13, sex="m", hobby=1)
            yield Guest(name=13, sex="m", hobby=3)
            yield Guest(name=14, sex="m", hobby=3)
            yield Guest(name=14, sex="m", hobby=2)
            yield Guest(name=15, sex="f", hobby=2)
            yield Guest(name=15, sex="f", hobby=1)
            yield Guest(name=15, sex="f", hobby=3)
            yield Guest(name=16, sex="f", hobby=3)
            yield Guest(name=16, sex="f", hobby=2)
            yield Guest(name=16, sex="f", hobby=1)
            yield Guest(name=17, sex="m", hobby=3)
            yield Guest(name=17, sex="m", hobby=2)
            yield Guest(name=18, sex="f", hobby=2)
            yield Guest(name=18, sex="f", hobby=1)
            yield Guest(name=19, sex="f", hobby=1)
            yield Guest(name=19, sex="f", hobby=2)
            yield Guest(name=19, sex="f", hobby=3)
            yield Guest(name=20, sex="f", hobby=1)
            yield Guest(name=20, sex="f", hobby=2)
            yield Guest(name=20, sex="f", hobby=3)
            yield Guest(name=21, sex="m", hobby=2)
            yield Guest(name=21, sex="m", hobby=3)
            yield Guest(name=21, sex="m", hobby=1)
            yield Guest(name=22, sex="f", hobby=1)
            yield Guest(name=22, sex="f", hobby=2)
            yield Guest(name=22, sex="f", hobby=3)
            yield Guest(name=23, sex="f", hobby=3)
            yield Guest(name=23, sex="f", hobby=1)
            yield Guest(name=23, sex="f", hobby=2)
            yield Guest(name=24, sex="m", hobby=1)
            yield Guest(name=24, sex="m", hobby=3)
            yield Guest(name=25, sex="f", hobby=3)
            yield Guest(name=25, sex="f", hobby=2)
            yield Guest(name=25, sex="f", hobby=1)
            yield Guest(name=26, sex="f", hobby=3)
            yield Guest(name=26, sex="f", hobby=2)
            yield Guest(name=26, sex="f", hobby=1)
            yield Guest(name=27, sex="m", hobby=3)
            yield Guest(name=27, sex="m", hobby=1)
            yield Guest(name=27, sex="m", hobby=2)
            yield Guest(name=28, sex="m", hobby=3)
            yield Guest(name=28, sex="m", hobby=1)
            yield Guest(name=29, sex="m", hobby=3)
            yield Guest(name=29, sex="m", hobby=2)
            yield Guest(name=29, sex="m", hobby=1)
            yield Guest(name=30, sex="m", hobby=2)
            yield Guest(name=30, sex="m", hobby=1)
            yield Guest(name=30, sex="m", hobby=3)
            yield Guest(name=31, sex="m", hobby=2)
            yield Guest(name=31, sex="m", hobby=1)
            yield Guest(name=32, sex="m", hobby=1)
            yield Guest(name=32, sex="m", hobby=3)
            yield Guest(name=32, sex="m", hobby=2)
        elif number_of_seats == 64:
            ## Manners 64
            yield Guest(name=1, sex="m", hobby=2)
            yield Guest(name=1, sex="m", hobby=1)
            yield Guest(name=1, sex="m", hobby=3)
            yield Guest(name=2, sex="f", hobby=2)
            yield Guest(name=2, sex="f", hobby=1)
            yield Guest(name=2, sex="f", hobby=3)
            yield Guest(name=3, sex="m", hobby=3)
            yield Guest(name=3, sex="m", hobby=2)
            yield Guest(name=4, sex="m", hobby=3)
            yield Guest(name=4, sex="m", hobby=2)
            yield Guest(name=4, sex="m", hobby=1)
            yield Guest(name=5, sex="m", hobby=2)
            yield Guest(name=5, sex="m", hobby=1)
            yield Guest(name=5, sex="m", hobby=3)
            yield Guest(name=6, sex="m", hobby=2)
            yield Guest(name=6, sex="m", hobby=3)
            yield Guest(name=6, sex="m", hobby=1)
            yield Guest(name=7, sex="f", hobby=1)
            yield Guest(name=7, sex="f", hobby=2)
            yield Guest(name=7, sex="f", hobby=3)
            yield Guest(name=8, sex="m", hobby=3)
            yield Guest(name=8, sex="m", hobby=1)
            yield Guest(name=9, sex="m", hobby=2)
            yield Guest(name=9, sex="m", hobby=3)
            yield Guest(name=9, sex="m", hobby=1)
            yield Guest(name=10, sex="m", hobby=3)
            yield Guest(name=10, sex="m", hobby=2)
            yield Guest(name=10, sex="m", hobby=1)
            yield Guest(name=11, sex="m", hobby=1)
            yield Guest(name=11, sex="m", hobby=3)
            yield Guest(name=11, sex="m", hobby=2)
            yield Guest(name=12, sex="f", hobby=3)
            yield Guest(name=12, sex="f", hobby=1)
            yield Guest(name=12, sex="f", hobby=2)
            yield Guest(name=13, sex="m", hobby=2)
            yield Guest(name=13, sex="m", hobby=3)
            yield Guest(name=14, sex="m", hobby=1)
            yield Guest(name=14, sex="m", hobby=2)
            yield Guest(name=15, sex="m", hobby=2)
            yield Guest(name=15, sex="m", hobby=3)
            yield Guest(name=15, sex="m", hobby=1)
            yield Guest(name=16, sex="f", hobby=2)
            yield Guest(name=16, sex="f", hobby=3)
            yield Guest(name=17, sex="f", hobby=3)
            yield Guest(name=17, sex="f", hobby=2)
            yield Guest(name=18, sex="m", hobby=1)
            yield Guest(name=18, sex="m", hobby=3)
            yield Guest(name=18, sex="m", hobby=2)
            yield Guest(name=19, sex="f", hobby=3)
            yield Guest(name=19, sex="f", hobby=1)
            yield Guest(name=20, sex="f", hobby=1)
            yield Guest(name=20, sex="f", hobby=3)
            yield Guest(name=20, sex="f", hobby=2)
            yield Guest(name=21, sex="m", hobby=2)
            yield Guest(name=21, sex="m", hobby=3)
            yield Guest(name=22, sex="m", hobby=2)
            yield Guest(name=22, sex="m", hobby=3)
            yield Guest(name=23, sex="f", hobby=1)
            yield Guest(name=23, sex="f", hobby=2)
            yield Guest(name=24, sex="f", hobby=3)
            yield Guest(name=24, sex="f", hobby=1)
            yield Guest(name=24, sex="f", hobby=2)
            yield Guest(name=25, sex="f", hobby=3)
            yield Guest(name=25, sex="f", hobby=1)
            yield Guest(name=25, sex="f", hobby=2)
            yield Guest(name=26, sex="m", hobby=2)
            yield Guest(name=26, sex="m", hobby=1)
            yield Guest(name=26, sex="m", hobby=3)
            yield Guest(name=27, sex="f", hobby=2)
            yield Guest(name=27, sex="f", hobby=3)
            yield Guest(name=27, sex="f", hobby=1)
            yield Guest(name=28, sex="m", hobby=1)
            yield Guest(name=28, sex="m", hobby=2)
            yield Guest(name=29, sex="f", hobby=2)
            yield Guest(name=29, sex="f", hobby=3)
            yield Guest(name=29, sex="f", hobby=1)
            yield Guest(name=30, sex="f", hobby=2)
            yield Guest(name=30, sex="f", hobby=1)
            yield Guest(name=30, sex="f", hobby=3)
            yield Guest(name=31, sex="m", hobby=1)
            yield Guest(name=31, sex="m", hobby=2)
            yield Guest(name=31, sex="m", hobby=3)
            yield Guest(name=32, sex="m", hobby=1)
            yield Guest(name=32, sex="m", hobby=2)
            yield Guest(name=33, sex="m", hobby=2)
            yield Guest(name=33, sex="m", hobby=3)
            yield Guest(name=33, sex="m", hobby=1)
            yield Guest(name=34, sex="f", hobby=2)
            yield Guest(name=34, sex="f", hobby=1)
            yield Guest(name=34, sex="f", hobby=3)
            yield Guest(name=35, sex="f", hobby=2)
            yield Guest(name=35, sex="f", hobby=3)
            yield Guest(name=36, sex="m", hobby=2)
            yield Guest(name=36, sex="m", hobby=1)
            yield Guest(name=37, sex="m", hobby=2)
            yield Guest(name=37, sex="m", hobby=1)
            yield Guest(name=38, sex="f", hobby=1)
            yield Guest(name=38, sex="f", hobby=3)
            yield Guest(name=38, sex="f", hobby=2)
            yield Guest(name=39, sex="m", hobby=3)
            yield Guest(name=39, sex="m", hobby=1)
            yield Guest(name=39, sex="m", hobby=2)
            yield Guest(name=40, sex="f", hobby=1)
            yield Guest(name=40, sex="f", hobby=2)
            yield Guest(name=40, sex="f", hobby=3)
            yield Guest(name=41, sex="m", hobby=2)
            yield Guest(name=41, sex="m", hobby=1)
            yield Guest(name=41, sex="m", hobby=3)
            yield Guest(name=42, sex="m", hobby=3)
            yield Guest(name=42, sex="m", hobby=1)
            yield Guest(name=43, sex="m", hobby=1)
            yield Guest(name=43, sex="m", hobby=3)
            yield Guest(name=43, sex="m", hobby=2)
            yield Guest(name=44, sex="m", hobby=3)
            yield Guest(name=44, sex="m", hobby=1)
            yield Guest(name=44, sex="m", hobby=2)
            yield Guest(name=45, sex="m", hobby=1)
            yield Guest(name=45, sex="m", hobby=2)
            yield Guest(name=46, sex="f", hobby=1)
            yield Guest(name=46, sex="f", hobby=2)
            yield Guest(name=46, sex="f", hobby=3)
            yield Guest(name=47, sex="m", hobby=1)
            yield Guest(name=47, sex="m", hobby=2)
            yield Guest(name=48, sex="f", hobby=3)
            yield Guest(name=48, sex="f", hobby=2)
            yield Guest(name=49, sex="m", hobby=3)
            yield Guest(name=49, sex="m", hobby=2)
            yield Guest(name=50, sex="m", hobby=2)
            yield Guest(name=50, sex="m", hobby=3)
            yield Guest(name=51, sex="f", hobby=2)
            yield Guest(name=51, sex="f", hobby=1)
            yield Guest(name=51, sex="f", hobby=3)
            yield Guest(name=52, sex="m", hobby=1)
            yield Guest(name=52, sex="m", hobby=2)
            yield Guest(name=52, sex="m", hobby=3)
            yield Guest(name=53, sex="f", hobby=2)
            yield Guest(name=53, sex="f", hobby=1)
            yield Guest(name=54, sex="f", hobby=1)
            yield Guest(name=54, sex="f", hobby=2)
            yield Guest(name=54, sex="f", hobby=3)
            yield Guest(name=55, sex="f", hobby=1)
            yield Guest(name=55, sex="f", hobby=2)
            yield Guest(name=55, sex="f", hobby=3)
            yield Guest(name=56, sex="f", hobby=2)
            yield Guest(name=56, sex="f", hobby=1)
            yield Guest(name=56, sex="f", hobby=3)
            yield Guest(name=57, sex="f", hobby=3)
            yield Guest(name=57, sex="f", hobby=2)
            yield Guest(name=57, sex="f", hobby=1)
            yield Guest(name=58, sex="f", hobby=3)
            yield Guest(name=58, sex="f", hobby=1)
            yield Guest(name=58, sex="f", hobby=2)
            yield Guest(name=59, sex="f", hobby=1)
            yield Guest(name=59, sex="f", hobby=2)
            yield Guest(name=59, sex="f", hobby=3)
            yield Guest(name=60, sex="f", hobby=3)
            yield Guest(name=60, sex="f", hobby=1)
            yield Guest(name=61, sex="f", hobby=3)
            yield Guest(name=61, sex="f", hobby=2)
            yield Guest(name=62, sex="f", hobby=1)
            yield Guest(name=62, sex="f", hobby=2)
            yield Guest(name=62, sex="f", hobby=3)
            yield Guest(name=63, sex="f", hobby=3)
            yield Guest(name=63, sex="f", hobby=1)
            yield Guest(name=63, sex="f", hobby=2)
            yield Guest(name=64, sex="f", hobby=3)
            yield Guest(name=64, sex="f", hobby=2)
        else:
            raise NotImplementedError("Invalid number of seats")

        yield LastSeat(seat=number_of_seats)

    @DefFacts(order=1)
    def declare_state(self):
        yield Count(c=1)
        yield Context(state="start")

    @Rule(AS.f1 << Context(state='start'),
          Guest(name=MATCH.n),
          AS.f3 << Count(c=MATCH.c))
    def assign_first_seat(self, f1, f3, n, c):
        self.declare(Seating(seat1=1,
                             name1=n,
                             name2=n,
                             seat2=1,
                             id=c,
                             pid=0,
                             path_done=True))

        self.declare(Path(id=c, name=n, seat=1))
        self.modify(f3, c=c + 1)
        print("seat 1", n, n, 1, c, 0, 1)
        self.modify(f1, state="assign_seats")


    @Rule(AS.f1 << Context(state='assign_seats'),
          Seating(seat1=MATCH.seat1,
                  seat2=MATCH.seat2,
                  name2=MATCH.n2,
                  id=MATCH.id,
                  pid=MATCH.pid,
                  path_done=True),
          Guest(name=MATCH.n2, sex=MATCH.s1, hobby=MATCH.h1),
          Guest(name=MATCH.g2, sex=~MATCH.s1, hobby=MATCH.h1),
          AS.f5 << Count(c=MATCH.c),
          NOT(Path(id=MATCH.id, name=MATCH.g2)),
          NOT(Chosen(id=MATCH.id, name=MATCH.g2, hobby=MATCH.h1)))
    def find_seating(self, f1, seat2, n2, id, h1, g2, c, f5):
        self.declare(Seating(seat1=seat2, name1=n2, name2=g2, seat2=seat2+1,
                             id=c, pid=id, path_done=False))
        self.declare(Path(id=c, name=g2, seat=seat2+1))
        self.declare(Chosen(id=id, name=g2, hobby=h1))
        self.modify(f5, c=c + 1)

        print("seat", seat2, n2, g2)

        self.modify(f1, state="make_path")

    @Rule(Context(state="make_path"),
          Seating(id=MATCH.id, pid=MATCH.pid, path_done=False),
          Path(id=MATCH.pid, name=MATCH.n1, seat=MATCH.s),
          NOT(Path(id=MATCH.id, name=MATCH.n1)))
    def make_path(self, id, n1, s):
        self.declare(Path(id=id, name=n1, seat=s))


    @Rule(AS.f1 << Context(state="make_path"),
          AS.f2 << Seating(path_done=False))
    def path_done(self, f1, f2):
        self.modify(f2, path_done=True)
        self.modify(f1, state="check_done")

    @Rule(AS.f1 << Context(state="check_done"),
          LastSeat(seat=MATCH.l_seat),
          Seating(seat2=MATCH.l_seat))
    def are_we_done(self, f1):
        print("Yes, we are done!!")
        self.modify(f1, state="print_results")

    @Rule(AS.f1 << Context(state="check_done"))
    def do_continue(self, f1):
        self.modify(f1, state="assign_seats")

    @Rule(Context(state="print_results"),
          Seating(id=MATCH.id, seat2=MATCH.s2),
          LastSeat(seat=MATCH.s2),
          AS.f4 << Path(id=MATCH.id, name=MATCH.n, seat=MATCH.s))
    def print_results(self, f4, n, s):
        self.retract(f4)
        print(n, s)

    @Rule(Context(state="print_results"))
    def all_done(self):
        self.halt()

if __name__ == '__main__':
    k = Manners()
    k.reset(number_of_seats=8)
    k.run()