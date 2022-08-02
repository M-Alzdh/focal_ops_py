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
    

random_array = np.array(np.random.randint(0, 10, size = (20, 10)))

#focal_ops(random_array, window_size=3, op_function='mean')


## aggregation 

def aggregate(x, aggregation_factor = (2, 2), aggregation_function = 'mean'):
    row_agg_fact = aggregation_factor[0]
    col_agg_fact = aggregation_factor[1]
    shape = np.shape(x)
    new_shape = (int(shape[0]/row_agg_fact), int(shape[1]/col_agg_fact))
    aggregate_mtrx = np.empty(new_shape)

    functions = {
        'mean' : np.mean, 
        'median' : np.median 
    }
        
    for i in range(0, new_shape[0]):
        for j in range(0, new_shape[1]):

            top = i * row_agg_fact
            bottom = (i*row_agg_fact) + row_agg_fact

            left = j * col_agg_fact
            right = (j * col_agg_fact) + col_agg_fact
            
            selection = x[top:bottom, left:right]
            
            aggregate_mtrx[i, j] = functions[aggregation_function](selection)

    print(aggregate_mtrx)
    return(aggregate_mtrx)
    

aggregate(random_array, aggregation_factor=(1,1), aggregation_function='mean')

## down scaling + smoothing
