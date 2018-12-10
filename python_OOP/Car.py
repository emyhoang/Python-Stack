# Create a class called  Car.
class Car:
    # In the __init__(),allow the user to specify the following attributes: price, speed, fuel, mileage. 
    def __init__(self, price, speed, fuel, mileage):
        self.price = price 
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        # If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.
        if self.price >= 10000: 
		    self.tax = ".15"
	    else: 
		    self.tax = ".12"
		self.display_all()
    # In the class have a method called display_all() that 
    def display_all(self):
        # returns all the information about the car as a string. 
        print(self.price, self.speed, self.fuel, self.mileage, self.tax) 

# Create six different instances of the class Car.
car1 = Car(2500, "15mph", "full", "15mpg")
car2 = Car(3000, "25mpg", "not full", "13mpg")
car3 = Car(3500, "45mpg", "full", "90mpg")
car4 = Car(5000, "65mpg", "full", "254mpg")
car5 = Car(8000, "75mpg", "full", "588mpg")
Car6 = Car(12000, "85mpg", "full", "55mpg")
    
