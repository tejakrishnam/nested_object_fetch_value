import string
import json

def safeget(dct, keys):
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
    return dct

# provide input in a dictionary format
example_dict = input("Provide the nested object/dictionary : ")

# creating an empty list
lst = []
  
# number of elemetns as input
n = int(input("Enter number of keys : "))
  
# iterating till the range
for i in range(0, n):
    ele = str(input())
    lst.append(ele) # adding the element
value = safeget(json.loads(example_dict), lst)
print(value)