"""
WHEN WE WANT TO DELETE AN ELEMENT FROM ARRAY NUMPY PROVIDES 
DELETE FUNCTION FOR IT
            np.delete(arr, index)
ITS CREATES A COPY MENS ORIGINAL ONES IS STAY AS IT IS
"""

import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr)

new_arr = np.delete(arr, 2)
print(new_arr)


print(arr)      #ORIGINAL ONE STAYS AS IT IS