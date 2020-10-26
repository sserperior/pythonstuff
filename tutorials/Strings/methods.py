message = 'Hello World'

# lower case
print(message.lower())

# upper case
print(message.upper())

# count Hello occurrences - just 1
print(message.count('Hello'))

# count 'o' occurrences - 2
print(message.count('o'))

# find first index of a sequence of letters - 6 for 'World'
print(message.find('World'))

# find returns -1 if sequence of letters is not found
print(message.find('Universe'))

# replace
newMessage = message.replace('World', 'Universe')
print(newMessage)

# concatenation
greeting = 'Hello'
name = 'Michael'
greetingMessage = greeting + ', ' + name
print(greetingMessage)

# formatted string
greetingMessage = '{}, {}. Welcome!'.format(greeting, name)
print(greetingMessage)

# fstrings
greetingMessage = f'{greeting}, {name}. Welcome fstring!'

# show attributes and methods of a variable
print(dir(name))

# help for a string type
print(help(str))
print(help(str.lower))