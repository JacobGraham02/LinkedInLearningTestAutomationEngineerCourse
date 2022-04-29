# JSON exists as a sequence of bytes which is useful in case we need to transmit a stream of data over a network
'''
Simple python objects are translated to JSON according to the following conversion:
Python  JSON
dict             -> object
list, tuple      -> array
str              -> string
int, long, float -> number
True             -> true
False            -> false
None             -> null
'''

# Python to JSON serialization and encoding
import json
from json import JSONEncoder

person = {"name": "John", "Age": 30, "City": "Barrie", "titles": ["Engineer", "Chef", "Cat-man"]}

# Converting a Python object into JSON
person_json = json.dumps(person)

# Convert Python objects into JSON objects and save them to a file with json_dump()
with open('json/person.json', 'w') as json_file:
    json.dump(person, json_file)
    
# Converting a JSON string into a Python object with the json.loads() method will result in a Python dictionary
json_file = open('json/person.json', 'r')

json_data = json.load(json_file)

print(json_data)



# A custom encoder class is good practice when writing custom objects to a JSON file. You must overwrite the default() method for this approach. 
class ComplexEncoder(JSONEncoder):
    
    def default(self, o):
        if isinstance(z, complex):
            return {z.__class__.__name__: True, "real": z.real, "imaginary" : z.imag}
        # Let the default implementation of handle() deal with other objects or raise a TypeError
        return JSONEncoder.default(self, o)
    
z = 5 + 9j # A complex data type here where the first argument is real, and the second argument is imaginary. 
zJSON = json.dumps(z, cls=ComplexEncoder)

# Can use the encoder class directly without passing in as an argument to another function
zJson = ComplexEncoder().encode(z)
print(zJson)


# Decoding a custom object with the default JSONDecoder will be decoded into a dictionary. Write a function that takes a dictionary as input and creates an object using it. 
def decode_complex_object(dictOfJson):
    if complex.__name__ in dictOfJson:
        return complex(dictOfJson["real"], dictOfJson["imag"])
    return dictOfJson

zJson = json.loads(zJSON, object_hook=decode_complex_object) # The object_hook argument specifies which function the result dictionary is passed into.

