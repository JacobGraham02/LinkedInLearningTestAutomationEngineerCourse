from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

def collections_counter():
    '''
    Implements container data types, and other versions of collections with special functionality
    Counter: Counts the number of occurances of a character in a string. 
    '''
    my_counter = Counter("hello")
    print(my_counter.items())
    print(my_counter.keys())
    print(my_counter.values())
    print(my_counter.most_common(1)) # The argument in most_common returns the x number of common characters starting from the most common to the last common. 
    print(list(my_counter.elements())) # An iterable over all of the elements in the my_counter 
    
    
def collections_namedtuple():
    Point = namedtuple('Point', 'x,y') # arguments are: class name, fields separated by delimiter.
    pt = Point(1, -4)
    print(pt)  
    
def collections_ordereddict():
    # Maintains dictionary element insertion order if using Python versions < 3.7
    ordered_dict = OrderedDict()
    ordered_dict['a'] = 1
    ordered_dict['b'] = 2
    ordered_dict['c'] = 3
    ordered_dict['d'] = 4
    print(ordered_dict)
    
def collections_defaultdict():
    # Will have a default value if key has not been set
    default_dict = defaultdict(int)
    default_dict['a'] = 1
    default_dict['b'] = 2
    print(default_dict)
    
    
def collections_deque():
    # Is a double-ended queue. Elements can be added and removed from both ends of the deque
    d = deque()
    
    d.append(1)
    d.append(2)
    d.appendleft(3)    
    
    d.pop() # Removes from the right side (traditional rear) of the queue.
    d.popleft() # Removes from the left side (traditional front) of the queue.
    d.clear()
    
    d.extend([4,5,6]) # Appends entire list to right side of deque.
    
    d.extendleft([4,5,6]) # Appends to left side of deque.
    
    d.rotate(1) # Rotates all elements 1 space to right
    
    d.rotate(-1) # Rotates all elements 1 space to left
