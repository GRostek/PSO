import math
import numpy as np
from matplotlib import pyplot as plt

import scipy as sc


#FIR - odwrotna transformata fouriera
#IIR - transformata Z 


def butterworth(s, s0, n):
    return 1/math.sqrt(1+math.pow(s/s0,2*n))


def oknoTrojkatne(data):    
    wynik_tab = []
    N = len(data)
    for n, wartosc in enumerate(data[:N//2]):
        okno = wartosc*(n/(N/2))
        wynik_tab.append(okno)
    
    for n, wartosc in enumerate(data[N//2:]):
        okno = wartosc*(3-((n+N)/(N/2)))
        wynik_tab.append(okno)
    
    return wynik_tab





N = 2048
fg = 10000
fs = 48000
delta_f = fs/N


butterworth_hz = []
butterworth_val = []

for hz in np.arange(0,fs/2, delta_f):
    butterworth_hz.append(hz)
    butterworth_val.append(butterworth(hz,fg,5))

for hz in np.arange(fs/2, fs, delta_f):
    butterworth_hz.append(hz)

butterworth_val += butterworth_val[::-1]

transformata = np.fft.ifft(butterworth_val)

okno_transformata = oknoTrojkatne(transformata)


_, axs = plt.subplots(2)
axs[0].plot(butterworth_hz,butterworth_val)
axs[1].plot(butterworth_hz,okno_transformata)
plt.show()

