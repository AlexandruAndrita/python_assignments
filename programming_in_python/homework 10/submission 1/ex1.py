import random
import sys
import numpy as np


def extend(arr: np.ndarray, size:int, fill=None) -> np.ndarray:
    #original_array=np.copy(arr)

    if arr.ndim!=1:
        raise ValueError("The array given is not 1D")
    if size<arr.size:
        raise ValueError(f"Size {size} is smaller than the length {arr.size} of the array")
    nr_new_elements=abs(arr.size-size)
    new_array=np.copy(arr)
    if nr_new_elements==0:
        return new_array
    elif nr_new_elements!=0:
        if fill is None:
            while nr_new_elements:
                number=random.randint(-sys.maxsize-1,sys.maxsize)
                new_array=np.append(new_array,number)
                nr_new_elements-=1
        elif isinstance(fill,int):
            while nr_new_elements:
                new_array=np.append(new_array,fill)
                nr_new_elements-=1
        elif fill=="mean":
            if np.issubdtype(arr.dtype, np.number):
                mean_value=np.mean(arr,dtype=arr.dtype)
                while nr_new_elements:
                    new_array=np.append(new_array,mean_value)
                    nr_new_elements-=1
            else:
                while nr_new_elements:
                    new_array=np.append(new_array,"mean")
                    nr_new_elements-=1

    #assert np.array_equal(arr,original_array)==True

    return new_array
