import os


def chunks(path: str,size: int, **kwargs):
    if os.path.isfile(path) is False:
        raise ValueError("path is not a file. A file should be provided")
    if size<1:
        raise ValueError("size should be greater or equal to 1")
    file=open(path,**kwargs)
    chunks_list=[]
    while True:
        line=file.read(size)
        if not line:
            break
        chunks_list.append(line)
    file.close()
    return chunks_list


"""
for i, c in enumerate(chunks("ex1_data.txt", 25, mode="rb")):
    print(f"Chunk {i} = {c}")
"""