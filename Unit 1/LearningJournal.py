print("- - - - - - - - - - - - -")
print("- - - 1.9 Exercises - - -")
print(" ")


# B -  If you are trying to print your name, what happens if you
# leave out one of the quotation marks or both and why?

# print("What happens if you leave out one quote?)
# print(What happens if you leave out one quote?")
# If you leave out one quotation mark, you get "Unterminated string literal"
# telling you that the string is "unterminated", or not ended with a closing
# quote.


# print(Or both quotes?)
# Leaving out both quotation marks give you a 'Invalid Syntax' SyntaxError
# and suggests you might have forgotten a comma, even though it's quotation
# marks forgotten in this scenario.


# C - What is the difference between * and ** operators in Python?
# Explain with the help of an example.

# In Python, a single asterisk (*) is used to do multiplication in mathematical
# equations.
# print(5 * 2)
# The above will output 10.
# In Python, a double asterisk(**) is used to represent exponents.
# print(5**2)
# The above will output 25.

# D -  In Python, is it possible to display an integer like 09?
# Justify your answer.
# print(01)
# No you cannot, because it gives you a SyntaxError and warns you that
# leading Zero's are not permitted and to use 0o prefixes for octal integers.

# E - Run the commands type('67') and type(67).
# What is the difference in the output and why?
# print(type('67'))
# print(type(67))
# The first one, '67', will return a type of string because it is interpreted
# as a string due to the single quotes around the number.
# The second one, 67, will return a type of int because it is seen as a number
print(" ")

_age = 31
_new_age = _age * 2
print("A) My age doubled is: " + str(_new_age) + ".")

_city = "Reading, Pennsylvania"
_country = "United States of America"
_continent = "North America"
print("B) I live in " + _city + " in the " +
      _country + " in " + _continent + ".")

_start_of_term = "June 15th"
_end_of_term = "August 13th"
print("C) The term started on " + _start_of_term +
      " and ends on " + _end_of_term + ".")

_reading_temp = 74

print("D) The temperature in " + _city + " is: " + str(_reading_temp) + "F.")
