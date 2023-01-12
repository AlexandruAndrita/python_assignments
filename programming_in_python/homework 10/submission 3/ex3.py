import numpy as np


def create_data(setups: list[dict], seed=None) -> dict:
    np.random.seed(seed=seed)
    randomized_arrays=dict()
    for dictionary in setups:
        new_array_id=dictionary["id"]
        new_array_dimension=dictionary["n"]
        new_array_lower_bound=dictionary["a"]
        new_array_upper_bound=dictionary["b"]

        randomized_array=np.random.uniform(low=new_array_lower_bound,high=new_array_upper_bound,size=new_array_dimension)
        randomized_arrays[new_array_id]=randomized_array

    return randomized_arrays

