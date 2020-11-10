# args = arguments
# kwargs = keyword arguments
def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

# Prints
# ('Math', 'Art')
# {'name': 'John', 'age': 22}
student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = { 'name': 'John', 'age': 22}

# Prints
# (['Math', 'Art'], {'name': 'John', 'age': 22})
# {}
student_info(courses, info)

# Unpack
# Prints
# ('Math', 'Art')
# {'name': 'John', 'age': 22}
student_info(*courses, **info)