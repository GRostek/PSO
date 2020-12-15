from audio_source import audio_source
from math import sqrt, pow

class virtual_space:

    def __init__(self, MAXX,MAXY, Xs, Ys, ear_distance):
        self.MAXX = float(MAXX)
        self.MAXY = float(MAXY)
        self.sources = []
        self.Xs = float(Xs)
        self.Ys = float(Ys)
        self.ear_distance = float(ear_distance)


    def add_source(self, Xzd, Yzd):
        source = audio_source(Xzd,Yzd)
        self.sources.append(source)


    def get_distance_from_listener(self, source):
        # Jako punkty Xs oraz Ys uznaję lewe ucho
        left_distance = 0
        right_distance = 0
        #Jeśli jest "poza głową"
        if(source.Xzd < self.Xs or source.Xzd+self.ear_distance > self.Xs):
            left_distance =  sqrt(pow(source.Yzd - self.Ys,2) + pow(source.Xzd - self.Xs,2))
            right_distance = sqrt(pow(source.Yzd - self.Ys,2) + pow(source.Xzd - (self.Xs+self.ear_distance),2))

        else:
            left_ear_distance = abs(source.Xzd - self.Xs)
            right_ear_distance = abs(source.Xzd - (self.Xs+self.ear_distance))

            left_distance =  sqrt(pow(source.Yzd - self.Ys,2) + pow(source.Xzd - (self.Xs+left_ear_distance),2))
            right_distance = sqrt(pow(source.Yzd - self.Ys,2) + pow(source.Xzd - (self.Xs+right_ear_distance),2))

        return left_distance, right_distance

        
    def get_time(self,left_ear_distance,right_ear_distance):

        left = left_ear_distance/344.0
        right = right_ear_distance/344.0

        return left, right

    def get_db_drop(self):
        print("todo")

    







    