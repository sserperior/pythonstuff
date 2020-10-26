courses = ['History', 'Math', 'Physics', 'CompSci']

# Comma separated courses
course_str = ', '.join(courses)
print(course_str)

# Create list back from string
new_courses = course_str.split(', ')
print(new_courses)