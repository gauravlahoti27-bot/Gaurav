class transport:
    def __init__(self,provider,category,total_units,daily_rate):
        self.provider=provider
        self.category=category
        self.total_units=total_units
        self.daily_rate=daily_rate
    
    def show_availability(self):
        print("the available",self.category,"are",self.total_units,"with rent of Rs",self.daily_rate,"per day from",self.provider,"agency")
        
        
        
class rental_service(transport):
    def __init__(self,provider,category,total_units,daily_rate):
        super().__init__(provider,category,total_units,daily_rate)
        
    def get_rental_duration(self):
        return int(input("enter the rental period in days: "))
    
class rental_manager(rental_service):
    def __init__(self,provider,category,total_units,daily_rate):
        super().__init__(provider,category,total_units,daily_rate)
          
    
    def calculate_cost(self,rental_days,unit_price,quantity):
        return rental_days*unit_price*quantity
    
    
def main():
    print("welcome to vehicle rental systrem!")
    car_stock,bus_stock=200,100
    car_rate,bus_rate=25,50
    
    
    while True:
        print("\nenter your choice from menu\n1.rent a car.\n2.rent a bus\n3.exit")
        user_choice=int(input("enter yor choice: "))
        
        if user_choice==1:
            vehicle=rental_manager("LA","car",car_stock,car_rate)
            vehicle.show_availability()
            quantity=int(input("enter the number of cars required: "))
            if quantity>car_stock:
                print("not enough cars available")
                continue
            car_stock-=quantity
            rental_days=vehicle.get_rental_duration()
            print(f"your order for {quantity} cars from LA agency is booked. Please pay Rs {vehicle.calculate_cost(rental_days,car_rate,quantity)}.")
        elif user_choice==2:
            vehicle=rental_manager("Botswana","bus",bus_stock,bus_rate)
            vehicle.show_availability()
            quantity=int(input("enter the number of buses required: "))
            if quantity>bus_stock:
                print("not enough buses available")
                continue
            bus_stock-=quantity
            rental_days=vehicle.get_rental_duration()
            print(f"your order for {quantity} buses from Botswana agency is booked. Please pay Rs {vehicle.calculate_cost(rental_days,bus_rate,quantity)}.")
            
        elif user_choice==3:
            print("thank you for using the rental system.\ngoodbye!")
            break
            
        else:
            print("invalid choice entered! please enter valid option.")
if __name__=="__main__":
    main()