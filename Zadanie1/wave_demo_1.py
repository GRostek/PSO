import matplotlib.pyplot as plt

from scipy.io import wavfile
samplerate, data = wavfile.read('Struna 6 - E.wav') #Plik mono!!!!!

from scipy.io.wavfile import write


print ("Częstotliwość próbkowania ......... " + str(samplerate))
print ("Liczba próbek ..................... " + str(len(data)))

data_x = range(len(data))

plt.plot(data_x, data)

plt.show()



