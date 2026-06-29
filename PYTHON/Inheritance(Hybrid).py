class A:
    def a(self):
        print("Class A - Parent")
class B(A):
    def b(self):
        print("Class B - Derived from A")
class C:
    def c(self):
        print("Class C - New")
class D(B,C):
    def d(self):
        print("Class D - Derived from B and C")

obj = D()

obj.a()
obj.b()
obj.c()
obj.d()