# EXAMPLE 1

# In this function, if you provide your weight (on Earth)  it will return what your weight would be 
# on the moon.

# _earth_weight is the argument in this case, it is what can be fed into the function _weight_on_moon
_earth_weight = 200

# _weight is the paramter for this function, it is the temporary local variable that is only accessible
# from inside of the function _weight_on_moon, and it will hold whatever value you pass in to the function.
def _weight_on_moon(_weight):
    # _moon_weight is a local variable that is unique to _weight_on_moon and cannot be accessed
    # outside of the function itself. If you were to try to (which I will later for Example 3), 
    # it would not work properly because you can only access that varibale from within the function.
    _moon_weight = _weight / 9.81 * 1.622
    print("If you weigh " + str(_weight) + "lbs on Earth, on the moon you would weigh " 
                + str(_moon_weight // 1) + "lbs.")
    
print("")

# EXAMPLE 2

# This is a call to the function using a variable already defined inside of the code.
# Changing _earth_weight above will change the result you recieve from the function itself.
_weight_on_moon(_earth_weight)

# This is a call to the function using a value instead of a variable. This isn't stored in a variable 
# itself, so to change the output of the function you would have to change the number you are feeding 
# into the function; in this case you would have to change the 150 to another number.
_weight_on_moon(150)

# You can also feed expressions into the function as a variable, or even put the expression 
# inside of the variable above and it will properly work! It will execute the expression first and
# do the math following PEMDAS, and afterwards it will run the function passing the result in to the
# function. In the below example, it will pass 130 in to the function. 
_weight_on_moon(360 / 2)

# EXAMPLE 3

# If you try using the local variable _moon_weight, you will encounter a 'NameError' that tells you
# that _moon_weight is undefined. This is because you can only access local variable from the scope,
# or position within the code, that they are defined in. 

# In this example, the only place you can actually access, modify, or interact with _moon_weight 
# is within the _weight_on_moon function itself. Uncomment the below print statement to see the error.
#print(_moon_weight)

# EXAMPLE 4

# In the same way that _moon_weight is inaccessible from outside of the function it is defined in, 
# _weight is also inaccessible for the same reasons. It is a locally defined variable, defined in
# the creation of the function parameters itself, and is only accessible from within the function
# itself. 

# If you were to try to access _weight from outside of the function, like below, it will give you 
# the same error as trying to access _moon_weight. It is not defined in the scope you are trying to use,
# and needs to be defined.
#print(_weight_)

# EXAMPLE 5

_moon_weight = 250

print(_moon_weight)

# In the above example, I have defined a variable named _moon_weight outside of the function where 
# it is defined locally. Because they are defined in two different places, they are considered 
# two different variables when it comes to code execution. 

# Changing the _moon_weight variable defined just above will not affect the _moon_weight local variable inside
# of the function above, and changing the local variable in the function itself will not affect 
# the variable defined above for example 5. 

# They both run seperately from eachother and do not interact in any way because of the scope they are on.

# Scope is basically the region in which code is created and accessible.

# There is the GLobal Scope, which is anything defined outside of functions. An example of Global Scope
# is the variable _earth_weight at the top of this script. It is not defined inside of a function, and 
# is defined inside of the script itself. This means that it is globally accessible from anywhere
# within the code. 

# There is also the Local scope, which is anything defined inside of functions. An example of Local Scope
# is the variable _moon_weight defined INSIDE the function above, not the one defined outside for 
# example 5. 

# There is more to scope, such as being able to define a global variable from within a function itself.
# This isn't relevant to the subject at hand though, but it is possible to globally define a variable
# from inside of a function's local scope and access it from outside of the function itself.

# W3 Schools has a really good explanation of Scope that I'm probably not doing justice here, so I will
# make sure to link it for anybody to read that wishes to do so. 
# https://www.w3schools.com/python/python_scope.asp