class Parent:
    def show(self):
        print("I am Parent")

class Child1(Parent):
    def c1(self):
        print("I am Child1")

class Child2(Parent):
    def c2(self):
        print("I am Child2")

c1= Child1()
c2= Child2()

c1.show()
c2.show()
c1.c1()
c2.c2()
