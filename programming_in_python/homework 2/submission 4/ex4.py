start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

odd_counter, even_sum = 0, 0
length = len(range(start, stop, step))

if length == 1:
    if start % 2 == 0:
        even_sum = start
    elif start % 2 == 1:
        odd_counter = 1
    print(f"Last value in range = {start}\nodd_counter = {odd_counter}\neven_sum = {even_sum}")
else:
    count = 0
    for i in range(start, stop, step):
        count += 1
        if count == 2:
            print(f"2nd value in range = {i}")
        if i + step >= stop:
            print(f"Last value in range = {i}")
        if i % 2 == 0:
            even_sum += i
        elif i % 2 == 1:
            odd_counter += 1
    print(f"odd_counter = {odd_counter}\neven_sum = {even_sum}")
