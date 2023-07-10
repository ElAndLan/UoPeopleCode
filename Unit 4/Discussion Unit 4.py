#Section 6.9 Debugging of your textbook lists three possibilities to consider if a function is not working.

#Describe each possibility in your own words.

#Define "precondition" and "postcondition" as part of your description.

#Create your own example of each possibility in Python code. List the code for each example, along with sample output from trying to run it.

'''

The three possibilities to consider if your function isn't properly working are as follows:

1) There's something wrong with the arguments that your function is recieving, or the values that are being passed into it. This would be a PRECONDITION being violated. 
   This means that a condition that needs to be provided for the function to properly work and execute is invalid.
   
2) There's something wrong with the function itself, this would be a POSTCONDITION being violated. 
   This means that the actual function itself has some form of a greater flaw that causes it to not properly work be it a flaw in logic or some other problem. 
   
3) There is something wrong with the result of the function itself, whether it's the return value or the actual usage of the function itself.
   This means that the way the function is being used is is likely improper and a new function needs to be created, or old one modified, to meet the actual needs.
   

'''

def find_sum(a, b):
    return a + b

#print(find_sum(5, 5)) 
#print(find_sum(5, "Hello"))

'''
The above find_sum is an example of a PRECONDITION being violated. 
The issue with this is that the condition that needs to be provided, or the argument the function is taking in,is flawed and is not what needs to be provided for the function to work.

In this example, the issue is that find_sum is given an argument of an int (Which it expects) and a string (Which it does not), and it cannot add an int with a string so it 
outputs an error.

To see the error itself that is output to the console, please uncomment line 29 and run the program. 
I have commented it out so that the rest of the script will run properly.
'''


def find_quotient(a, b):
    return a * b

print(find_quotient(10, 5))

'''
The above find_quotient is an example of a POSTCONDITION being violated.

In this example, the issue is that find_quotient itself is the problem. 
The function instead of dividing like it should be to find the quotient, is instead multiplying the numbers together.

Because the problem is with the function itself and not the arguments, that means it is a POSTCONDITION being violated.
'''

def repeat_strings(a, b):
    return a * b

repeat_strings("Hello", 5)

'''
The above repeat_strings function is an example of there being something wrong with the results of the function itself, more specifically the usage of the function results.

In this case, the function is being called and it's properly executing but because I did not put the function call inside of a print statement, 
it isn't properly using the results returned from the function itself. 
'''