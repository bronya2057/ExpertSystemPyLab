# Whenever going to Football match or music festieval we are asked for tickets. Below is example of system machine
# that checks the ticket and if not, it asks to buy a ticket. What you can check by this example is that order of
# @Rules is not important for the engine. When asked by program you tell that both you have money and ticket it will
# pass two rules. First rule that is passed is the most suitable. By this I mean that if we have 2 arguments in Rule
# and both are passed then it will be fired faster than Rule with only one condition. That is why we first receive
# Lucky you and below this is You can pass which has only one argument about the ticket.
from pyknow import *
from random import choice

class Money(Fact):
    """ ask about money you have """
    pass


class Ticket(Fact):
    """ ask about free ticker """


class Solution(KnowledgeEngine):

    @Rule(Ticket(ticket='yes'))
    def have_ticket(self):
        print('You can pass')

    @Rule(AND(Money(money='yes'), Ticket(ticket='yes')))
    def have_ticket_and_money(self):
        print('Lucky you')

    @Rule(AND(Money(money='yes'), Ticket(ticket='no')))
    def buy_ticket(self):
        print('Buy the ticket')

    @Rule(AND(Money(money='no'), Ticket(ticket='no')))
    def no_money_nor_ticket(self):
        print('Sorry no money no honey :<')


if __name__ == '__main__':
    engine = Solution()
    engine.reset()

    ask_money = input("Did you have money?: ")
    ask_ticket = input("Did you have free luanch ticket?: ")

    engine.declare((Money(money=ask_money)), (Ticket(ticket=ask_ticket)))

    engine.run()
