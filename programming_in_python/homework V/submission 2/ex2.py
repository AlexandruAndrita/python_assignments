def special_case(start: int,stop: int,step: int=1):
    if start>=stop:
        return []
    return [start]+special_case(start-step,stop,step)


def gen_range(start: int,stop: int, step: int = 1):
    if not isinstance(start,int) or not isinstance(stop,int) or not isinstance(step,int):
        raise TypeError("One of 'start', 'stop' or 'step' is not an integer")
    if step==0:
        raise ValueError("'step' has been assigned value 0 - imposible")
    if start<=stop and step<0 and start<0:
        return special_case(start,stop,step)
    if start<stop and step>0 or start>stop and step<0:
        return [start]+gen_range(start+step,stop,step)
    elif start>=stop or start<=stop and step<0 and start>=0:
        return []

