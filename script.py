import string
import json

def get_obj_value(dct, keys):
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
    return dct

# provide input in a dictionary format
input_dct = input("Provide the nested object/dictionary : ")

# creating an empty list
lst = []
  
# number of elemetns as input
n = int(input("Enter number of keys : "))
  
# iterating till the range
for i in range(0, n):
    ele = str(input())
    lst.append(ele) # adding the element
value = get_obj_value(json.loads(input_dct), lst)
print(value)