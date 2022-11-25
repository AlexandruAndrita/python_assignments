def flatten(nested: list) -> list:
    if len(nested)==0:
        return []
    else:
        if isinstance(nested[0],list):
            return flatten(nested[0])+flatten(nested[1:])
        else:
            return nested[:1]+flatten(nested[1:])

