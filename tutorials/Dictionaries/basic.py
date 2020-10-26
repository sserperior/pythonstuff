# key-value pairs aka hash tables/maps
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'] }
print(student)

# Access a key of student - John
print(student['name'])

# Integer keys
student = {1: 'John', 'age': 25}
print(student[1])

# Non-Existent key - returns 'None'
print(student.get('Name'))

# Defaults for non-existent keys - returns 'Non-Existent'
print(student.get('Name', 'Non-Existent'))

# Add to dictionary
student['phone'] = '555-5555'
print(student.get('phone'))

# Update values via update
student.update({ 1: 'Jane', 'age': 33, 'isGrad': True })
print(student)

# Delete a key-value
del student['age']
print(student)

# Delete via pop
student['age'] = 44
age = student.pop('age')
print(student)
print(age)