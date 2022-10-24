my_string = input("Enter string: ")
my_string = my_string.lower()

dictionary = dict()

for i in range(len(my_string)):
    if my_string[i] not in dictionary:
        dictionary[my_string[i]] = 1
    else:
        dictionary[my_string[i]] += 1

print(dictionary)