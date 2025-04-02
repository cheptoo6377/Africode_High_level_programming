from model import vehicle
class vehicle:
    def __init__(self,model,make,year):
        self.model = model
        self.make = make
        self.year = year
    def get_info(self):
        return(self.year) (self.make) (self.model)
    def start_engine(self):
        return "engine started"
class electriccar(vehicle):
    def __init__(self, model, make, year,battery):
        super().__init__(model, make, year)
        self.battery = battery
    def start_engine (self):
        return "the electric motor"
    def get_battery_info(self):
        return(f"this is electric{self.battery}")
class engine:
    def __init__(self,power):
        self.power = power
    def get_power(self):
        return(f"engine profuces{self.power}")
class ectricsystem:
    def __init__(self,voltage):
        self.voltage = voltage
    def get_voltage(self):
        return(f"this electric car{self.voltage}")
     
        
