
a = 1.5 
b = 0.03

class Tyre():
    def __init__(self, compound, efficiency, degradation):   
        self.compound = compound
        self.degradation = 0.0
        d = self.degradation
        self.efficiency = 1 - 0.003*d - 0.00008*d*d

    def updateWear(degradation_increase):
        self.degradation = a + b*d
        d = self.degradation
        for each in 0 <= d <= 100:
            P = self.efficiency = 1 - 0.003*d - 0.00008*d*d
            if 0 <= P <= 1:
                P=True
            else:
                P=False
        return P


class Track(): 
    def __init__(self, lap_distance):  # not sure how to add measurements here (e.g. km or miles), assuming this is a track
        self.name = 
        self.location = 
        self.lap_distance =       
        # distance above sea level
        # weather conditions
        # clear/busy track?



class LapTime():
    def __init__(self, minutes, seconds, base_time):  
       self.base_time =   
       
       def provisional_lap_time(self, minutes, seconds):
           self.base_time + 
       

