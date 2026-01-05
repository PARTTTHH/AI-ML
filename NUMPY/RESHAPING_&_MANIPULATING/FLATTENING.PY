"""
WHEN WE WANT TO RESHAPE OUR MULTI-DIAMENTIONAL ARRAY INTO 1D ARRAY
NUMPY PRIVIDES TWO FUNCTION TO ACHIVE THAT 
    np.ravel()    ->  THIS FUNCTION JUST CHANGES THE VIEW OF ARRAY SAME LIKE reshape() MEANS ORINAL ARRAY AFFECTS
    np.flatten()  -> THIS FUNCTION IS CREATES A COPY OF ORINAL AND ALSO ALLOWS TO MAKE CHNAGES    DOES NOT AFFECTS ORIGANL ONE
"""

import numpy as np

arr_2d = np.array([[1,2,3],
                   [4,5,6]])
print(arr_2d.ravel())

new_arr = arr_2d.flatten()
print(new_arr + 2)
