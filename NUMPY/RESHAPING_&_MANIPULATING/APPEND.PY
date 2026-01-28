"""
        np.append()       FUNCTION FOR INSERT A VALUE AT END OF ARRAY
                np.append(arr_here, value)
"""

import numpy as np

arr = np.array([1,2,3,4,5])

new_arr = np.append(arr, [6,7,8,9,10])
print(new_arr)