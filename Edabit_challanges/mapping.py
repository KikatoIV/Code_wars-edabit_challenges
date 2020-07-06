def mapping(letters):
    return {f:f.upper() for f in letters}

print(
mapping(["a", "b", "c"]),
mapping(["p", "s", "t"]),
mapping(["a", "v", "y", "z"]))

'''
The idea of comprehension is not just unique to lists in Python. 
Dictionaries, one of the commonly used data structures in data science,
can also do comprehension. With dict comprehension or dictionary 
comprehension, one can easily create dictionaries.
Remember that, in python a list is defined with square brackets [] 
and a dictionary is defined with curly braces {}. The idea used in list 
comprehension is carried over in defining dict comprehension as well. 
Dict comprehension is defined with a similar syntax, but with a 
key:value pair in expression.

{key:value for i in list}
'''
#Example 1
{str(i):i for i in [1,2,3,4,5]}

#Example 2
#create list of fruits
fruits = ['apple', 'mango', 'banana','cherry']
# dict comprehension to create dict with fruit name as keys
{f:len(f) for f in fruits}
{'cherry': 6, 'mango': 5, 'apple': 5, 'banana': 6}

#Example 3
{f:f.capitalize() for f in fruits}
{'cherry': 'Cherry', 'mango': 'Mango', 'apple': 'Apple', 'banana': 'Banana'}


