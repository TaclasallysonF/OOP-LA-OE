class Toy:
 def __init__(self, name, price):
  self.name = name
  self.price = price
 def describeToy(self):
  print(f"My Toy's name is {self.name} and the price of it is {self.price}")
class Car(Toy):
 def __init__(self, name, price):
  super().__init__(name, price)
Hotwheels = Toy("Hotwheels", "50,000")
Hotwheels.describeToy