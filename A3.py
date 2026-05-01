a = 1.5
b = 0.03


class Tyre():                                               
    def __init__(self, degradation, performance):            
        self.deg = degradation                               
        self.performance = performance
        
        self.deg = 0.0                                       
        self.performance = 1.0                             

    def updateDegradation(self):                                  
        degradation_increase = a + b*self.deg               
        self.deg = degradation_increase + self.deg  

    def updatePerformance(self):                            
        performance_decrease = 1 - 0.003*self.deg - 0.00008*self.deg*self.deg   
        self.performance = performance_decrease


       
class LapTime():                                              
    def __init__(self, base_time):
       self.base_time = base_time
       base_time = 90
       self.provisional_lap_time = 0.0       
       
    def calcProvisionalLapTime(self, tyre):      
        self.provisional_lap_time = self.base_time + self.provisional_lap_time*(1-tyre.performance) 
        return self.provisional_lap_time
    
    def getProvisionalLapTime(self):
        minutes = int(self.provisional_lap_time // 60)
        seconds = int(self.provisional_lap_time % 60)
        milliseconds = int((self.provisional_lap_time - (minutes*60 + seconds))*1000)
        return f"{minutes:02d}:{seconds:02d}.{milliseconds:03d}"



tyre_one = Tyre('0.0', '1.0')
laptime_manager = LapTime(90)

for lap in range(1,10):
    tyre_one.updateDegradation()
    tyre_one.updatePerformance()
    laptime_manager.calcProvisionalLapTime(tyre_one)
    print(f"Lap: {lap}  Tyre Degradation: {tyre_one.deg:.2f}%   Tyre Performance: {tyre_one.performance*100:.2f}%")
    print(f"Provisional Lap Time: {laptime_manager.getProvisionalLapTime()}")

