class Car:
	def __init__(self, brand, color):
		self.brand = brand
		self.color = color
	def drive(self):
		print(f"{self.brand} ({self.color}) is driving...")
car1 = Car("maruthi", "red")
car2 = Car("benz", "black")
car1.drive()
car2.drive()

class Bike:
	def __init__(self, brand, price):
		self.brand = brand
		self.price = price

	def ride(self):
		print(f"{self.brand} bike with price {self.price} is riding...")

bike1 = Bike("yamaha", 1500)
bike1.ride()

bike2 = Bike("honda", 2000)
bike2.ride()
