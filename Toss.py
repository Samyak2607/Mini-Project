import numpy as np
print('Choose Head or Tail')
choice = input()
coin = np.random.randint(0,2)
if(coin == 0 ):
  print('Head comes')
else:
  print('Tails Comes')
