age = int(input("Enter age: "))

if age<0:
    print("Invalid age")
elif age<=7:
    print("Child ticket: 10$")
elif age>=8 and age<=17:
    print("Teenager ticket: 15$")
elif age>=18:
    salary = int(input("Enter salary: "))
    if salary<0:
        print("Invalid salary")
    elif salary<=1000:
        print("Reduced adult ticket 1: 20$")
    elif salary>=1001 and salary<=2000:
        print("Reduced adult ticket 2: 25$")
    else:
        print("Adult ticket: 30$")


