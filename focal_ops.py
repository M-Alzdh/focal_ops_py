from dis import dis
from locale import windows_locale

import numpy as np

def input_check (x, check_divisibility = False, divisible_by = ()): 
    shape = np.shape(x)

    if not isinstance(x, (np.ndarray)):
        raise TypeError('input should be a numpy.ndarray')

    if not np.ndim(x) == 2:
        raise Exception('input should be a two-dimensional numpy.ndarray')

    if check_divisibility:
        if not shape[0] % divisible_by[0] == 0 or not shape[1] % divisible_by[1] == 0:
            raise Exception("the length of at least one of the input's is not divisible by the respective aggregation factor")
    
    return(True) 


def focal_ops(x, op_function = 'mean', window_size = 3):
    '''performs focal operations'''

    while input_check(x):
        
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
    

random_array = np.array(np.random.randint(0, 10, size = (4, 4)))

#focal_ops(random_array, window_size=3, op_function='mean')


## aggregation 

def aggregate(x, aggregation_factor = (2, 2), aggregation_function = 'mean'):
    row_agg_fact = aggregation_factor[0]
    col_agg_fact = aggregation_factor[1]
    shape = np.shape(x)

    while input_check(x, check_divisibility = True , divisible_by = aggregation_factor):

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
    

## down scaling

def disaggregate(x, disaggregation_factor = ()):
    row_dis_agg_fact = disaggregation_factor[0]
    col_dis_agg_fact = disaggregation_factor[1]
    shape = np.shape(x)
    new_shape = (int(shape[0]*row_dis_agg_fact), int(shape[1]*col_dis_agg_fact))
    while input_check(x): 
        disaggregated_mtrx = np.zeros(shape = new_shape)
        for i in range(0, shape[0]):
            for j in range(0, shape[1]):
                value_in_x = float(x[i, j])
                top = i*row_dis_agg_fact
                bottom = (i*row_dis_agg_fact)+row_dis_agg_fact
                left = j*col_dis_agg_fact
                right = (j*col_dis_agg_fact)+col_dis_agg_fact
                disaggregated_mtrx[top:bottom, left:right] = value_in_x
        print(disaggregated_mtrx)
        return(disaggregated_mtrx)
print(random_array)

disaggregate(random_array, disaggregation_factor=(3, 3))
    


