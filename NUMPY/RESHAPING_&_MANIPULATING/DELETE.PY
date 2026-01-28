"""
DELETE FUNCTION FOR IT
            np.delete(arr, index)
ITS CREATES A COPY MENS ORIGINAL ONES IS STAY AS IT IS
"""

import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr)

new_arr = np.delete(arr, 2)
print(new_arr)
print()


print("ALSO WE DO THIS SAME FOR 2D OR MULTI DIAMENTIONAL ARRAYS")
arr_2d = np.array([[1,2,3],
                   [4,5,6]])
print(arr_2d)
new_2d_arr = np.delete(arr_2d, 0, axis=0)
print(new_2d_arr)