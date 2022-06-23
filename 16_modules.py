# pip install module_name
# import module_name -> module_name.functionName()
# import module_name as m
# from module_name import functionName

#example
import math as m
m.factorial(5)

import sys
sys.path.append('../data/')
"""
import calculator as mc
mc.method_in()
print(mc.sub(2,3))
"""
from calculator import sub
print(sub(2,3))