# Docstring comment is the triple quoted string below.

def factorial(n):
	"""Returns the factorial of a number n > 0.
	This is a recursive function.
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

print(factorial(6))