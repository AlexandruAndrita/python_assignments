import dill as pkl
import matplotlib.pyplot as plt
import os
import numpy as np


def plot_eval_metrics(data: dict, save_path: str=None):
    it=1
    value=len(data)
    medianprops=dict(color="black")
    for key in data:
        values=data[key]["values"]
        labels=data[key]["labels"]
        cmap=plt.get_cmap(name="Set2")
        plt.subplot(1,value,it)
        # array=np.random.uniform(low=0,high=1,size=len(labels))
        # boxprops=dict(color=cmap(array))

        plt.boxplot(values,vert=True,patch_artist=True,medianprops=medianprops,labels=labels)
        plt.title(key)
        plt.grid(axis="y")
        plt.tight_layout(pad=1.0,w_pad=0.5,h_pad=1.0)
        it+=1
    if save_path is not None:
        plt.savefig(os.path.join(save_path,"box_plots.png"))

    plt.show()


