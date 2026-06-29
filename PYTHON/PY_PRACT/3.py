class Person:
    def __init__(self,name):
        self.name = name
    class DOB:
        def __init__(self,day,month,year):
            self.day = day
            self.month = month
            self.year = year
        
        def display_dob(self):
            print(f"DOb:{self.day}/{self.month}/{self.year}")
p = Person("Gaurav")

d = p.DOB(1,1,2000)

print("Name:", p.name)
d.display_dob()
