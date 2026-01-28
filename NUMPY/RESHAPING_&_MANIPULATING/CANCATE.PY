"""
WHEN WE WANT TO JOIN OR ADD TWO OR MORE ARRAYS TOGETHER 
                np.concatenate()   
                np.cancatenate((arr1, arr2), axis=0/1)    WE PASS ARRAYS IN TUPLE 
axis = 0  -> VERTICLKE STACKING
axis = 1  -> HORIZONTAL STACKING
"""

import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

new_arr = np.concatenate((arr1, arr2),axis=0)
print(new_arr)