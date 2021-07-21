# Assignment 01
def concat_list(list1, list2):
    return list1 + list2


concated_list = concat_list(['a', 'b', 'y', 'd'], [5, 2, 9])
print(concated_list)

# Assignment 2:
"""
    create a function called separate() that accepts a string as an argument
    and returns a list containing each of the characters of
    the string separated as individual items in the list.
    Make sure to test the function.
"""


def separate(input):
    return list(input)

print(separate("Hello World"))

# Assignment 3:
"""
Create a function called multi_merge that takes a list and a string
as arguments.
The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.
"""

def multi_merge(my_list, my_string):
    my_list.append(my_string)
    return my_list + list(my_string)

print(multi_merge(['a','b','c'],'Hello World'))

# Assignment 4:

"""
Define a function called last_list that can accept an unlimited number
of lists but returns only the last list.
Example:
    For example, the below function call should return ['mike', 'john']
    last_list([1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john'])
"""

def last_list(*args):
    return args[-1]

print(last_list([1,2],['w','t'],[5,7,2]))

# Assignment 5:

"""
Define a function called key_list_items that can accept an unlimited number
of lists along with another argument. The function should return
the second_folder to last item in the specific list specified by the user of the function.
Example:
    For example, the below function call should return: jan
    key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])
"""
def key_list_items(key,**kwargs):
    return kwargs[key][-2]


result = key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])
print(result)