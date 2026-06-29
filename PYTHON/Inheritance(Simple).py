class Parent:
    def greet(self):
        print("Hello from parent class")
class Child(Parent):
    def welcome(self):
        print("Hello from child class")
c = Child()
c.greet()
c.welcome()