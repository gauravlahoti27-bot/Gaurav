class A:
    def showa(self):
        print("A")
class B:
    def showb(self):
        print("B")
class C(A,B):
    def showc(self):
        print("C")

obj = C()
obj.showa()
obj.showb()    
obj.showc()