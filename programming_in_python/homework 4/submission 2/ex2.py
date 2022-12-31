def clip(*values, min_=0, max_=1) -> list:
    if len(values)==0:
        return []

    new_list=[]
    for i in values:
        if i<min_:
            new_list.append(min_)
        elif i>max_:
            new_list.append(max_)
        else:
            new_list.append(i)
    return new_list


print("clip() = {}".format(clip()))
print("clip(1,2,0.1,0) = {}".format(clip(1,2,0.1,0)))
print("clip(-1,0.5) = {}".format(clip(-1,0.5)))
print("clip(-1, 0.5, min_=-2) = {}".format(clip(-1, 0.5, min_=-2)))
print("clip(-1, 0.5, max_=0.3) = {}".format(clip(-1, 0.5, max_=0.3)))
print("clip(-1, 0.5, min_=2, max_=3) = {}".format(clip(-1, 0.5, min_=2, max_=3)))