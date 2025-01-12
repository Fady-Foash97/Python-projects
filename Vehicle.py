class Vehicle:
    def __init__(self, car_name, manufacturer, speed):
        self.car_name = car_name
        self.manufacturer = manufacturer
        self.speed = speed 

car1 = Vehicle("Dodge Charger", "Chrysler", "132 miles per hour")
car2 = Vehicle("Mini Cooper", "BMW", "250 kilometer per hour")
car3 = Vehicle("Aston Martin db10", "Aston martin", "193 miles per hour")
car4 = Vehicle("Aston Martin db5", "Aston martin", "145 miles per hour")
car5 = Vehicle("Toyota Corolla", "Toyota", "117 miles per hour")
print(f"Car name: {car1.car_name} , manufacturer: {car1.manufacturer}, speed: {car1.speed}")
print(f"Car name: {car2.car_name} , manufacturer: {car2.manufacturer}, speed: {car2.speed}")
print(f"Car name: {car3.car_name} , manufacturer: {car3.manufacturer}, speed: {car3.speed}")
print(f"Car name: {car4.car_name} , manufacturer: {car4.manufacturer}, speed: {car4.speed}")
print(f"Car name: {car5.car_name} , manufacturer: {car5.manufacturer}, speed: {car5.speed}")