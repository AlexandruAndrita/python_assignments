import numpy as np


def matrix_stats(matrix: np.ndarray) -> dict:
    if matrix.ndim!=2:
        raise ValueError("The matrix is not 2D")
    total_sum=matrix.sum()
    row_sum=matrix.sum(axis=1)
    column_sum=matrix.sum(axis=0)
    statistics=dict()
    statistics['total_sum']=total_sum
    statistics['row_sums'] = row_sum
    statistics['column_sums'] = column_sum
    return statistics


