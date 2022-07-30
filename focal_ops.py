from locale import windows_locale

import numpy as np


def focal_ops(x, op_function = 'mean', window_size = 3):
    '''performs focal operations'''
    
    shape = np.shape(x)
    new_array = np.zeros(shape = shape)

    functions = {
        'mean' : np.mean, 
        'median' : np.median, 
        'max' : np.max, 
        'min' : np.min, 
        'range' : lambda x: np.max(x)- np.min(x)
    }

    num_neighbor = int((window_size-1)/2)

    for i in range(shape[0]):
        for j in range(shape[1]):

            indx = [i, j]
            
            left = max(0, indx[0]-num_neighbor)
            right = max(0, indx[0]+num_neighbor+1)

            bottom = max(0,indx[1]-num_neighbor)
            top = max(0,indx[1]+num_neighbor+1)

            selection = x[left:right, bottom:top]
            value = np.round(functions[op_function](selection), 4)

            new_array[indx[0], indx[1]] = value
    print(new_array)
    return(new_array)
    

random_array = np.array(np.random.randint(0, 5, size = (6,6)))

#focal_ops(random_array, window_size=3, op_function='mean')

## aggregate

def aggregate(x, aggregation_factor = 3):
    shape = np.shape(x)
    new_shape = (shape[0]/3, shape[1]/3)
    aggregated_mtrx = np.zeros((int(new_shape[0]), int(new_shape[1])))
    print(aggregated_mtrx)

aggregate(random_array)


