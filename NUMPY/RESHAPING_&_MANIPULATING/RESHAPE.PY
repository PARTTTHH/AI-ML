"""
WHEN WE WANT TO RESHAPE OUR EXSISTING 1D ARRAY IT IS POSSIBILE WITH HELP OF 
        .reshape()   FUNCTION  THERE WE PASSES  (rows, columns)
"""

import numpy as np

arr = np.array([1,2,3,4,5,6])
re_shaped = arr.reshape(2,-1)
print(re_shaped)


"""KEEP IT MIND
RESHAPING DOES NOT CREATES A COPY OF OUR ORIGANAL ARRAY
ITS JUST CHANGE THE VIEW"""