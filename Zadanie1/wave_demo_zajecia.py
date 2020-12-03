import matplotlib.pyplot as plt

from scipy.io import wavfile
samplerate, data = wavfile.read('Struna 6 - E.wav') #Plik mono!!!!!


print ("Częstotliwość próbkowania ......... " + str(samplerate) + " Hz")
print ("Liczba próbek ..................... " + str(len(data)))

okres_probkowania = 1 / samplerate

print ("Okres próbkowania ................. " + str(okres_probkowania) + " s")

czas_trwania_nagrania = len(data) * okres_probkowania

print ("Czas trwania nagrania ............. " + str(czas_trwania_nagrania) + " s")


data_x = range(len(data))

plt.plot(data_x, data)

plt.show()

ile_przesunac = float(input("O ile czasu przesunąć sygnał? "))

liczba_probek = ile_przesunac/okres_probkowania

print("Aby przesunąć sygnał o czas " + str(ile_przesunac) + "należy wstawić" + str(liczba_probek) + " probek")


