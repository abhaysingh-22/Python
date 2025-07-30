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

    @staticmethod   # this is known as decorator for static method.
    # when we use static method, we don't need to pass self or cls as the first argument.
    # Static methods can be called on the class itself, not just on instances.
    def general_description():
        return "This is a general car class that can be used to create different types of cars."

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

print(isinstance(my_electric_car, ElectricCar))  # Check if my_electric_car is an instance of ElectricCar
print(isinstance(my_electric_car, Car))  # Check if my_electric_car is also an instance of Car
