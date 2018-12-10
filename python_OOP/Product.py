# The owner of a store wants a program to track products. 
# Create a product class to fill the following requirements.
# Attributes:
    # Price
    # Item Name
    # Weight
    # Brand
# Status: default "for sale"
# Methods:
    # Sell: changes status to "sold"
    # Add tax: takes tax as a decimal amount as a parameter and returns the price of the item 
    # including sales tax
    # Return Item: takes reason_for_return as a parameter and changes status accordingly. 
    # If the item is being returned because it is defective, 
    # change status to "defective" and change price to 0. 
    # If it is being returned in the box, like new, mark it "for sale". If the box has been opened, set the status to "used" and apply a 20% discount.  (use "defective", "like_new", or "opened" as three possible value for reason_for_return).
    # Display Info: show all product details.

class Product:
    def __init__(self, price, item_name, weight, brand, status='for sale'):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.price = self.price*(1+tax)

    def return_item(self, reason_for_return):
        if reason_for_return == 'defective':
        self.status = 'Defective'
        self.price = 0
        elif reason_for_return == 'like new':
        self.status = 'For Sale'
        elif reason_for_return == 'open box':
        self.status = 'Used'
        self.price = 0.8 * self.price 
        return self

    def display_info(self):
        print "Item Name:", self.item_name
        print "Brand:", self.brand
        print "Status:", self.status
        print "Weight:", self.weight
        print "Price:", self.price

maxi_dress = Product(50, 'summer_dress', 100, 'coach')

