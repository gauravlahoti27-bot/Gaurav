class super():
    def __init__(self):
        print("Parent")
class sub():
    def __init__(self):
        super().__init__()
        print("Child")
c = sub()
