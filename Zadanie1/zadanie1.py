import matplotlib.pyplot as plt
import math
import numpy as np

from scipy.io import wavfile
from scipy.io.wavfile import write
samplerate, data = wavfile.read('Struna 1 - E.wav') #Plik mono!!!!!



print ("Częstotliwość próbkowania ......... " + str(samplerate) + " Hz")
print ("Liczba próbek ..................... " + str(len(data)))

okres_probkowania = 1 / samplerate

print ("Okres próbkowania ................. " + str(okres_probkowania) + " s")

czas_trwania_nagrania = len(data) * okres_probkowania

print ("Czas trwania nagrania ............. " + str(czas_trwania_nagrania) + " s")



ile_przesunac = float(input("O ile czasu przesunąć sygnał? "))

ile_wzmocnic = -1

while ile_wzmocnic < 0 or ile_wzmocnic > 1:
    ile_wzmocnic = float(input("O ile wzmocnic sygnał? [0,1] "))

liczba_probek = int(ile_przesunac/okres_probkowania)

delay = np.zeros(liczba_probek, dtype=np.int16)

delay = np.concatenate((delay, data))

dB = 20 * math.log10(np.sqrt(np.mean(np.power(data,2))))


delay = np.multiply(delay,ile_wzmocnic, casting='unsafe')

delay = np.array(delay, dtype=np.int16)

#amplituda_po = abs(max(delay.astype(np.int32)) - min(delay.astype(np.int32))) # liczenie amplitudy wzmocnienia

data = np.concatenate((data, np.zeros(liczba_probek,dtype=np.int16)))


delay = np.add(data, delay)

delay_x = range(len(data))

plt.plot(delay_x, delay)

#amplituda_przed = abs(max(data.astype(np.int32)) - min(data.astype(np.int32)))

#dB = 10 * math.log10(amplituda_przed)

print("dB przed efektem: " + str(dB))

#amplituda_po = abs(max(delay) - min(delay))

dB = 20 * math.log10(np.sqrt(np.mean(np.power(delay,2))))
print("dB po efekcie: " + str(dB))



plt.show()

write("zadanie.wav",samplerate,delay)


