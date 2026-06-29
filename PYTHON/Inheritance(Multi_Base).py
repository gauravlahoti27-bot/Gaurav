class Father:
    def skills(self):
        print("I have father's skill")
class Mother:
    def talents(self):
        print("I have mother's talent")
class Child(Father,Mother):
    def money(self):
        print("I have Mother, Father and Money")
c = Child()
c.skills()
c.talents()
c.money()