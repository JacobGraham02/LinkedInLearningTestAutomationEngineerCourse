# lambda arguments : expression. A lambda creates a single-line anonymous function that takes an argument and returns an expression
# Lambdas are used when you only need a function once or few other times in your code, or can be used as an argument for other higher-order functions. 
# Higher-order functions are functions that take other functions as arguments. 

def function_addlambda():
    add10 = lambda x: x + 10
    print(add10(5))
    
def function_multiplylambda():
    mult = lambda x,y: x * y
    print(mult(2,7))
    
points2D = [(1,2), (15,1), (5,-1), (10,4)]

def sort_by_y(x):
    return x[1]

def function_sortpoints2dlambda():
    points2D_sorted = sorted(points2D, key=lambda x: x[1]) # The list gets sorted according to the y-index of each coordinate
    print(points2D)
    print(points2D_sorted)