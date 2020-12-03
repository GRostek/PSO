
class systemIIR:

    def __init__(self, wspolczynnikia, wspolczynnikib):
        self.wspolczynnikia = wspolczynnikia
        self.wspolczynnikib = wspolczynnikib

        self.dane = []
        self.daneb = []


        for i in range(len(wspolczynnikia)):
            self.dane.append(0)
        
        for i in (range(len(wspolczynnikib))):
            self.daneb.append(0)
    
    def MnozISumuj(self):
        
        suma = 0
        
        for i in range(len(self.wspolczynnikia)):
            a = self.wspolczynnikia[i]
            x = self.dane[i]
            suma += (a * x)
        
        return suma

    def MnozISumujB(self):
        
        suma = 0
        
        for i in range(len(self.wspolczynnikib)):
            b = self.wspolczynnikib[i]
            y = self.daneb[i]
            suma += (b * y)
        
        return suma
    
    def WpiszNowa(self,x):
        
        indeks = len(self.wspolczynnikia) - 1
        
        for i in range(len(self.wspolczynnikia)):
            if(i < len(self.wspolczynnikia)):
                self.dane[indeks] = self.dane[indeks - 1]
                indeks -= 1
                
        self.dane[0] = x

    def WpiszNowaB(self,y):
        
        indeks = len(self.wspolczynnikib) - 1
        
        for i in range(len(self.wspolczynnikib)):
            if(i < len(self.wspolczynnikib)):
                self.daneb[indeks] = self.daneb[indeks - 1]
                indeks -= 1
                
        self.daneb[0] = y


    def WyzerujDane(self):
        for i in range(len(self.dane)):
            self.dane[i] = 0
        for i in range(len(self.daneb)):
            self.daneb[i] = 0
    
    
    def Wylicz(self,x):
        
        self.WpiszNowa(x)
        wynik = self.MnozISumuj()
        wynikb = self.MnozISumujB()
        self.WpiszNowaB(wynik + wynikb)
        
        return (wynik + wynikb)


    
