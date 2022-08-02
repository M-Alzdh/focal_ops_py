import numpy as np


def check_fun(x):
    if not isinstance(x, (np.ndarray)):
        raise TypeError('input should be a numpy.ndarray')

    else:
        print('gtg')

#print(isinstance(random_array, (np.ndarray)))

#check_fun(random_array)
#check_fun([1, 2, 3])


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

random_array = np.array(np.random.randint(0, 10, size = (12, 12)))

print(input_check(random_array, check_divisibility=True, divisible_by=(5, 3)))


