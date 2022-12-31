fnames = ["file7.txt",  "file3.txt", "file2.txt",
          "file7.txt", "file1.txt", "file3.txt", "file4.png",
          "file4.png", "file5.txt", "file0.txt", "file7.dat"]

files = list()

for i in fnames:
    if i.endswith(".txt"):
        ok = 1
        for j in files:
            if i == j:
                ok = 0
        if ok == 1:
            files.append(i)

files.sort()
print(files)

