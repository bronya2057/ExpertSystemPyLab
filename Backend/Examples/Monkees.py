from pyknow import *
import schema


class Monkey(Fact):
    location = Field(str, default="green-couch")
    on_top_of = Field(str, default="floor")
    holding = Field(str, default="blank")


class Thing(Fact):
    name = Field(str, mandatory=True)
    location = Field(str, mandatory=True)
    on_top_of = Field(str, default="floor")
    weight = Field(schema.Or("light", "heavy"), default="light")


class Chest(Fact):
    name = Field(str, mandatory=True)
    contents = Field(str, mandatory=True)
    unlocked_by = Field(str, mandatory=True)


class GoalIsTo(Fact):
    action = Field(schema.Or("hold", "unlock", "eat", "move", "on", "walk-to"),
                   mandatory=True)
    arguments = Field(schema.Or(str, [str]), mandatory=True)


class ChestUnlockingRules:
    """CHEST UNLOCKING RULES"""

    @Rule(
        GoalIsTo(action="unlock", arguments=MATCH.chest),
        Thing(name=MATCH.chest, on_top_of=NE("floor"), weight="light"),
        Monkey(holding=~MATCH.chest),
        NOT(GoalIsTo(action="hold", arguments=MATCH.chest)))
    def hold_chest_to_put_on_floor(self, chest):
        self.declare(GoalIsTo(action="hold", arguments=chest))

    @Rule(
        GoalIsTo(
            action="unlock",
            arguments=MATCH.chest),
        AS.monkey << Monkey(
            location=MATCH.place,
            on_top_of=MATCH.on,
            holding=MATCH.chest),
        AS.thing << Thing(
            name=MATCH.chest))
    def put_chest_on_floor(self, monkey, thing, place, on, chest):
        print("Monkey throws the %s off the %s onto the floor." % (chest, on))
        self.modify(monkey, holding="blank")
        self.modify(thing, location=place, on_top_of="floor")

    @Rule(
        GoalIsTo(action="unlock", arguments=MATCH.obj),
        Thing(name=MATCH.obj, on_top_of="floor"),
        Chest(name=MATCH.obj, unlocked_by=MATCH.key),
        Monkey(holding=~MATCH.key),
        NOT(GoalIsTo(action="hold", arguments=MATCH.key)))
    def get_key_to_unlock(self, key):
        self.declare(GoalIsTo(action="hold", arguments=key))

    @Rule(
        GoalIsTo(
            action="unlock",
            arguments=MATCH.chest),
        Monkey(
            location=MATCH.mplace,
            holding=MATCH.key),
        Thing(
            name=MATCH.chest,
            location=MATCH.cplace & ~MATCH.mplace,
            on_top_of="floor"),
        Chest(
            name=MATCH.chest,
            unlocked_by=MATCH.key),
        NOT(
            GoalIsTo(
                action="walk-to",
                arguments=MATCH.cplace)))
    def move_to_chest_with_key(self, cplace):
        self.declare(GoalIsTo(action="walk-to", arguments=cplace))

    @Rule(
        AS.goal << GoalIsTo(action="unlock", arguments=MATCH.name),
        AS.chest << Chest(name=MATCH.name, contents=MATCH.contents, unlocked_by=MATCH.key),
        Thing(name=MATCH.name, location=MATCH.place, on_top_of=MATCH.on),
        Monkey(location=MATCH.place, on_top_of=MATCH.on, holding=MATCH.key))
    def unlock_chest_with_key(self, goal, name, key, contents, place, chest):
        print("Monkey opens the %s with the %s revealing the %s." % (name, key, contents))
        self.modify(chest, contents="nothing")
        self.declare(Thing(name=contents, location=place, on_top_of=name, weight="light"))
        self.retract(goal)


