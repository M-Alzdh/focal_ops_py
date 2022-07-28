from ctypes import resize
import math as m
import random as rnd
from statistics import mean
import numpy as np

random_numbers = np.empty(16)

for i in range(len(random_numbers)):
    random_numbers[i] = rnd.randint(1, 10)

random_numbers.shape = (4,4)

h_pad = np.zeros(shape=(1, 4))

#print(h_pad)

h_padded = np.vstack((h_pad, random_numbers, h_pad))



v_pad = np.zeros(shape = (6, 1))

hv_padded = np.hstack((v_pad, h_padded, v_pad))

"""
indx = [1, 1]

num_neighbor = 1

left = max(0, indx[0]-num_neighbor)
right = max(0, indx[0]+num_neighbor+1)

bottom = max(0,indx[1]-num_neighbor)
top = max(0,indx[1]+num_neighbor+1)

selection = hv_padded[left:right, bottom:top]

print(selection)

print(np.mean(selection))
print(selection[indx[0], indx[1]])

"""

new_array = np.empty(shape=(6, 6))

for i in range(hv_padded.shape[0]):
    for j in range(hv_padded.shape[1]):
        indx = [i, j]
        num_neighbor = 1
        left = max(0, indx[0]-num_neighbor)
        right = max(0, indx[0]+num_neighbor+1)

        bottom = max(0,indx[1]-num_neighbor)
        top = max(0,indx[1]+num_neighbor+1)
        selection = hv_padded[left:right, bottom:top]
        value = np.round(np.mean(selection), 2)
        new_array[indx[0], indx[1]] = value

print(hv_padded)
print(new_array)


def focal_ops(x, op_function = 'mean'):
    #performs focal operations

    shape = np.shape(x)
    new_array = np.zeros(shape = shape)

    functions = {
        'mean' : np.mean, 
        'median' : np.median, 
        'max' : np.max, 
        'min' : np.min
    }

    for i in range(shape[0]):
        for j in range(shape[1]):

            indx = [i, j]
            num_neighbor = 1

            left = max(0, indx[0]-num_neighbor)
            right = max(0, indx[0]+num_neighbor+1)

            bottom = max(0,indx[1]-num_neighbor)
            top = max(0,indx[1]+num_neighbor+1)

            selection = x[left:right, bottom:top]
            value = np.round(functions[op_function](selection), 2)

            new_array[indx[0], indx[1]] = value
    print(new_array)
    return(new_array)
    

focal_ops(hv_padded, op_function='max')

