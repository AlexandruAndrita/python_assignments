def newline_character(word):
    new_word=""
    for c in range(len(word)):
        if word[c]=="\n":
            new_word+="\\n"
        else:
            new_word+=word[c]
    return new_word


def write_dict(d: dict, path: str, encoding: str="utf-8"):
    file=open(path,"w",encoding=encoding)
    for pair in d:
        value_new=newline_character(d[pair])
        key_new=newline_character(pair)

        line=key_new+":"+value_new
        file.write(line)
        file.write("\n")
    file.close()


def read_dict(path: str, encoding: str="utf-8") -> dict:
    file=open(path,encoding=encoding)
    dictionary={}
    while True:
        line=file.readline()
        if not line:
            break
        position=0
        for pos in range(len(line)):
            if line[pos]==":":
                position=pos
                break
        dictionary[line[:position]]=line[position+1:]

    #eliminates the '\n' from the end of the row
    for key in dictionary:
        if dictionary[key][len(dictionary[key])-1]=="\n":
            dictionary[key]=dictionary[key][:len(dictionary[key])-1]

    file.close()
    return dictionary


"""
#used for testing

#creating an arbitrary dictionary
def create_dictionary():
    dictionary=dict()
    dictionary["br  \\nand\\n"]="   Ford\\n  "
    dictionary["\\nmod  el"]="  Mustang  \\n\\n"
    dictionary["year\\n  "]="  196  4  "
    return dictionary

#calling the funciton to get the dictionary
some_dict=create_dictionary()

#the file used for testing
some_file="ex2_data.txt"

write_dict(some_dict,some_file)
new_dict=read_dict(some_file)
print(some_dict==new_dict)
"""