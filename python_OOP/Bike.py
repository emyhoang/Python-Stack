class Bike:
    def __init__(self,price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def display_info(self):
        print(self.price, self.max_speed, self.miles)

    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    def reverse(self):
        print("Reversing")
        # What would you do to prevent the instance from having negative miles?
        if self.miles <= 0:
            print("You Lose")
        else: 
            self.miles -= 5
        return self
        
bike1 = Bike(500,"25mph") 
# Have the first instance ride three times, reverse once and have it displayInfo().
bike1.ride().ride().ride().reverse().display_info()
bike2 = Bike(250,"15mph")
# Have the second instance ride twice, reverse twice and have it displayInfo(). 
bike2.ride().ride().reverse().reverse().display_info()
bike3 = Bike(950,"25mph")
# Have the third instance reverse three times and displayInfo().
bike3.reverse().reverse().reverse().display_info()