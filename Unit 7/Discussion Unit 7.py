'''
The Items keyword when it comes to tuples, or just dictionaries in general, is incredibly useful 
for isolating individual elements, putting them inside of a tuple and returning them fast.

In the below example, I give it a Dictionary containing a Username, a Password, and an E-Mail address.
It then loops over the items inside of the dictionary and prints both the key and the value for that key.
'''

def tuple_items(dict):
    for key, value in dict.items():
        print('Key: ', key,', Value: ', value)
        
tuple_items({'Username:': 'AndLan', 'Password:': 'Password123', 'E-Mail:': 'xandrewlanoue@gmail.com'})

'''
The Zip keyword is useful for iterating through two lists at the same time, because it returns a list 
of tuples that can then be iterated across. 

In the blow example, it takes two lists of numbers, uses Zip on them and makes a list of tuples.

Then it loops over that list of tuples and prints the numbers in those matching indices for each list.

This can be used for more than just numbers, which is shown in the example with the last indices being strings.
'''

_number_list_one = [5, 23, 18, 9, 3, 20, 'Hello']
_number_list_two = [12, 3, 9, 11, 17, 10, 'World!']

def tuple_zip(l1, l2):
    _tuple_list = list(zip(l1, l2))
    for num1, num2 in _tuple_list:
        print('List 1: ',num1,' List 2: ', num2)
    
tuple_zip(_number_list_one, _number_list_two)

'''
As for Enumerate, this can be used to easily loop over  a list and return a tuple with more efficiency.

For this function ,it takes a list as an argument and creates a new tuple based off of that list, then 
it loops over that tuple and prints both the Index and the Item itself in that index.

'''
_list_of_words = ['This', 'is', 'a', 'list', 'of', 'words']

def tuple_enumerate(list):
    _tuple = enumerate(list)
    for index, item in _tuple:
        print('Index: ', index, ' Item: ', item)

tuple_enumerate(_list_of_words)