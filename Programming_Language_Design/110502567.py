class Beverage:
    def cost(self):
        return 0
    def description(self):
        return "beverage"

# The above is a fixed class, please do not modify it.
# Please complete other class definitions here >>
    
class Ingridient(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost()
    
    def description(self):
        return self.beverage.description()
    
class BlackTea(Beverage):
    def cost(self):
        return 25
    def description(self):
        return "blackTea"
    
class GreenTea(Beverage):
    def cost(self):
        return 20
    def description(self):
        return "greenTea"
    
class Ice(Ingridient):
    def cost(self):
        return self.beverage.cost() + 1
    def description(self):
        return self.beverage.description() + " + ice"
    
class Milk(Ingridient):
    def cost(self):
        return self.beverage.cost() + 5
    def description(self):
        return self.beverage.description() + " + milk"
    
class Bubble(Ingridient):
    def cost(self):
        return self.beverage.cost() + 10
    def description(self):
        return self.beverage.description() + " + bubble"
    
# << Please complete other class definitions here
# The following are test cases, please do not modify them

beverages = [
    BlackTea(),
    GreenTea(),
    Ice(BlackTea()),
    Milk(GreenTea()),
    Bubble(Ice(GreenTea())),
    Milk(Milk(BlackTea())),
    Milk(Ice(GreenTea())),
    Bubble(Milk(Ice(BlackTea())))
]

for b in beverages:
    if isinstance(b, Beverage):
        print(b.description(), "is a beverage!")
    else:
        print(b.description(), "is not a beverage?")
    print("Its price is", b.cost())
'''
Output:
blackTea is a beverage!
Its price is 25
greenTea is a beverage!
Its price is 20
blackTea + ice is a beverage!
Its price is 26
greenTea + milk is a beverage!
Its price is 25
greenTea + ice + bubble is a beverage!
Its price is 31
blackTea + milk + milk is a beverage!
Its price is 35
greenTea + ice + milk is a beverage!
Its price is 26
blackTea + ice + milk + bubble is a beverage!
Its price is 41
'''