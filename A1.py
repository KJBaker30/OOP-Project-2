
class Tyre():   #There is a tyre
    def __init__(self, performance, wear):  #The tyre has a performance value and a wear value 
        a = 1.5 
        b = 0.03   
        w = self.wear = a + b*w  # wear, w = a + bw 
        w_lower_bound = 0 # the lowest possible value of w
        w_upper_bound = 100 # the highest possible value of w 
        for each in w_lower_bound <= w <= w_upper_bound:  # for each w between 0 and 100%..
            P = self.performance = 1 - 0.003*w - 0.00008*w*w # relative performance, P, is equal to 1 - 0.003w - 0.00008w^2
            P_upper_bound = 1  # biggest value of P = 1
            P_lower_bound = 0  # Smallest value of P = 0
            if P_lower_bound <= P <= P_upper_bound:  # if P is between 0 and 1
                P=True # P is valid 
            else:
                P=False 

        # P = self.performance = 1 - 0.003*w - 0.00008*w*w # performance, P, is equal to 1 - 0.003w - 0.00008w^2
        # P_upper_bound = 1  # biggest value of P = 1
        # P_lower_bound = 0  # Smallest value of P = 0
        # if P_lower_bound <= P <= P_upper_bound:  # if P is between 0 and 1
        #     P=True # P is valid 
        # else:
        #     P=False 
        
        # for w in wear: # for all wear values...
        #     print (P)  # print performance value 

        

class Track():   # There is a track
    def __init__(self, distance):  #The track has a distance - not sure how to add measurements here (e.g. km or miles)
        self.distance =  # track has distance - unknown
        # distance above sea level
        # weather conditions
        # clear/busy track?



class LapTime():  # there is a laptime 
    def __init__(self, minutes, seconds, base_time):  # the laptime has minutes and it has seconds - does base_time need to go in brackets 
       self.base_time =              #if base_time in brackets, get rid 
       L = base_time + 

