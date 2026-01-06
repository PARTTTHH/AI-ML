"""
STACKING MEANS JOINING TWO OR MORE ARRAYS TOGETHER TO FORM A LARGE ARRAY
THINK IT LIKE STACKING BOXES TOGETHER LIKE THAT 
FOR ARRAY STACKING NUMPY PROVIDES TWO FUNCTIONS
            np.vstack((arr1, arr2))     FOR VERTICALLY STACKING = ROW-WISE
            np.hstack((arr1, arr2))     FOR HORIZONTALLY STACKING = COLUMN-WISE
"""
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print("vstack VERTICALLY STACKKING:-")
print(np.vstack((arr1,arr2)))
print("hstack HORIZONTALLY STACKKING:-")
print(np.hstack((arr1,arr2)))

""" WE HAVE ONE MORE WHICH IS 
        np.stack()      FUNCTION    == ADDS A NEW DIAMENTION
    THIS FUNCTION JOINS THEM ALONG A NEW AXIS
        """
print("np.stack THIS FUNCTION ADDS NEW DIAMENTION:-")
print(np.stack((arr1, arr2)))

arr_2d_1 = np.array([[1,2,3],
                     [4,5,6]])
arr_2d_2 = np.array([[10,20,30],
                     [40,50,60]])
print("PASSING 2D ARRAYS TO np.stack TO GET 3D ARRAY")
print(np.stack((arr_2d_1,arr_2d_2)))