class HoldObjectRules:
    """HOLD OBJECT RULES"""

    @Rule(
        GoalIsTo(action="hold", arguments=MATCH.obj),
        Chest(name=MATCH.chest, contents=MATCH.obj),
        NOT(GoalIsTo(action="unlock", arguments=MATCH.chest)))
    def unlock_chest_to_hold_object(self, chest):
        self.declare(GoalIsTo(action="unlock", arguments=chest))

    @Rule(
        GoalIsTo(action="hold", arguments=MATCH.obj),
        Thing(name=MATCH.obj, location=MATCH.place, on_top_of="ceiling", weight="light"),
        NOT(Thing(name="ladder", location=MATCH.place)),
        NOT(GoalIsTo(action="move", arguments__0="ladder", arguments__1=MATCH.place)))
    def use_ladder_to_hold(self, place):
        self.declare(GoalIsTo(action="move", arguments=["ladder", place]))

    @Rule(
        GoalIsTo(action="hold", arguments=MATCH.obj),
        Thing(name=MATCH.obj, location=MATCH.place, on_top_of="ceiling", weight="light"),
        Thing(name="ladder", location=MATCH.place, on_top_of="floor"),
        Monkey(on_top_of=NE("ladder")),
        NOT(GoalIsTo(action="on", arguments="ladder")))
    def climb_ladder_to_hold(self):
        self.declare(GoalIsTo(action="on", arguments="ladder"))

    @Rule(
        AS.goal << GoalIsTo(action="hold", arguments=MATCH.name),
        AS.thing << Thing(name=MATCH.name, location=MATCH.place, on_top_of="ceiling", weight="light"),
        Thing(name="ladder", location=MATCH.place),
        AS.monkey << Monkey(location=MATCH.place, on_top_of="ladder", holding="blank"))
    def grab_object_from_ladder(self, thing, monkey, goal, name):
        print("Monkey grabs the %s." % name)
        self.modify(thing, location="held", on_top_of="held")
        self.modify(monkey, holding=name)
        self.retract(goal)

    @Rule(
        GoalIsTo(action="hold", arguments=MATCH.obj),
        Thing(name=MATCH.obj, location=MATCH.place, on_top_of=MATCH.on & NE("ceiling"), weight="light"),
        Monkey(location=MATCH.place, on_top_of=~MATCH.on),
        NOT(GoalIsTo(action="on", arguments=MATCH.on)))
    def climb_to_hold(self, on):
        self.declare(GoalIsTo(action="on", arguments=on))

    @Rule(
        GoalIsTo(action="hold", arguments=MATCH.obj),
        Thing(name=MATCH.obj, location=MATCH.place, on_top_of=NE("ceiling"), weight="light"),
        Monkey(location=~MATCH.place),
        NOT(GoalIsTo(action="walk-to", arguments=MATCH.place)))
    def walk_to_hold(self, place):
        self.declare(GoalIsTo(action="walk-to", arguments=place))

    @Rule(
        GoalIsTo(action="hold", arguments=MATCH.obj),
        Thing(name=MATCH.obj, location=MATCH.place, on_top_of=MATCH.on, weight="light"),
        Monkey(location=MATCH.place, on_top_of=MATCH.on, holding=NE("blank")),
        NOT(GoalIsTo(action="hold", arguments="blank")))
    def drop_to_hold(self):
        self.declare(GoalIsTo(action="hold", arguments="blank"))

    @Rule(
        AS.goal << GoalIsTo(action="hold", arguments=MATCH.name),
        AS.thing << Thing(name=MATCH.name, location=MATCH.place, on_top_of=MATCH.on, weight="light"),
        AS.monkey << Monkey(location=MATCH.place, on_top_of=MATCH.on, holding="blank"))
    def grab_object(self, name, monkey, thing, goal):
        print("Monkey grabs the %s." % name)
        self.modify(thing, location="held", on_top_of="held")
        self.modify(monkey, holding=name)
        self.retract(goal)

    @Rule(
        AS.goal << GoalIsTo(action="hold", arguments="blank"),
        AS.monkey << Monkey(location=MATCH.place, on_top_of=MATCH.on, holding=MATCH.name & NE("blank")),
        AS.thing << Thing(name=MATCH.name))
    def drop_object(self, monkey, thing, place, name, on, goal):
        print("Monkey drops the %s." % name)
        self.modify(monkey, holding="blank")
        self.modify(thing, location=place, on_top_of=on)
        self.retract(goal)


