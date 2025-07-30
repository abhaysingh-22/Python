class Car:
    
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand + " is the brand of the car."
        
    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "This car uses petrol or diesel."

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "This car uses electricity."

    def battery_info(self):
        return f"{self.__brand} {self.model} has a {self.battery_size} kWh battery."



my_electric_car = ElectricCar("Tesla", "Model S", 100)
print(my_electric_car.fuel_type())

my_car = Car("Toyota", "Corolla")
print(my_car.fuel_type())

your_car = Car("Honda", "Civic")
print(your_car.fuel_type()) 

print(Car.total_car)