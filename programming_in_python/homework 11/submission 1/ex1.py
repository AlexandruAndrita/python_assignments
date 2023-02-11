import matplotlib.pyplot as plt
import numpy as np
import os


def plot_lifts(data: dict, save_path: str = None):
    it=1
    value=len(data)
    for key in data:
        labels=np.arange(1,len(data[key])+1,1)
        labels=labels.astype(str)
        plt.subplot(value,1,it)
        plt.ylabel("kg")
        plt.grid(axis="y")
        plt.title(key)
        plt.tight_layout(pad=1.0)
        plt.bar(labels,data[key])
        it+=1
    if save_path is not None:
        plt.savefig(os.path.join(save_path,'lifts_plot.png'))
    plt.show()