class MoveObjectRules:
    """MOVE OBJECT RULES"""

    @Rule(
        GoalIsTo(action="move", arguments__0=MATCH.obj),
        Chest(name=MATCH.chest, contents=MATCH.obj),
        NOT(GoalIsTo(action="unlock", arguments=MATCH.chest)))
    def unlock_chest_to_move_object(self, chest):
        self.declare(GoalIsTo(action="unlock", arguments=chest))

    @Rule(
        GoalIsTo(action="move", arguments__0=MATCH.obj, arguments__1=MATCH.place),
        Thing(name=MATCH.obj, location=~MATCH.place, weight="light"),
        Monkey(holding=~MATCH.obj),
        NOT(GoalIsTo(action="hold", arguments=MATCH.obj)))
    def hold_object_to_move(self, obj):
        self.declare(GoalIsTo(action="hold", arguments=obj))

    @Rule(
        GoalIsTo(action="move", arguments__0=MATCH.obj, arguments__1=MATCH.place),
        Monkey(location=~MATCH.place, holding=MATCH.obj),
        NOT(GoalIsTo(action="walk-to", arguments=MATCH.place)))
    def move_object_to_place(self, place):
        self.declare(GoalIsTo(action="walk-to", arguments=place))

    @Rule(
        AS.goal << GoalIsTo(action="move", arguments__0=MATCH.name, arguments__1=MATCH.place),
        AS.monkey << Monkey(location=MATCH.place, holding=MATCH.obj),
        AS.thing << Thing(name=MATCH.name, weight="light"))
    def drop_object_once_moved(self, name, monkey, thing, goal, place):
        print("Monkey drops the %s." % name)
        self.modify(monkey, holding="blank")
        self.modify(thing, location=place, on_top_of="floor")
        self.retract(goal)

    @Rule(
        AS.goal << GoalIsTo(action="move", arguments__0=MATCH.obj, arguments__1=MATCH.place),
        Thing(name=MATCH.obj, location=MATCH.place))
    def already_moved_object(self, goal):
        self.retract(goal)


class WalkToPlaceRules:
    """WALK TO PLACE RULES"""

    @Rule(
        AS.goal << GoalIsTo(action="walk-to", arguments=MATCH.place),
        Monkey(location=MATCH.place))
    def already_at_place(self, goal):
        self.retract(goal)

    @Rule(
        GoalIsTo(action="walk-to", arguments=MATCH.place),
        Monkey(location=~MATCH.place, on_top_of=NE("floor")),
        NOT(GoalIsTo(action="on", arguments="floor")))
    def get_on_floor_to_walk(self):
        self.declare(GoalIsTo(action="on", arguments="floor"))

    @Rule(
        AS.goal << GoalIsTo(action="walk-to", arguments=MATCH.place),
        AS.monkey << Monkey(location=~MATCH.place, on_top_of="floor", holding="blank"))
    def walk_holding_nothing(self, place, monkey, goal):
        print("Monkey walks to %s." % place)
        self.modify(monkey, location=place)
        self.retract(goal)

    @Rule(
        AS.goal << GoalIsTo(action="walk-to", arguments=MATCH.place),
        AS.monkey << Monkey(location=~MATCH.place, on_top_of="floor", holding=MATCH.obj & NE("blank")))
    def walk_holding_object(self, place, obj, goal, monkey):
        print("Monkey walks to %s holding the %s." % (place, obj))
        self.modify(monkey, location=place)
        self.retract(goal)


