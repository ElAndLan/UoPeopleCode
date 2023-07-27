'''
Equivelant in a nutshell is when something is equal to eachother, but aren't the same objects.

Identical on the other hand is when something is the same object. 

Below are two examples, one will showcase Equivelancy and the other will showcase Identicalness.
'''


'''
Because the _fruits list is assigned to _my_favourite_fruits in show_identical, they are both essentially the same object (Which is the _fruits object).
'''

def show_identical():
    _fruits = ["Apple", "Banana", "Mango"]
    _my_favourite_fruits = _fruits
    
    print("- - - Example 1: Identical - - -")
    print(_fruits is _my_favourite_fruits)
    print("- - - - - - - - - - - - - - - - -")
    
'''
In the show_equivelant example, you instantiate two seperate objects and assign them both the same values.

They may have the same values, but they are not identical objects because they are their own objects.

This is showcased by first using the 'is' keyword to check to see if the two lists are identical. This returns false because they are not the same objects.
Then it checks for equivelancy by using the '==' operator to check to see if the two lists have the same values. This returns true because the values inside of the lists are the same.
'''
def show_equivelant():
    _fruits = ["Apple", "Banana", "Mango"]
    _my_favourite_fruits =  ["Apple", "Banana", "Mango"]
    
    print(" - - - Example 2: Equivelant - - -")
    print(_fruits is _my_favourite_fruits)
    print(_fruits == _my_favourite_fruits)
    
show_identical()
show_equivelant()

'''
In the remove_duplicates function below, it will take in an argument of an array of strings and it will go through said array and remove any duplicates.

The set function will go then create a dictionary of the remaining words, and convert it to a list.

But because I am not setting the _updated_list value to the list itself, the new updated list is not identical to the provided list into the function.
'''

def remove_duplicates(list):
    _updated_list = [*set(list)]
    print(" - - - Example 3 - - -")
    print(f"The submitted list is: {list}.")
    print(f"The submitted list with duplicates removed is {_updated_list} ")
    print(list is _updated_list)
    
remove_duplicates(["Apples", "Bananas", "Avocado", "Apples", "Mangoes", "Grapes", "Avocado", "Strawberry", "Watermelon", "Apples"])