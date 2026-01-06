"""
SPIT FUCNTION IN NUMPY USED TO SLIPT A LARGE OR BIG ARRAY INTO SMALL PARTS OR SMALL PICES
    THERE ARE THREE FUNCTIONS FOR SPITTING
            np.split()   THE STRICT CUTTER THIS FUNCTION DIVIDES LONG ARRAY INTO EQUAL SUB ARRAYS 6 INTO 3
            np.array_split()    THE FLEXIBLE CUTTER THIS WORK ALSO WITH WRONG CUTTER 5 INTO 2
            np.vsplit()     SPLITS ARRAY VERTICALLY ROW-WISE [TOP TO BOTTOM]
            np.hsplit()     SPLITS ARRAY HORUZONTALLY COLUMN-WISE [LEFT TO RIGTH]
            
"""

import numpy as np
arr = np.array([10,20,30,40,50,60])

print("np.split FUNC SPLITS ARR WITH 6 ELE INTO 3 EQUAL PARTS:-")
print(np.split(arr, 3))
print()

print("HERE np.array_split FUNC SPLITS SAME ARRAY INTO 4 PARTS:-")
print(np.array_split(arr, 4))
print()

arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print("2D ARRAY SPLIT WITH vsplit FUNCTION:-")
print(np.vsplit(arr_2d, 3))
print()

print("2D ARRAY SPLIT WITH hsplit FUNCTION:-")
print(np.hsplit(arr_2d, 3))
