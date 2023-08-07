import math

'''
The first step of the incremental development process for developing a hypotenuse function is to create the function, that takes in parameters, and returns a basic value.

Once created, call the function to ensure that it properly works and print the results so you can visibly see it functioning properly.
'''

#def hypotenuse(a, b):
#    return "Working as intended."

#print(hypotenuse(5, 5))

'''
The second step of the incremental process is to perform basic math on the variables to ensure that they are properly fed in.

In the below example, the function should return the value of a + b, or 10 in this case.
'''

#def hypotenuse(a, b):
#    return a + b

#print(hypotenuse(5, 5))


'''
The third step of the incremental process is to perform the correct calculations on the values provided, and return them in the function.
'''

#def hypotenuse(a, b):
#    return math.sqrt(a**2 + b**2)

#print(hypotenuse(5, 5))

'''
The final step, for readability, is to round down the result to a more manageable point. 
'''

'''def hypotenuse(a, b):
    return round(math.sqrt(a**2 + b**2), 2)

print(hypotenuse(3, 4))
print(" ")
print(hypotenuse(3, 7))
print(" ")
print(hypotenuse(4, 10))
print(" ")'''


'''
The function I've decided to make in this is a multi-part calculator to find your weight on both the Moon and Mars.

The formula, for obvious reasons, is not mine but the function will be.

The first step is to instantiate a basic function, called calc_weight, that takes in two parameters: The location and your weight on Earth.
'''

#def calc_weight(loc, weight):
#    return "This works"


'''
The second step is to properly access the arguments being passed into the function. To do this, I will simply print them out to the console to test this.
'''

#def calc_weight(loc, weight):
#    print(loc)
#    print(weight)
#    return "This works"

'''
The third step is to set up a few conditionals for the function. These will look at the location and decide which formunla to apply to the weight.

To test this, I will call the function twice with three different variables. One will be "Moon", one will be "Mars", and one will be "Earth".
'''

#def calc_weight(loc, weight):
#    if loc == "Moon":
#       return "Calculating weight on the Moon..."
#    elif loc == "Mars":
#        return "Calculating weight on Mars..."
#    else: return "Right now this only works with 'Mars' and 'Moon'. Please call this function with one of those two as the first value."

'''
The final step for creating this function and ensuring it works properly is to plug the proper formula into the return function inside of the two If statements.

I will also, for the sake of readability, be rounding those numbers down to two decimal places.

'''

#def calc_weight(loc, weight):
#    if loc == "Moon":
#       return round(weight / 9.81 * 1.622, 2)
#    elif loc == "Mars":
#       return round(weight / 9.81 * 3.711, 2)
#    else: return "Right now this only works with 'Mars' and 'Moon'. Please call this function with one of those two as the first value."

#print(" ")
#print(f'If you weighed 150 on Earth, on the moon it would be: {calc_weight("Moon", 150)} lbs ')
#print(f'If you weighed 150 on Earth, on Mars it would be: {calc_weight("Mars", 150)} lbs ')
#print(" ")

'''
This part isn't necessary, but I will be adding functionality for the other solid surfaced planets as well because I find it fun.
'''

def calc_weight(loc, weight):
    if loc == "Moon":
       return round(weight / 9.81 * 1.6, 2)
    elif loc == "Mars":
       return round(weight / 9.81 * 3.7, 2)
    elif loc == "Mercury":
        return round(weight / 9.81 * 3.7, 2)
    elif loc == "Pluto":
       return round(weight / 9.81 * .58, 2)
    else: return "Right now this only works with 'Mars', 'Moon', 'Mercury' and 'Pluto'. Please call this function with one of those two as the first value."
    
print(" ")
print(f'If you weighed 150 on Earth, on the Moon it would be: {calc_weight("Moon", 170)} lbs ')
print(f'If you weighed 150 on Earth, on Mars it would be: {calc_weight("Mars", 170)} lbs ')
print(f'If you weighed 150 on Earth, on Mercury it would be: {calc_weight("Mercury", 170)} lbs ')
print(f'If you weighed 150 on Earth, on Pluto it would be: {calc_weight("Pluto", 170)} lbs ')
print(" ")

