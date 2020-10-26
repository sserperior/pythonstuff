courses = ['History', 'Math', 'Physics', 'CompSci']

for item in courses:	
	print(item)

# loop with an index
for index, course in enumerate(courses):
	print(index, course)	

# loop with a starting index value
for index, course in enumerate(courses, start=1):
	print(index, course)
