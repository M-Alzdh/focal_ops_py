import numpy as np

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
    

random_array = np.array(np.random.random_integers(0, 100, size = (4,5)))

print(random_array)

focal_ops(random_array)


