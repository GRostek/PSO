import math
import scipy
import numpy as np
from matplotlib import pyplot as plt


def get_dB(data):
    p = sum([val**2 for val in data])/len(data)
    p=abs(p)
    return 10*math.log10(p)


def get_thd(data):
    fft_abs = abs(data)

    sequence_sum = 0
    for x in fft_abs:
        sequence_sum+=(x**2)

    #for i in range(0,24):
    #    sequence_sum+=(fft_abs[i]**2)

    sequence_harmonic = sequence_sum -(max(fft_abs))**2.0
    thd = sequence_harmonic**0.5 / max(fft_abs)
    return thd * 100

def get_delta_f(f,fs,windows, data):
    N = ((1/f)*windows)/(1/fs)
    return fs/N


def get_quanatized_signal(signal):
    quantized_signal = []
    bit=8
    w= 1/(2**(bit-1))
    fs=48000
    for x in signal[:fs]:
        sign = x/abs(x) if x != 0 else 0
        quantized_signal.append((int(x*(2**(bit-1)))+sign)*w)
    return quantized_signal


def get_harmonics(f0, fn):
    time = np.arange(0,10,1/48000)
    signal = []
    T=1/f0
    for n in np.arange(f0,fn,f0):
        signal.append(np.sin(2*np.pi*n*time*T))
    
    quantized_signal = []
    for s in signal:
        quantized_signal.append(get_quanatized_signal(s))

    harmonic_fft = []
    for s in quantized_signal:
        harmonic_fft.append(np.abs(np.fft.rfft(s,n=480)))

    return harmonic_fft


def get_thd_2(harmonics):
    first_harmonic = 0
    for s in harmonics[0]:
        first_harmonic+=s**2

    sum_harmonics = 0
    for s in harmonics:
        for val in s:
            sum_harmonics+=val**2
    sum_harmonics-=first_harmonic
    return (sum_harmonics/first_harmonic)

def get_thd_3(harmonics,f0,fs,step):
    first_harmonic = harmonics[0][int(get_delta_f(f0,fs,10,harmonics[0]))]**2

    sum_harmonics=0
    f=f0
    for s in harmonics:
        sum_harmonics+=s[int(get_delta_f(f,fs,10,s))]**2
        f+=step
    sum_harmonics-=first_harmonic
    return sum_harmonics/first_harmonic

def get_thd_4(fft, f0,fs,step,delta_f):
    
    sum_harmonic=0
    for s in np.arange(f0,fs,step):
        n=s/delta_f
        sum_harmonic+=10*math.log10(fft[int(n)]**2)
    first_harmonic = 10*math.log10(fft[int(f0/delta_f)]**2)
    sum_harmonic-=first_harmonic
    return (sum_harmonic/first_harmonic)*100




f0 = 1000
fs = 48000

#print(get_thd_2(get_harmonics(1000,24000)))
#print(get_thd_3(get_harmonics(1000,24000),f0,fs,1000))

T = 1/f0
Ts = 1/fs

N = (T*10)/Ts


time = np.arange(0, 10, 1/fs)
signal = np.sin(2*np.pi*f0*time*T)

dB_before = get_dB(signal)

quantized_signal = get_quanatized_signal(signal)

spectrum = np.fft.fft(quantized_signal)

rspectrum = np.fft.rfft(quantized_signal)

print(get_thd_4(abs(rspectrum),f0,24000,f0,get_delta_f(f0,fs,1,quantized_signal)))


dB_after = get_dB(quantized_signal)
print("dB przed skwantowaniem: "+str(dB_before))
print("dB po skwantowaniu: "+str(dB_after))
difference = abs(dB_before-dB_after)
print("różnica w dB: "+str(difference))

print("THD: "+str(get_thd(np.fft.rfft(quantized_signal)))+"%")
fig,axs = plt.subplots(3)

#print(get_delta_f(2000,48000,10,quantized_signal))

axs[0].plot(time,signal)
axs[0].set_title("Sygnał")
axs[1].plot(quantized_signal)
axs[1].set_title("Skwantywikowany sygnał")
axs[2].plot(np.abs(spectrum))
axs[2].set_title("Widmo amplitudowe")
plt.show()








#def get_thd(f0,fn):
#    total_harmonic = 0
#    for n in np.arange(f0,fn,1000):
#        T=1/f0
#        time = np.arange(0, 10, (n/1000)/fs)
#        signal = np.sin(2*np.pi*n*time*T)
#        fft = np.fft.rfft(get_quanatized_signal(signal))
#        total_harmonic+= get_harmonic(fft)
#    return total_harmonic * 100