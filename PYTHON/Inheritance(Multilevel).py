class Grandparent:
    def house(self):
        print("House from grandparents")
class Parent(Grandparent):
    def car(self):
        print("Car from parents")
class Child(Parent):
    def bike(self):
        print("Bike from child")
c = Child()
c.house()
c.car()
c.bike()

p = Parent()
p.house()
p.car()

g = Grandparent()
g.house()