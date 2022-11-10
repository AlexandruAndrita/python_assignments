def swap_elements(a,b):
    aux=a
    a=b
    b=aux
    return a,b


def is_sorted(elements:list,ascending:bool) -> bool:
    for i in range(len(elements)-1):
        if ascending==True and elements[i]>elements[i+1]:
            return False
        elif ascending==False and elements[i]<elements[i+1]:
            return False
    return True


def sort(elements: list, ascending: bool = True):
    length=len(elements)
    while is_sorted(elements,ascending)==False:
        index=0
        while index<length-1:
            if ascending==True and elements[index]>elements[index+1]:
                elements[index],elements[index+1]=swap_elements(elements[index],elements[index+1])
            elif ascending==False and elements[index]<elements[index+1]:
                elements[index+1],elements[index]=swap_elements(elements[index+1],elements[index])
            index+=1
        length-=1


some_list = [1, 3, 0, 4, 5]
sort(some_list)
print("sort(some_list) -> some_list = {}".format(some_list))
some_list = [1, 3, 0, 4, 5]
sort(some_list,ascending=False)
print("sort(some_list, ascending=False) -> some_list = {}".format(some_list))


#just another example to test the sorting method
print()
some_list = [5,6,3,2,1,4,9,8,10,44,23,100,69]
sort(some_list)
print("sort(some_list) -> some_list = {}".format(some_list))
some_list = [5,6,3,2,1,4,8,9,10,44,23,100,69]
sort(some_list,ascending=False)
print("sort(some_list, ascending=False) -> some_list = {}".format(some_list))