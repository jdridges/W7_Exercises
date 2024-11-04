import numpy as np

# veg = ['cucumber', 'celery', 'avacado', 'kale']

# array_veg = np.array(veg)
# print(array_veg)
# print(type(array_veg))  #class is numpy.ndarray --- an array!

#the name of the array object in Numpy is ndarray
## to create an ndarray object, the array() function is used
        # Any array-object such as a list, tuple, etc. can be passed to the array() function

# veg = ['cucumber', 'celery', 'avacado', 'kale']
# array_veg = np.array(veg)

# prices = (1, 2, 3, 4.99)
# array_price = np.array(prices)

# print(array_veg)
# print(array_price)
# print(type(array_price))        #These are all ONE- demensional arrays so far


# veg = [('cucumber', 'celery'), ('avacado', 'kale')]     #TWO demensional array - nested tuple
# array_veg = np.array(veg)

# prices = ()
# array_price = np.array(prices)
# print(array_veg)
# print(array_price)
# print(type(array_price))

# arr0 = np.array(1)      #0 dimensional array
# arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])      #3 demensional array

# print(arr0)
# print(arr3d)    #this output looks very interesting
# print(arr3d.ndim)   #.ndim returns the dimensions
# print(arr3d.size)   #.size returns total number of elements in array
# print(arr3d.shape)  #.shape returns a tuple with the size of each dimension, listed outermost to innermost
# print(arr3d.T)      #transposes dimensions

array2d = np.array([[1, 2], [3, 4], [5, 6]])
print(array2d[0][0])
print(array2d.shape)
print(array2d.T[0][0])
print(array2d.T.shape)