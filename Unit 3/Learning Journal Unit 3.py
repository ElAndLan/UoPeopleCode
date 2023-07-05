# 1. Copy the countdown function from Section 5.8 of your textbook.

def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)
          
# 1.1 Write a new recursive function countup that expects a negative argument and counts “up” from that number.

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)
        
# Write a Python program that gets a number using keyboard input.

# If the number is positive, the program should call countdown.
 
# If the number is negative, the program should call countup. 

# Choose for yourself which function to call (countdown or countup) for input of zero.

''' 
In this scenario, I have chosen for countdown to be called if the input is equal to zero or higher than zero.
'''

def get_input():
    n = int(input("Pick any number.\n"))
    if n > 0:
        countdown(n)
    else: countup(n)
    
#get_input()

# 2. Write your own unique Python program that has a runtime error.

def calculate_sales_tax_incorrect():
    _total_before_tax = float(input("What is your total cost before tax?\n"))
    print(f"The tax on a purchase of {_total_before_tax} is {(total_before_tax * .10)}")

'''
To see the RunTime error generated in this function, please uncomment line 47 and input any integer or float value and hit enter.
'''

#calculate_sales_tax_incorrect()

'''

The calculate_sales_tax_incorrect function will instantiate a variable named _total_before_tax, and ask the user for an input of the total cost before tax is applied.

Once the user inputs a value, whether it is an integer or a float value, it will automatically cast the value to a float.

Afterwards, it will print out a statement telling you the tax on a purchase of the input value, and it will multiply the _total_before_tax by .10 to apply a 10% discount.

But because the incorrect function has total_before_tax and not _total_before_tax, it will give a runtime error once the user inputs a value for the total before tax.

The reason this runtime error occurs is because the variables being called inside of the function, namely the second variable in the print statement on line 38, is incorrect.

Because this variable doesn't exist, it gives an error stating that it is not defined, and gives a suggestion for the correct variable.

- - - A simple fix for this would be to correct the total_before_tax error on 38 to the proper variable (_total_before_tax). - - -

A correct version of this function, called calculate_sales_tax_correct has been provided below that will run properly without any runtime errors because the second variable

in the print function has been called correctly.

'''

def calculate_sales_tax_correct():
    _total_before_tax = float(input("What is your total cost before tax?\n"))
    print(f"the tax on apurchase of {_total_before_tax} is {(_total_before_tax * .10)}")
    
calculate_sales_tax_correct()
