import math
import cmath as cm
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile


def oknoProstokatne(data):
    return data

def oknoTrojkatne(data):    
    wynik_tab = []
    N = len(data)
    for n, wartosc in enumerate(data[:N//2]):
        okno = wartosc*(n/(N/2))
        wynik_tab.append(okno)
    
    for n, wartosc in enumerate(data[N//2:]):
        okno = wartosc*(2-((n+N)/(N/2)))
        wynik_tab.append(okno)

    return wynik_tab

def oknoHanninga(data):
    wynik_tab = []
    N = len(data)
    for n, wartosc in enumerate(data):
        okno = 1/2 - ((1/2)*math.cos(2*math.pi*(n/N)))
        okno = wartosc*okno
        wynik_tab.append(okno)

    return wynik_tab

def oknoHamminga(data):
    wynik_tab = []
    N = len(data)
    for n, wartosc in enumerate(data):
        okno = 0.54 - (0.46*math.cos(2*math.pi*(n/N)))
        okno = wartosc*okno
        wynik_tab.append(okno)

    return wynik_tab

def oknoBlackmana(data):
    wynik_tab = []
    N = len(data)
    for n, wartosc in enumerate(data):
        okno = 0.42 - (0.5*math.cos((2*math.pi*n)/(N-1))+0.08*((4*math.pi*n)/(N-1)))
        okno = wartosc*okno
        wynik_tab.append(okno)

    return wynik_tab



#ogranicza nagranie do 1s
def ograniczNagranie(data, fs):
    probki = int(1/(1/fs))
    return data[:probki]


def dtft(sygnal, f, fs):
    omega = 2*math.pi*f 
    ts = 1/fs
	
    wynik = 0

    for i, wartosc in enumerate(sygnal):
        wynik += wartosc*cm.exp( -1j*omega*i*ts)
		
    return wynik/len(sygnal)


samplerate, data = wavfile.read('Struna 1 - E.wav')

data = ograniczNagranie(data,samplerate)

dataProstokatne = oknoProstokatne(data)

dataTrojkatne = oknoTrojkatne(data)

dataHanning = oknoHanninga(data)

dataHamming = oknoHamminga(data)

dataBlackman = oknoBlackmana(data)


dataTab = [dataProstokatne,dataTrojkatne,dataHanning,dataHamming,dataBlackman]

fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5)

axisTab = [ax1,ax2,ax3,ax4,ax5]
colors = ['tab:blue','tab:red','tab:orange','tab:green', 'tab:cyan']

bhz = 300
ehz = 400
step = 1

samples = int(((ehz-bhz)//step)+1)

Hzarray = []
dBarray = []

for n, d in enumerate(dataTab):
    for i in np.linspace(bhz,ehz,samples,True):
        Hz = dtft(d,i,samplerate)
        Hz = abs(Hz)
        dB = 20*math.log10(Hz/np.iinfo(np.int16).max)
        Hzarray.append(i)
        dBarray.append(dB)
    axisTab[n].plot(Hzarray,dBarray,colors[n])
    Hzarray = []
    dBarray = []
    

ax1.set_title('Okno protokątne')

ax2.set_title('Okno Trójkątne')

ax3.set_title('Okno Hanninga')

ax4.set_title('Okno Hamminga')

ax5.set_title('Okno Blackmana')

plt.show()
