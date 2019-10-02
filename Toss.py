import numpy as np
print('Choose Head or Tail')
choice = input()
np.random.seed(123)
coin = np.random.randint(0,2)
if(coin == 0 ):
  print('Head comes')
else:
  print('Tails Comes')
