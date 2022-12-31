lowercase, uppercase, other, unique = [], [], [], set()

my_string = input("Enter string: ")

for i in range(len(my_string)):
    unique.add(my_string[i])
    if my_string[i].islower():
        lowercase.append(my_string[i])
    elif my_string[i].isupper():
        uppercase.append(my_string[i])
    else:
        other.append(my_string[i])

print(f"lowercase: {lowercase}\nuppercase: {uppercase}\nother: {other}\nunique: {unique}")