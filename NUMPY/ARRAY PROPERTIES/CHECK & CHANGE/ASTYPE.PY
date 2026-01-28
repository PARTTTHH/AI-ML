# .astype(new type here)
    
import numpy as np

arr = np.array([2.3, 4.6, 3.9, 7.2])
print(arr.dtype)
int_arr = arr.astype(int)

print(int_arr)
print(int_arr.dtype)

age = np.array(['19'])
print(age.astype(int)) 