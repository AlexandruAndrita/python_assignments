text = input("Enter text: ")

upper_number = 0
for i in text:
    if i.isupper():
        upper_number += 1

if upper_number == 1:
    print(f"The input text contains {upper_number} uppercase character.")
else:
    print(f"The input text contains {upper_number} uppercase characters.")
