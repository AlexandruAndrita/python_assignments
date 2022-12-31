import os


class Reader:
    def __init__(self,path: str):
        if not os.path.isfile(path):
            raise ValueError("path is not a file")
        self.path=open(path,"rb")

    def close(self):
        self.path.close()

    def __len__(self):
        self.path.seek(0,os.SEEK_END)
        size=self.path.tell()
        return size

    def __getitem__(self, key):
        if not isinstance(key,int):
            raise TypeError(f"indexing expects 'int', not '{type(key).__name__}'")
        if key>len(self):
            raise IndexError("Reader index out of range")
        if key==0:
            pos=self.path.seek(key, os.SEEK_SET)
            pos+=1
            return self.path.read(pos)
        elif key>0:
            pos=self.path.seek(key,os.SEEK_SET)
            return self.path.read(pos)
        elif key<0:
            pos=self.path.seek(key,os.SEEK_END)
            return self.path.read(pos)

