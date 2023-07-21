prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
     if letter == 'Q' or letter == "O":
         print(f'{letter}u{suffix}')
     else : print(letter + suffix)
     

'''
The simplest form of string splicing is the ability to combine two strings in one step. You can add any number of strings together.
'''
def string_splice_1(a, b):
    return (f"{a}{b}")

print("- - - Example 1 - - -")
print(string_splice_1("Crab", "apple"))

'''
Another feature of string splicing is to be able to break apart a sentence/paragraph into the individual words and count them.

These words are also saved in an array called _list_of_words that you can then access later on to do whatever you want with them.
'''
def string_splice_2(s):
    _list_of_words = s.split(" ")
    return (f"There are {len(_list_of_words)} words in the sentence you submitted.")

print("- - - Example 2 - - -")
print(string_splice_2("Hello, it is nice to meet you! What is your name?"))

'''
You can also use splicing to isolate certain parts of a string. Say for example you wanted to isolate the first half of the last half of a word, you can use my function below to do so.

By providing any string into string_splice_3 below, it will automatically split any word or string in half. 
'''

def string_splice_3(s):
    _length = len(s)
    _seperated_strings = [s[0: round(_length / 2)], s[round(_length / 2):_length]]
    return _seperated_strings

print("- - - Example 3 - - -")
print(string_splice_3("Hello World! What a nice day for a walk, isn't it?"))