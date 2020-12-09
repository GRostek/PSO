import math
import numpy as np
from matplotlib import pyplot as plt
import fir
import iir

import scipy as sc
import scipy.signal


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


# FIR

transformata = np.fft.ifft(butterworth_val)

wspolczynniki_fir = oknoTrojkatne(transformata)

#system FIR tworzę za pomocą implementacji FIR, którą udostępnił nam Pan przy zadaniu 2 (laboratorium 3)

system_fir = fir.systemFIR(wspolczynniki_fir)


# IIR

b, a = sc.signal.butter(5, fg, fs=fs)

#podobnie jak wcześniej, implementację systemu IIR wziąłem z zadania 2
system_iir = iir.systemIIR(a,b)





_, axs = plt.subplots(2)
axs[0].plot(butterworth_hz,butterworth_val)
axs[0].set_title('charakterystyka czestotliwosciowa')
axs[1].plot(butterworth_hz,wspolczynniki_fir)
axs[1].set_title('wspolczynniki fir')
plt.show()