nums = [1, 2, 3, 4, 5]

# Prints
# 1 a
# 1 b
# 1 c
# 2 a
# 2 b
# 2 c
# 3 a
# 3 b
# 3 c
# 4 a
# 4 b
# 4 c
# 5 a
# 5 b
# 5 c

for num in nums:
	for letter in 'abc':
		print(num, letter)