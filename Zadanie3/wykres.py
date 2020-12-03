import matplotlib.pyplot as plt
import math
import numpy as np


w = 0.1
w0 = 10

wtab = []
ftab = []


while (w<(w0*20)):
    tmp = (1/(((w**2)*(w0**2))+(w**4))) * math.sqrt((w**2)*(w0**4) + (w0**2)*(w**4))
    wtab.append(w)
    ftab.append(tmp)
    w+= 1





plt.plot(wtab,ftab, 'c')
plt.ylabel('widmo')
plt.xlabel('w')
plt.show()