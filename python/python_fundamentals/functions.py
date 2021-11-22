# Objectives:
# Understand what a function is and why it's important
# Understand the basic syntax for a Python function
# Understand parameters and arguments
# Understand what a return does in a function


# syntax

def add(a, b):  # function name: 'add', parameters: a and b
    x = a + b  # process
    return x  # return value: x


new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
# the result of the add function gets sent back to and saved into new_val, so we will see 8
print(new_val)
