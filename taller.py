import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.signal import welch

signal = loadmat('r01_edfm (1).mat')

senal = signal['val']

print(senal.shape)

time = np.arange(5000)

plt.plot(time,senal[0,0:5000])
plt.plot(time,senal[1,0:5000]+2500)
plt.legend(['Electrodo 1', 'Electrodo 2'])
plt.show()

# np.sin()