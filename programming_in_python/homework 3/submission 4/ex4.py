import sys

matrix, maximum, number_of_lines = [], -sys.maxsize-1, 0

while True:
    user_input = input("Enter row: ")
    if user_input == "x":
        break
    number_of_lines += 1
    row = user_input
    row = row.split(" ")
    for i in range(len(row)):
        row[i] = int(row[i])
    if len(row) > maximum:
        maximum = len(row)
    matrix.append(row)

for i in matrix:
    if len(i) != maximum:
        length = len(i)
        while length != maximum:
            i.append(0)
            length += 1

print("[", end="")
for count, i in enumerate(matrix):
    if count != 0:
        print(" [", end="")
    else:
        print("[", end="")
    for count_line,j in enumerate(i):
        if count_line + 1 != len(i):
            print(j, end=" ")
        else:
            print(j, end="")
    if count + 1 != number_of_lines:
        print("]")
    else:
        print("]", end="")
print("]")

row_sum, column_sum = [], []
total_sum = 0

for i in matrix:
    r_sum = 0
    r_sum += sum(i)
    total_sum += r_sum
    row_sum.append(r_sum)

for j in range(len(matrix[0])):
    c_sum = 0
    for i in matrix:
        c_sum += i[j]
    column_sum.append(c_sum)

print(f"row sums: {row_sum}\ncolumn sums: {column_sum}\ntotal sum: {total_sum}")

