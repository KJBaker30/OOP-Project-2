a = 1.5
b = 0.03


class Tyre():                                                # there is a tyre
    def __init__(self, degradation, performance):            # tyre has a degradation value and performance value 
        self.degradation = degradation
        self.deg = degradation                               # self.deg = self.degradation
        self.performance = performance
        
        self.deg = 0.0                                       # tyre deg = 0.0
        self.performance = 1.0                               # tyre performance = 1.0

    def updateDegradation(self, degradation_increase):       # update of tyre deg value 
        self.degradation_increase = degradation_increase     
        degradation_increase = a + b*self.deg                # deg increase = 1.5 + 0.03(0)  -  base decrease in deg per lap = 1.5
        
        self.deg = self.deg + degradation_increase          # 0 + new deg value(= 1.5) = new deg value 
        return self.deg                                      # replace old deg value with new deg value & store
    
    def updatePerformance(self, performance_decrease):       # update of tyre performance
        self.performance_decrease = performance_decrease
        performance_decrease = 1 - 0.003*self.deg - 0.00008*self.deg*self.deg   # performance decrease = 1 - deg value(0.03) - deg value ^2 (0.00008)

        self.performance = self.performance - performance_decrease             # performance value - decrease = new performance value
        return self.performance                              # replace performance value with new value and store
    
print(Tyre.updateDegradation)
print(Tyre.updatePerformance)

        
        
# class Track():                                               # There is a track
    # def __init__(self, distance):                            # The track has a distance - not sure how to add measurements here (e.g. km or miles)
    #     self.distance = distance  
        # distance above sea level
        # weather conditions
        # no. of cars on track
        # elevation

       

class LapTime():                                             # there is a laptime 
    def __init__(self, minutes, seconds, base_time):         # the laptime has minutes and seconds and a base lap time
       self.minutes = minutes
       self.seconds = seconds
       self.base_time = base_time         
       
    def provisional_lap_time(self, base_time, minutes, seconds):        # there is a provisional lap time that has minutes and seconds
           self.minutes = minutes
           self.seconds = seconds
           self.base_time = base_time
           base_time = 1*minutes + 00*seconds

           



          # self.provisional_lap_time = self.base_time + ...
          # #Laptime(L) = BaseTime + L*(P(w(L)))




tyre_one = Tyre('0.0', '1.0')

tyre_one.updateDegradation('a + b*self.deg')
print('Tyre Degradation:', tyre_one.deg)
tyre_one.updatePerformance('1 - 0.003*self.deg - 0.00008*self.deg*self.deg')
print('Performance Value:', ((1 - tyre_one.performance)*100),'%')





       