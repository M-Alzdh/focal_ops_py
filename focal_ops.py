from ctypes import resize
import math as m
import random as rnd
import numpy as np

random_numbers = np.empty(16)

for i in range(len(random_numbers)):
    random_numbers[i] = rnd.randint(1, 10)

random_numbers.shape = (4,4)

h_pad = np.zeros(shape=(1, 4))

#print(h_pad)

h_padded = np.vstack((h_pad, random_numbers, h_pad))

print(h_padded)

v_pad = np.zeros(shape = (6, 1))

hv_padded = np.hstack((v_pad, h_padded, v_pad))
