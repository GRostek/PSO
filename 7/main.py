from virtual_space import virtual_space
from audio_source import audio_source
import numpy as np

from scipy.io import wavfile
from scipy.io.wavfile import write


def get_remaining_delay(left, right):
    return abs(left - right)


#TODO
# zmień wszystkie operacje tablicowe na numpy + float16
# przenieś wszystko do virtual_space
# zmień na plik mono
# oblicz decybele
# profit


samplerate, data = wavfile.read('Cat-Meow.wav')

data_left = data[:, 0]
data_right = data[:, 1]

space = virtual_space(100,100,10,10,0.24)

source = audio_source(60,60)


#przenies to pozniej do klasy

print(space.get_distance_from_listener(source))

left, right = space.get_distance_from_listener(source)

left, right = space.get_time(left,right)

#opozninie dla lewego i prawego kanalu
left_delay = int(samplerate*left)
right_delay = int(samplerate*right)

print(left_delay)


#inicjacja lewego i prawego kanalu
delay_left = []
delay_right = []

#dodanie opoznienia na poczatku
delay_left[0:] = [0] * left_delay
delay_right[0:] = [0] * right_delay

#dodanie reszty
delay_left[left_delay:] = data_left
delay_right[right_delay:] = data_right



#wyrównanie
if(left_delay > right_delay):
    delay_right[len(delay_right):] = [0] * get_remaining_delay(left_delay,right_delay)
elif(right_delay > left_delay):
    delay_left[len(delay_left):] = [0] * get_remaining_delay(left_delay,right_delay)


write_data = np.array([delay_left, delay_right]).T



write("wynik.wav", samplerate, write_data)



