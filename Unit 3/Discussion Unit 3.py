# Describe the difference between a chained conditional and a nested conditional. Give your own example of each. Do not copy examples from the textbook.

'''

A chained conditional is when multiple conditionals are all chained on the same scope/indentation level instead of spacing them out individually.

In the greet_neighbor_chained example below, it has a single if statement that uses chained conditionals to check if the neighbor is named John, and if the neighbor is outside.

'''

def greet_neighbor_chained(_neighbor_name, _is_outside, _is_weather_good): 
    if _neighbor_name == "John" and _is_outside and _is_weather_good:
        print(f"Hello, {_neighbor_name}! This is great weather we're having isn't it?")

print(" ")
greet_neighbor_chained("John", True, True)
print(" ")
        
'''

A nested conditional is when multiple conditionals are used but on different scopes/indentation levels. This leads to sloppy, hard to read conditionals.

In the greet_neighbor_nested example below, it has the same conditionals as above but instead of chaining them together to make everything neat and tidy, they are instead 
nested inside of eachother. This makes things overly complicated and hard to read, especially on larger scales where there's a lot more code to read.

'''

def greet_neighbor_nested(_neighbor_name, _is_outside, _is_weather_good): 
    if _neighbor_name == "Alyssa":
        if _is_outside:
            if _is_weather_good:
                print(f"Hello, {_neighbor_name}! This is great weather we're having isn't it?")

greet_neighbor_nested("Alyssa", True, True)
print(" ")


'''

Below is an example of another nested-conditional function that can be reformatted into a chained conditional rather than having sloppy, hard to read nested conditionals.

You'll notice that for this example, because everything is nested inside of eachother it not only makes it more complicated to read and go through, but it adds a LOT of code
that just isn't necessary. 

There's 4 different IF statements, and 4 different ELSE's for each of those if statements. This is incredibly sloppy and inefficient, especially on a big project with 
thousands, or tens of thousands of lines of code.

'''

def is_it_storming(_is_raining, _is_lightning, _is_thunder, _is_windy):
    if _is_windy:
        if _is_raining:
            if _is_lightning:
                if _is_thunder:
                    print ("There is a storm outside! Be careful!")
                else: 
                    print("There is no storm outside, it is safe to go play!")
            else: 
                    print("There is no storm outside, it is safe to go play!")
        else: 
                    print("There is no storm outside, it is safe to go play!")
    else: 
        print("There is no storm outside, it is safe to go play!")
        
is_it_storming(True, True, True, True)
is_it_storming(True, False, True, True)
print(" ")

'''

Below is a simplified version, with chained conditionals instead of nested conditionals.  It is all contained within 5 lines of code total, including the function declaration.

Compared to the above example, taking up 14 lines of code just to do the same thing as the function below using 5 lines. 

This simplified version is much easier to read, much more efficient and overall better.

'''

def is_it_storming(_is_raining, _is_lightning, _is_thunder, _is_windy):
    if _is_windy and _is_raining and _is_lightning and _is_thunder:
        print ("There is a storm outside! Be careful!")
    else:
        print("There is no storm outside, it is safe to go play!")
    
is_it_storming(True, True, True, True)
is_it_storming(True, False, True, True)