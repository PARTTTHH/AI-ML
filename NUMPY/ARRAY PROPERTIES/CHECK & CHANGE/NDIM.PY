# .ndim   RETURNS NUMBER OF DIAMENTIONS
    
import numpy as np

arr1d = np.array([1, 2, 3, 4])
arr2d = np.array([[1, 2, 3],[4, 5, 6]])
arr3d = np.array([[[1,2],[3,4],[4,5],[6,7]]])

print(arr1d.ndim)
print(arr2d.ndim)
print(arr3d.ndim)
