class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand + " is the brand of the car."
        
    def full_name(self):
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def battery_info(self):
        return f"{self.__brand} {self.model} has a {self.battery_size} kWh battery."



my_electric_car = ElectricCar("Tesla", "Model S", 100)
print(my_electric_car.get_brand())
# print(my_electric_car.brand())



# In encapsulation, we can restrict access to certain attributes or methods using __ (double underscore) before the attribute or method name.
# This makes them private and not accessible from outside the class.but we can still access them using getter methods and in its own class.