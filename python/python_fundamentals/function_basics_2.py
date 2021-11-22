""" function basics 2

Objectives:
Learn how to create basic functions in Python
Get comfortable using lists
Get comfortable having the function return an expression/value


"""


def countdown_v1(num):
    my_list = []
    for num in range(0, -6, -1):
        my_list.append(5 - num)
    return my_list


def countdown_v2(num):
    return [num for num in range(5, -1, -1)]


def countdown_v3(num):
    return list(range(5, -1, -1))


print(countdown_v1(5))
print(countdown_v2(5))
print(countdown_v3(5))
