animals = {'a': ['ant'], 'b': ['bat'], 'c': ['cobra']} 
animals['d'] = ['deer']

animals['d'].append('dog') 

animals['d'].append('dolphin')
"""
for all .values() in the dictionary
    get the len(values)
    all up the length of all values
return the sum
"""

def value_counter(dic):
    sum = 0
    for item in dic.values():
        sum += len(item)
    return sum
   


#print(value_counter(animals))
#print(value_counter({'k': [100, 12, 12, 16], 'M': [1]}))  
animals = {'a': ['ant'], 'b': ['bat'], 'c': ['cobra']} 
animals['d'] = ['deer']

animals['d'].append('dog') 

animals['d'].append('dolphin')