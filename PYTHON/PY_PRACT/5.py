class base:
    def __init__(self):
        print("Base class constructor1")
    def display(self):
        print("Base class method1")
class derived(base):
    def __init__(self):
        super().__init__()
        print("Derived class constructor2")
    def display(self):
        super().display()
        print("Derived class method2")
    
d = derived()
d.display()