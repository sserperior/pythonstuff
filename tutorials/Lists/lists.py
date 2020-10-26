courses = ['History', 'Math', 'Physics', 'CompSci']

# ['History', 'Math', 'Physics', 'CompSci']
print(courses)

# 4
print(len(courses))

# 2nd course - Math (0-based index)
print(courses[1])

# Negative indexes start from the end

# Last item (CompSci)
print(courses[-1])

# Range of values - first two History and Math only - last parameter is stopping point exclusive
print(courses[0:2])
print(courses[:2])

# Range of values - index 2 to end - Physics and CompSci
print(courses[2:])

# Add items to a list
courses.append('Art')
print(courses)

# Insert item into a list - Add English to the front
courses.insert(0, 'English')
print(courses)

# Add multiple values via extend
courses2 = ['Education', 'Philosophy']
# Add list within a list
# [['Education', 'Philosophy'], ...]
#courses.insert(0, courses2)

# ['English', 'History', 'Math', 'Physics', 'CompSci', 'Art', 'Education', 'Philosophy']
courses.extend(courses2)
print(courses)

# remove
courses.remove('Math')
print(courses)

# pop - removes last element from the list
popped = courses.pop()
print(popped)
print(courses)

# Reverse list
courses.reverse()
print(courses)

# Sort list - ascii order. Works for numbers too
courses.sort()
print(courses)

# Sort in descending order
courses.sort(reverse=True)
print(courses)

# Sort without affecting original list
courses = ['History', 'Math', 'Physics', 'CompSci']
print(sorted(courses))
print(courses)