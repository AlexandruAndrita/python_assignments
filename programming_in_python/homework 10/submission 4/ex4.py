import numpy as np


def neighboring(matrix,rows,columns):
    for row in range(rows):
        for column in range(columns):
            if matrix[row,column]==-1:
                continue
            if row>0 and column>0 and matrix[row-1,column-1]==-1:
                matrix[row,column]+=1
            if row>0 and column<columns-1 and matrix[row-1,column+1]==-1:
                matrix[row,column]+=1
            if row<rows-1 and column>0 and matrix[row+1,column-1]==-1:
                matrix[row,column]+=1
            if row<rows-1 and column<columns-1 and matrix[row+1,column+1]==-1:
                matrix[row,column]+=1
            if row>0 and matrix[row-1,column]==-1:
                matrix[row,column]+=1
            if row<rows-1 and matrix[row+1,column]==-1:
                matrix[row,column]+=1
            if column>0 and matrix[row,column-1]==-1:
                matrix[row,column]+=1
            if column<columns-1 and matrix[row,column+1]==-1:
                matrix[row,column]+=1

def create_minefield(rows: int, cols: int, n_mines: int, seed=None) -> np.ndarray:
    rng=np.random.default_rng(seed=seed)

    if rows<2:
        raise ValueError(f"Number of rows {rows} is smaller than 2")
    if cols<2:
        raise ValueError(f"Number of columns {cols} is smaller than 2")
    if n_mines<1 or n_mines>=rows*cols:
        raise ValueError(f"Number of mines: {n_mines} is not correctly introduced")

    matrix=np.zeros((rows,cols))
    matrix=matrix.astype(int)
    while n_mines:
        position=rng.integers(low=0,high=rows*cols-1,size=1)[0]
        i=position//rows
        j=position%rows
        if matrix[i,j]!=-1:
            matrix[i,j]=-1
            n_mines-=1

    neighboring(matrix,rows,cols)

    #assert np.count_nonzero(matrix==-1)==tmp_n_mines
    #print(np.count_nonzero(matrix==-1))

    return matrix

