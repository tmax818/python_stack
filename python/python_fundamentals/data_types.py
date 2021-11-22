# objectives

# Understand common data types we'll encounter as we learn Python
# Review the syntax for common data types
# Understand basic type casting


# primitives

# bool
is_hungry = True
has_freckles = False
# number
age = 35  # storing an int
weight = 160.57  # storing a float
# string
name = "Joe Blue"

# composite

# tuple

dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
# dog[1] = 'dachshund'
# ERROR: cannot be modified ('tuple' object does not support item assignment)

# lists

empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)  # output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)  # output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)  # output: ['Francis', 'Oliver']

# dictionaries

empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'  # updates if the key exists
# adds a key-value pair if the key doesn't exist
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')  # removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
