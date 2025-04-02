#inheritance
class vehicle:
    def __init__(self,model,make,year):
        self.model = model
        self.make = make
        self.year = year
    def get_info(self):
        return(self.year) (self.make) (self.model)
vehicle2 = vehicle("toyota","corolla",2020)

class car(vehicle):
    def __init__(self, model, make, year,fuel_type):
        super().__init__(model, make, year)
        self.fuel_type = fuel_type
    def get_fuel_type(self):
        return self.fuel_type
car1 = car("honda","mazda",2000,"diesel")
print(car1.get_info())

