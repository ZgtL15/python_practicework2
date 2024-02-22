"""
A collection of simple math operations
"""

def simple_add(a,b):
    return a+b
"""
the function to get the sum of a and b
parameters
---------- 
a:integer or float
b:integer or float

return
----------
a+b: the sum of a and b 

also the 
simple_sub
simple_mult
simple_div
poly_first
poly_second

"""


def simple_sub(a,b):
    return a-b

def simple_mult(a,b):
    return a*b

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
