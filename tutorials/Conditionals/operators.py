user = 'Admin'
loggedIn = True

# user is admin and logged in
if user == 'Admin' and loggedIn:
	print('User is admin and logged in!')
else:
	print('Bad credentials')

# Bad credentials
loggedIn = False
if user == 'Admin' and loggedIn:
	print('User is admin and logged in!')
else:
	print('Bad credentials')

# not
if not loggedIn:
	print('Not logged in')