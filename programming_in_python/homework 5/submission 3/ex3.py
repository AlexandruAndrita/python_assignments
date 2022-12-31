def binary_search(elements: list,x) -> bool:
    if len(elements)==0:
        return False
    if len(elements)==1 and elements[len(elements)-1]!=x:
        return False
    if elements[len(elements)//2]==x:
        return True
    try:
        if elements[len(elements)//2]<x:
            return binary_search(elements[len(elements)//2:],x)
        else:
            return binary_search(elements[:len(elements)//2], x)
    except TypeError:
        return False
