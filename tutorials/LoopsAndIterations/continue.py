nums = [1, 2, 3, 4, 5]

# Prints
# 1
# 2
# Found 3, continue
# 4
# 5

for num in nums:
	if num == 3:
		print('Found 3, continue')
		continue
	print(num)