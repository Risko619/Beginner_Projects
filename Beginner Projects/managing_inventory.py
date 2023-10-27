
""" First we start by creating a Product class, followed by a 'constructor method'"""
class Product:
  def __init__(self, name, price, units):

    """ Here are the properties we'll be using"""    
    self.name = name
    self.price = price
    self.units = units
    self.is_on_sale = False

#Create a method to make printing descriptive info reusable
  def describe(self):
    print(f"Product name: {self.name}")
    print(f"Product price: {self.price}")
    print(f"Available units: {self.units}")
    print(f"On sale? {self.is_on_sale}")
    print(f"In stock? {self.is_in_stock()}")
    print("-------------------------")

# This method will increase inventory amount
  def add_units(self, units):
    self.units += units

#This method will reduce inventory count to the available number of units
  def reduce_units(self, units):
    if self.units - units >= 0:
      self.units -= units
    else:
      print("Error: Not enough units in inventory.")

# We hold a sale due to too many laptops in inventory
  def reduce_price(self, discount):
    self.price = self.price * (1 - discount)
    self.is_on_sale = True

# Finally this method checks whether a product is in stock or not
  def is_in_stock(self):
    return self.units > 0

# laptop is an object for one of the products
laptop = Product("Dell Laptop", 850, 12)

# here I'm calling each new method I create to verify it works
laptop.describe()
laptop.add_units(15)
laptop.reduce_units(10)
laptop.reduce_units(20)
laptop.describe()
laptop.reduce_price(0.1)
laptop.describe()

# Instances are Variables in a Class
# Methods are functions in a Class

#Additional Tasks:
'''
1. Add code to the add_units() and reduce_units() methods to verify that the passed in units value is a number.
2. Modify the reduce_price() method to ensure the discount percentage is between 0 and 1.
3. Implement a method to calculate the total value of the available product inventory.
4. Modify the describe() method to display the product's price formatted with a dollar sign and two decimal points.
'''

"""
During this project I created a class with a constructor, added methods to describe the product info, 
add and reduce the number of units in inventory, reduce the product price, and check whether the product was in stock.
I then created a product instance to test out your class functionality!
"""