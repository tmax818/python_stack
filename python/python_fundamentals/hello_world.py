from webbrowser import open
print("Hello world!")

x = "Hello Python"
print(x)
y = 42
print(y)

# 1. TASK: print "Hello World"
print(None)
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print(None)  # with a comma
print(None)  # with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print(None)  # with a comma
print(None)  # with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print(None)  # with .format()
print(None)  # with an f string

# Solution

# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello", name)  # with a comma
print("Hello" + name)  # with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name)  # with a comma
print("Hello" + str(name))  # with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(
    fave_food1, fave_food2))  # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.")  # with an f string


# old string formatting

open('https://docs.python.org/3/library/stdtypes.html#old-string-formatting')
