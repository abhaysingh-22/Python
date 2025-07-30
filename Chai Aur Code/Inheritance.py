class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def battery_info(self):
        return f"{self.brand} {self.model} has a {self.battery_size} kWh battery."



my_electric_car = ElectricCar("Tesla", "Model S", 100)
print(my_electric_car.battery_info())   