class GetOnObjectRules:
    """GET ON OBJECT RULES"""

    @Rule(
        AS.goal << GoalIsTo(action="on", arguments="floor"),
        AS.monkey << Monkey(on_top_of=MATCH.on & NE("floor")))
    def jump_onto_floor(self, on, monkey, goal):
        print("Monkey jumps off the %s onto the floor." % on)
        self.modify(monkey, on_top_of="floor")
        self.retract(goal)

    @Rule(
        GoalIsTo(action="on", arguments=MATCH.obj),
        Thing(name=MATCH.obj, location=MATCH.place),
        Monkey(location=~MATCH.place),
        NOT(GoalIsTo(action="walk-to", arguments=MATCH.place)))
    def walk_to_place_to_climb(self, place):
        self.declare(GoalIsTo(action="walk-to", arguments=place))

    @Rule(
        GoalIsTo(action="on", arguments=MATCH.obj),
        Thing(name=MATCH.obj, location=MATCH.place),
        Monkey(location=MATCH.place, holding=NE("blank")),
        NOT(GoalIsTo(action="hold", arguments="blank")))
    def drop_to_climb(self):
        self.declare(GoalIsTo(action="hold", arguments="blank"))

    @Rule(
        GoalIsTo(action="on", arguments=MATCH.obj),
        Thing(name=MATCH.obj, location=MATCH.place, on_top_of=MATCH.on),
        Monkey(location=MATCH.place, on_top_of=~MATCH.on & ~MATCH.obj, holding="blank"),
        NOT(GoalIsTo(action="on", arguments=MATCH.on)))
    def climb_indirectly(self, on):
        self.declare(GoalIsTo(action="on", arguments=on))

    @Rule(
        AS.goal << GoalIsTo(action="on", arguments=MATCH.obj),
        Thing(name=MATCH.obj, location=MATCH.place, on_top_of=MATCH.on),
        AS.monkey << Monkey(location=MATCH.place, on_top_of=MATCH.on, holding="blank"))
    def climb_directly(self, obj, monkey, goal):
        print("Monkey climbs onto the %s." % obj)
        self.modify(monkey, on_top_of=obj)
        self.retract(goal)

    @Rule(
        AS.goal << GoalIsTo(action="on", arguments=MATCH.obj),
        Monkey(on_top_of=MATCH.obj))
    def already_on_object(self, goal):
        self.retract(goal)


class EatObjectRules:
    """EAT OBJECT RULES"""

    @Rule(
        GoalIsTo(action="eat", arguments=MATCH.obj),
        Monkey(holding=~MATCH.obj),
        NOT(GoalIsTo(action="hold", arguments=MATCH.obj)))
    def hold_to_eat(self, obj):
        self.declare(GoalIsTo(action="hold", arguments=obj))

    @Rule(
        AS.goal << GoalIsTo(action="eat", arguments=MATCH.name),
        AS.monkey << Monkey(holding=MATCH.name),
        AS.thing << Thing(name=MATCH.name))
    def satisfy_hunger(self, goal, thing, monkey, name):
        print("Monkey eats the %s." % name)
        self.modify(monkey, holding="blank")
        self.retract(goal)
        self.retract(thing)


class MonkeesAndBananas(ChestUnlockingRules,
                        HoldObjectRules,
                        MoveObjectRules,
                        WalkToPlaceRules,
                        GetOnObjectRules,
                        EatObjectRules,
                        KnowledgeEngine):

    @DefFacts()
    def startup(self):
        """INITIAL STATE"""
        yield Monkey(location="t5-7", on_top_of="green-couch", holding="blank")
        yield Thing(name="green-couch", location="t5-7", on_top_of="floor", weight="heavy")
        yield Thing(name="red-couch", location="t2-2", on_top_of="floor", weight="heavy")
        yield Thing(name="big-pillow", location="t2-2", on_top_of="red-couch", weight="light")
        yield Thing(name="red-chest", location="t2-2", on_top_of="big-pillow", weight="light")
        yield Chest(name="red-chest", contents="ladder", unlocked_by="red-key")
        yield Thing(name="blue-chest", location="t7-7", on_top_of="ceiling", weight="light")
        yield Chest(name="blue-chest", contents="bananas", unlocked_by="blue-key")
        yield Thing(name="blue-couch", location="t8-8", on_top_of="floor", weight="heavy")
        yield Thing(name="green-chest", location="t8-8", on_top_of="ceiling", weight="light")
        yield Chest(name="green-chest", contents="blue-key", unlocked_by="red-key")
        yield Thing(name="red-key", location="t1-3", on_top_of="floor", weight="light")
        yield GoalIsTo(action="eat", arguments="bananas")


if __name__ == '__main__':
    mab = MonkeesAndBananas()
    mab.reset()
    mab.run()
