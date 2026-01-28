"""
                    np.isinf(arr)
   THIS FUNCTION HELPS TO DETAICT INFINITE VALUES IN OUR ARRAY 
                    posinf = possitive infinite 
                    neginf = positive infinite
"""

import numpy as np

arr = np.array([1,2,3,np.inf,4,5,6,-np.inf])

print(np.isinf(arr))

cleaner_array = np.nan_to_num(arr, posinf=100, neginf=-100)
print(cleaner_array)