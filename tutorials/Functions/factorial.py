def factorial(n):
	if n==0:
		return 1
	elif n < 0:
		print('Cannot do a negative factorial.')
		return -1
	else:
		return n * factorial(n-1)

print(factorial(10))