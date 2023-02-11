import os
import numpy as np
import matplotlib.pyplot as plt


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

def plot_classes(data: dict, save_path: str=None):
    for key in data:
        x_data=data[key][:,0]
        y_data=data[key][:,1]
        plt.scatter(x_data,y_data,edgecolors='k',label=key)
    plt.title(f"2D data showing {len(data)} classes")
    plt.legend()

    if save_path is not None:
        plt.savefig(os.path.join(save_path,'scatter_plot_classes.png'))

    plt.show()
