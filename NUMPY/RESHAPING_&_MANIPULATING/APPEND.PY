"""WHEN WE WANT TO INSERT A VALUE AT END OF THE ARRAY 
NUMPY PROVIDE A FUNCTION FOR IT SAME LIKE LIST APPEND
WE HAVE         np.append()       FUNCTION FOR INSERT A VALUE AT END OF ARRAY
                np.append(arr_here, value)
        arr_here = ARR WHERE WE WANT TO PERFORM THIS INSERT
        value =  VALUE THAT WE WANTED TO APPEND
"""

import numpy as np

arr = np.array([1,2,3,4,5])

new_arr = np.append(arr, [6,7,8,9,10])
print(new_arr)