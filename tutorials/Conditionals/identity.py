a = [1,2,3]
b = [1,2,3]

# True
print(a==b)

# False - a and b are two different objects in memory
print(id(a))
print(id(b))
print(a is b)

# True - a and b are the same objects in memory
b = a
print(id(a))
print(id(b))
print(a is b)