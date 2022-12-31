import re


def flatten_list(id_numbers):
    flattened=[]
    for elem in id_numbers:
        if isinstance(elem,list):
            flattened+=flatten_list(elem)
        else:
            flattened.append(elem)
    return flattened

def convert_elements_to_int(id_numbers):
    for i in range(len(id_numbers)):
        id_numbers[i]=int(id_numbers[i])
    return id_numbers

def extract_matr_ids(text: str) -> list[int]:
    pattern=r"(?<![a-zA-Z0-9])[kK]{,1}\d{8}(?![a-zA-Z0-9])|id=[0-9]{4,8}(?![0-9])"
    match_object=re.findall(pattern,text)
    pattern_digits=r"[0-9]{4,8}"
    id_numbers=[]
    for match in match_object:
        match_digit=re.findall(pattern_digits,match)
        id_numbers.append(match_digit)
    id_numbers=flatten_list(id_numbers)
    id_numbers=convert_elements_to_int(id_numbers)
    return id_numbers


t = """This is an ID 01234567 this12345678 is not (leading "s"), nei12345678ther
(leading "i" and trailing "t" letters) is 12345678this (trailing "t"). but this
k22222222 is and also this K33333333, but again, k12345678is not valid (trailing
"i") and neither is K123456789 (too many digits) or 1234 (too few digits). Another
valid is ID id=4444 or id=5555555. Invalid examples are id=d1234 (leading "d") or
id=12 (too few digits) or id=x12345678 (leading "x") or id=123456789 (too many
digits) or ID=1234 ("ID" is not equal to "id"). id=11111xyz is valid again."""

print(extract_matr_ids(t))