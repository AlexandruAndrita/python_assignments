def menu():
    print("Available actions:\na - Add lifter\nr - Remove lifter\nu - Update lifter\nv - View lifters\nx - Exit the program")


print("Welcome to Powerlifting Data Collector!\n")
menu()

lifers, lifer_details = dict(), dict()
lifer_details["squat"] = []
lifer_details["bench press"] = []
lifer_details["deadlift"] = []

user_input = input("Enter action: ")
while user_input != "x":

    if user_input == "a":
        lifer_name = input("Enter new lifer name: ")
        exists = 0
        for i in lifers:
            if i == lifer_name:
                print(f"Lifer '{lifer_name}' already exists!\n")
                exists = 1
        if exists == 0:
            lifers[lifer_name] = {}
            lifers[lifer_name]["squat"] = []
            lifers[lifer_name]["bench press"] = []
            lifers[lifer_name]["deadlift"] = []
            print()

    elif user_input == "r":
        lifer_name = input("Enter new lifer name: ")
        exists = 0
        for i in lifers:
            if i == lifer_name:
                exists = 1
        if exists == 1:
            del lifers[lifer_name]
            print()
        else:
            print(f"Lifer '{lifer_name}' does not exist!\n")

    elif user_input == "u":
        lifer_name = input("Enter lifter name to update: ")
        exists = 0
        for i in lifers:
            if i == lifer_name:
                exists = 1
        if exists == 1:
            lift_to_update = input("Enter lift (one of 'squat', 'bench press', 'deadlift'): ")
            weights = input("Enter weight(s): ")
            weights = weights.split(" ")
            for i in lifers:
                if i == lifer_name:
                    for j in range(len(weights)):
                        lifers[i][lift_to_update].append(float(weights[j]))
            print()
        else:
            print(f"Lifer '{lifer_name}' does not exist!\n")

    elif user_input == "v":
        if len(lifers) != 0:
            for i in lifers:
                print("------------------------------")
                print(f"Name: {i}")
                squat_weight=lifers[i]["squat"]
                bench_press_weight = lifers[i]["bench press"]
                deadlift_weight = lifers[i]["deadlift"]

                print(f"squat: {squat_weight}\nbench press: {bench_press_weight}\ndeadlift: {deadlift_weight}")
        print()
    else:
        print(f"Invalid action '{user_input}'. Try again!\n")
    menu()
    user_input = input("Enter action: ")

else:
    print("Bye!")