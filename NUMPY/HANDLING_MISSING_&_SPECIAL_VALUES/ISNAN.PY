"""
                        np.isnan(Arr)   nan = NOT A NUMBER
    
    THIS FUNCTION RETURNS A BOOLEAN ARRAY WHICH CONTAIN TRUE OR FALSE THEN TRUE MEANS 
    THAT IS A NOT A NUMBER VALUR OR MISSING VALUE AND FALISE MEANS THATS IS A REAL VALUE
"""

import numpy as np

arr = np.array([1,2,3,np.nan,4,5,np.nan])

print(np.isnan(arr))