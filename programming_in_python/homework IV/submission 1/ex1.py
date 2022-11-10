def fib(n: int)-> int:
    if n<0:
        return -1
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    x0,x1,count,new_element=0,1,2,-1
    while count<=n:
        new_element=x0+x1
        x0=x1
        x1=new_element
        count+=1
    return new_element


print("fib(0) = {}".format(fib(0)))
print("fib(1) = {}".format(fib(1)))
print("fib(2) = {}".format(fib(2)))
print("fib(3) = {}".format(fib(3)))
print("fib(7) = {}".format(fib(7)))
print("fib(-2) = {}".format(fib(-2)))

