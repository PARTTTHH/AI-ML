"""
                        np.nan_to_num(arr, nan=, posinf=, neginf=)          
BY DEFAULT NAN VALUE GET 0 
"""
import numpy as np

arr = np.array([1,2,3,np.nan,4,5,np.nan])

cleaner_arr = np.nan_to_num(arr, nan=100)   

print(cleaner_arr)