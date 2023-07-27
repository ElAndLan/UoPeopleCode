'''
The function string_mutation will cover all of part 1 for this learning journal.

First, it will split the _words string based on the spaces. It will then store those values in a list.

Then, the list will pop the value in the index of 3, which should be 'Mangoes' being removed.

After that, the list will remove any value inside of the list that is equal to "Tomatoes", 
because in this list of fruits we don't want any tomatoes.

For the final deletion of an index, we'll be using the 'del' keyword to remove the fruit in the second index inside of the list,
which in this case will be "Bananas" because I'm just not a fan of them personally.

The list is then sorted, and I add three new values to the list being "Grapefruit", "Mandarin" in index 3, and "Canteloupe".

When extending the list, you must specify how you want to extend it. In this scenario, I put 'Canteloupe' inside of brackets to show that I'm adding a new list element.
If I didn't do that, it would see each individual character in the string 'Canteloupe' as a new element and add a bunch of new indexes with each letter of the word.

'''

def string_mutation():
    _words = "Apples Oranges Bananas Mangoes Grapes Papayas Pineapples Tomatoes"
    _split_string = _words.split(" ")
    
    _split_string.pop(3)
    _split_string.remove("Tomatoes")
    del _split_string[2]
    
    _split_string.sort()
    
    _split_string.append("Grapefruit")
    _split_string.insert(3, "Mandarin")
    _split_string.extend(["Canteloupe"])
    
    
    return " ".join(_split_string)


print(string_mutation())

'''
The following is an example of a nested list, which is just multiple lists nested inside of eachother. 
It looks sloppy, but using dictionaries for this would make it much neater and easier to read.
'''
_nested_list = ["This", "Is", ["An", "Example", ["Of", "A", "Nested"], "List"], "!"]
print(_nested_list)
    
'''
By using the '*' operand on a list, it duplicates the initial entries however many times you multiply the list by.
By multiplying the list ["Hello", "World"] times 5, it creates 4 new entries that are exact copies of the originals.
'''

_multiplied_list = ["Hello", "World"] * 5
print(_multiplied_list)

'''
With List spliciing, you can take specific indexes of a list and do multiple things with them, be it print the values or assign them to a new variable or more.
In the below example, it seperates the list from index 4, removing A-D, and ends at index 8, removing I-K.
'''
_list_of_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
print(_list_of_letters[4:8])

'''
The += operator does the same thing as normal when it comes to modifying arrays. It adds whatever you want to add onto the end of your Array.
In this example, it adds "World" to the end of the array containing "Hello"
'''
_plus_equals = ["Hello"]
_plus_equals += ["World"]
print(_plus_equals)

'''
Below is an example of using a filter to cycle through a list and apply the is_even function on each index. 

It saves all the values that come back as true in a list, and gets rid of the other values that do not return true (AKA non-even numbers)
'''
def is_even(num):
    return num % 2 == 0

nums = [5, 258, 2, 4, 12, -2]
print(list(filter(is_even, nums)))

'''
As for  a list operation that is legal but does the "wrong" thing, I have a simple one that I've ran into multiple times during this assignmnent!

If you add a new element to a list without making sure it's the proper type, it can have some weird effects.

In this case, not extending with an actual list item will instead break the string up into each individual character, and add each character to the
list in their own index rather than adding the whole string to the list.

'''
_fruits = ["Apples", "Canteloupe", "Orange", "Banana"]
_fruits.extend("Avocado")
print(_fruits)