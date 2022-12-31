import math


def create_train_test_splits(data: list, train_size: float) -> tuple:
    if len(data)==0:
        return ([],[])

    train_size=math.floor(train_size*10)
    train_set=data[:train_size]
    test_set=data[train_size:len(data)]

    return (train_set,test_set)


print("create_train_test_splits([], 0.5) = {}".format(create_train_test_splits([], 0.5)))
print("create_train_test_splits(list(range(10)), 0.5) = {}".format(create_train_test_splits(list(range(10)), 0.5)))
print("create_train_test_splits(list(range(10)), 0.67) = {}".format(create_train_test_splits(list(range(10)), 0.67)))
print("create_train_test_splits(list(range(10)), 0.32) = {}".format(create_train_test_splits(list(range(10)), 0.32)))
print("create_train_test_splits(list(range(10)), 0.19) = {}".format(create_train_test_splits(list(range(10)), 0.19)))
print("create_train_test_splits(list(range(10)), 0.21) = {}".format(create_train_test_splits(list(range(10)), 0.21)))