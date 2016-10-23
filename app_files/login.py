import sys
from . import functions
from . import doctor
from . import nurse
from . import admin

def start(): 
	username = input('Please login with your username: ')
	password = input('And password: ')
	
	user = functions.getUser(username, password) # return obj of user info, or None if can't be found
	if user is not None: 
		if user['role'] == 'D':
			doctor.flow(user)
		if user['role'] == 'N':
			nurse.flow(user)
		if user['role'] == 'A': 
			admin.flow(user)
