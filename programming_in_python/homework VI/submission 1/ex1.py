def read_numbers(path: str) ->list:
    token_list=list()
    with open(path,"r",newline="\r\n") as file:
        file_content=file.readlines()
    for line in file_content:
        line=line.split(" ")
        for token in line:
            if token[len(token)-2:]=="\r\n":
                token=token[:len(token)-2]
            try:
                if token.isdigit():
                    token=int(token)
                else:
                    token=float(token)

                if isinstance(token, int):
                    token_list.append(token)
                elif isinstance(token, float):
                    token_list.append(float(token))
            except:
                continue

    return token_list

