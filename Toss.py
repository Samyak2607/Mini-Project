import numpy as np

name_1st_person = input('Team A : Enter Your Team Name')
name_2nd_person = input('Team B: Enter Opponent Team Name')

ch = np.random.randint(0,2)
choice = ''
if(ch == 0):
	choice = input(name_1st_person+' Select Head or Tail')
else:
	choice = input(name_2nd_person+' select Head or Tail')

np.random.seed(12)

coin = np.random.randint(0,2)

if(choice.lower() != 'head' or choice.lower() != 'tail'):
	print('Invalid Input')

elif((coin == 0 and choice.lower() == 'head') or (coin == 1 and choice.lower() == 'tail')):
	if(ch == 0):
		print(name_1st_person+' Team Win')
	else:
		print(name_2nd_person+' Team Win')
else:
	if(ch == 0):
		print(name_2nd_person+' Team Win')
	else:
		print(name_1st_person+' Team Win')

