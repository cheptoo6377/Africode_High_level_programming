from models import engine,ectricsystem
from inheritance import car
class hybridcar(ectricsystem,engine,car):
    def __init__(self,make,model,year,fuel_type,power, voltage):
        engine .__init__(self,power)
        ectricsystem .__init__(self,voltage)
        car .__init__(self,make,model,year,fuel_type,)
        
    def get_hybrid_info(self):
        return(f"this hybrid has{self.power}horsepower and {self.voltage} volts")

my_hybrid = hybridcar("toyota","prius",2022,"hybrid",122,300)
print(my_hybrid.get_hybrid_info())
print(my_hybrid.get_hybrid_info())