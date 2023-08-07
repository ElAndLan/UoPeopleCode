'''
In the below example, a NameError is thrown because the string variable has not been created.

Catching exceptions is extremely helpful because it allows you pinpoint where bugs are happening and
why they're happening much easier. 

As long as the exceptions are set up properly, it gives you extremely helpful information that helps
to narrow down issues. 

In the below example, it requests an input from the user. If the input is a number, it multiplies it 
by 5 and returns the value.

If the input is not a number, it returns a Value Error and requests that you input a valid number.

'''

def Multiply_Number_By_5():
    while True:
        _input = input("Please input a number!")
        try: 
            _num = int(_input)
            return _num * 5
        except ValueError:
            print("Please input a valid number next time!")
    
print(Multiply_Number_By_5())