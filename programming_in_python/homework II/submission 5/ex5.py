import sys

def menu():
    print("Available actions:\na - Add numbers\nv - View statistics\nx - Exit the program\n")


sum, average, count = 0, 0.0, 0
minimum = sys.maxsize
maximum = -sys.maxsize - 1

print("Welcome to Data Statistics!\n")
menu()
option = input("Enter action: ")
while option!="x":
    if option=="a":
        number = input("Enter number or 'x' when you are done: ")
        while number != "x":
            number = int(number)
            sum += number
            count += 1
            average = sum/count
            if number > maximum:
                maximum = number
            if number < minimum:
                minimum = number
            number = input("Enter number or 'x' when you are done: ")
        else:
            print()
    elif option == "v":
        if count == 0:
            print("No numbers have been added yet!\n")
        else:
            print(f"Count: {count}\nSum: {sum}\nAverage: {average}\nMin: {minimum}\nMax: {maximum}\n")
    else:
        print(f"Invalid action '{option}'. Try again!\n")
    menu()
    option = input("Enter action: ")
else:
    print("Bye!")

