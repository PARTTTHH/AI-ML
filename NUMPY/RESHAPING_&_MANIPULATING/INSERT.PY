"""
WHEN WE WANT TO INSAERT ELEMENTS IN THE ARRAY NUMPY PROVIDES 
        np.insert()   FUNCTION FOR IT 
        np.insert(arr, index, value, axis=0/1)
    arr = arr WHERE WE WANT TO INSERT THAT VALUE
    index = INDEX WHERE WANT TO INSERT THAT ELEMENT
    value = NEW VALUE
    axis = SAME 0 FOR INSERT ROW-WISE AND 1 FOR INSERT COLUMN-WISE
    IF WE DO axix=NONE IT WILL INSERT IN PLATIN VERSION OF ARR
"""

import numpy as np

print("ORIGNAL ARRAY")
arr = np.array([1,2,3,4,5])
print(arr)

print("ARRAY AFTER INSERTION")
new_arr = np.insert(arr, 3, 7, axis=0)
print(new_arr)
print()

"""
ALSO WE CAN DO SAME FOR MULTI DIAMENTIONAL ARRAYS
"""
print("ORIGNAL 2D ARRAY:-")
arr_2d = np.array([[1,2,3,4],[5,6,7,8]])
print(arr_2d)

print()
print("2D ARRAY AFTER INSERTION:-")
new_arr_2d = np.insert(arr_2d, 2, [9,10,11,12], axis=0)
print(new_arr_2d)
