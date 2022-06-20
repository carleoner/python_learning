#from module_name import something
#import math
from math import sqrt
from random import random, randrange, shuffle
from secrets import choice

print(sqrt(4))

# ceil, floor, fabs, factorial, fmod
# log2(x), pow, sqrt, trunc
# degrees() radians()

import math

print(math.sin(0))

# pi, tau, Infinity - inf, Euler - e

print(math.pi)

###########################
###########################
# random number

import random
random.seed(5) #init the random number generator

print(random.random())              #generate float between 0 and 1
print(random.randint(1,1000))       #generate between 1 and 1000
print(random.randrange(1,10,3))     #generate between 1 and 10 with 3 step

seq = [3,5,7,9]
print(choice(seq))                  #random from sequence

random.shuffle(seq)
print(seq)