student = { 'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# number of key-value pairs - 3
print(len(student))

# print keys
print(student.keys())

# print values
print(student.values())

# print keys and values
print(student.items())

# loop through keys
for key in student:
	print(key)

# loop through keys and values
for key, value in student.items():
	print(key, value)