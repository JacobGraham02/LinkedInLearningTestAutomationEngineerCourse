# Collection of tools for handling iterators. Iterators are data types that can be used in a loop 
from cgitb import small
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
import operator

def function_cartesian_product():
    # Product will compute cartesian product of iterables. A cartesian product is the product of set X and set Y (X * Y) as ordered pairs where x is in X and y is in Y. 
    a = [1,2] # For example, these two products will return the following list if casted: [(1,3), (1,4), (2,3), (2,4)]
    b = [3,4]
    product = product(a,b, repeat=2) # Argument 'repeat' repeats the process of cartesian product x many times as specified
    print(list(product))
    
def function_permutations():
    # Returns all possible orderings of the specified collection. An iterable must be able to iterate over the collection. 
    a = [1,2,3]
    permutations_all = permutations(a, 2) # Second argument specifies permutations with a length of 2
    print(list(permutations_all))
    
def function_combinations():
    # Make all possible combinations with a specified length
    a = [1,2,3,4]
    comb = combinations(a, 2) # Second argument specifies length of combinations; is mandatory.
    print(list(comb))
    
def function_combinations_with_replacement():
    a = [1,2,3,4]
    comb_wr = (combinations_with_replacement(a,2))
    print(list(comb_wr))
    
def function_accumulate():
    a = [1,2,3,4]
    acc = accumulate(a, func=operator.mul) # Multiples each element instead of adding 
    acc2 = accumulate(a, func=max) 
    print(a)
    print(list(acc))

def smaller_than_three(x):
    return x < 3

def function_groupby():
    a = [1,2,3,4]
    group_object = groupby(a, key=smaller_than_three) # Groups some data from a sorted collection based on whatever the condition is for the second argument. 
    print(group_object)
    
    for key, value in group_object:
        print(key, list(value))
    
function_accumulate()