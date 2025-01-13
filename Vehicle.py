class Vehicle:
    def __init__(self, car_name, manufacturer, speed, year):
        self.car_name = car_name
        self.manufacturer = manufacturer
        self.speed = speed 
        self.year = year

car1 = Vehicle("Dodge Charger", "Chrysler", "132 miles per hour", 1964)
car2 = Vehicle("Mini Cooper", "BMW", "250 kilometer per hour", 1959)
car3 = Vehicle("Aston Martin db10", "Aston martin", "193 miles per hour", 2015)
car4 = Vehicle("Aston Martin db5", "Aston martin", "145 miles per hour", 1963)
car5 = Vehicle("Toyota Corolla", "Toyota", "117 miles per hour", 1966)
print(f"Car name: {car1.car_name} , manufacturer: {car1.manufacturer}, speed: {car1.speed}, year: {car1.year}")
print(f"Car name: {car2.car_name} , manufacturer: {car2.manufacturer}, speed: {car2.speed}, year: {car2.year}")
print(f"Car name: {car3.car_name} , manufacturer: {car3.manufacturer}, speed: {car3.speed}, year: {car3.year}")
print(f"Car name: {car4.car_name} , manufacturer: {car4.manufacturer}, speed: {car4.speed}, year: {car4.year}")
print(f"Car name: {car5.car_name} , manufacturer: {car5.manufacturer}, speed: {car5.speed}, year: {car5.year}")