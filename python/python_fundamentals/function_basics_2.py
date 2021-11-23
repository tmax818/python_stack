""" function basics 2

Objectives:
Learn how to create basic functions in Python
Get comfortable using lists
Get comfortable having the function return an expression/value


"""


def countdown_v1(num):
    my_list = []
    for num in range(5, -1, -1):
        my_list.append(num)
    return my_list


def countdown_v2(num):
    return [num for num in range(5, -1, -1)]


def countdown_v3(num):
    return list(range(5, -1, -1))


print(countdown_v1(5))
print(countdown_v2(5))
print(countdown_v3(5))


def print_and_return(lst):
    print(lst[0])
    return lst[1]


print(print_and_return([1, 2]))


def first_plus_length(lst):
    return len(lst) + lst[0]


print(first_plus_length([1, 2, 3, 4, 5]))


def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    new_list = []
    for num in lst:
        if num > lst[1]:
            new_list.append(num)
    print(len(new_list))
    return new_list
