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
    

random_array = np.array(np.random.randint(0, 10, size = (9,9)))

#focal_ops(random_array, window_size=3, op_function='mean')

## aggregation 

def aggregate(x, aggregation_factor = 2):
    shape = np.shape(x)
    new_shape = (int(shape[0]/aggregation_factor), int(shape[1]/aggregation_factor))
    means = []
    row_index = [0]
    row_index.extend(list(range(aggregation_factor, shape[0], aggregation_factor)))
    col_index = [0]
    col_index.extend(list(range(aggregation_factor, shape[1], aggregation_factor)))
    
    for i in row_index:
        for j in col_index:
            top = i
            bottom = i+aggregation_factor

            left = j
            right = j+aggregation_factor
            
            selection = x[top:bottom, left:right]
            mean = np.mean(selection)
            means.append(mean)
    aggregate_mtrx = np.array(means).reshape(new_shape)
    print(aggregate_mtrx)

    return(aggregate_mtrx)
    

aggregate(random_array, aggregation_factor=3)

