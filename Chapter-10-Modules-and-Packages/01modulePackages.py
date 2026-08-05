'''
modules and packages:
in python, modules & packages help organise and reuse code. 
here is a comprehensive guide on how to import them.

'''
from math import *
print(sqrt(25))

from math import sqrt, pi
print(sqrt(16))
print(sqrt(25))
print(pi)


import numpy as np
print(np.array([1,2,3,4,5,6,7,8,9,10]))

print(np.__version__)


from package.math import addition
print(addition(2, 3))