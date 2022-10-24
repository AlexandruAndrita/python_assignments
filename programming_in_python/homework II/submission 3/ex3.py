secret_number = int(input("Enter number to guess: "))
user_input = input("Enter number: ")

while user_input != "exit":
    user_input = int(user_input)
    if user_input == secret_number:
        print("Congratulations!")
        break
    elif user_input < secret_number:
        print("Your number is smaller.")
        user_input = input("Enter number: ")
    elif user_input > secret_number:
        print("Your number is bigger.")
        user_input = input("Enter number: ")
else:
    print("You lost!")