# Values are unordered and no duplicates. Defined with curly braces
courses = { 'History', 'Math', 'Physics', 'CompSci'}
# Order can change from run to run!
print(courses)

# Automatic removal of duplicates. Math should only show up once
courses = { 'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(courses)

# Test existence of a member. Optimized vs Lists
print('Math' in courses)

# Commonality - History, Math
courses = { 'History', 'Math', 'Physics', 'CompSci'}
courses2 = { 'History', 'Math', 'Art', 'Design'}
print(courses.intersection(courses2))

# Not common - Physics, CompSci
print(courses.difference(courses2))

# Union - all unique elements from two sets. Duplicates removed { 'CompSci', 'Art', 'Design', 'History', 'Math', 'Physics' }
print(courses.union(courses2))