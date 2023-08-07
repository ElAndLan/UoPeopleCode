import json

'''
Line 1 imports the library json to make importing a dictionary easier.

The first with open Opens Moons.json in Read mode as _moons, then inside of that it creates a variable
named _moon_list and loads the dictionary from _moons (AKA Moons.json) and assigns the value of that
to _moon_list
'''
with open('./Unit 8/Moons.json', 'r') as _moons:
    _moon_list = json.load(_moons)

'''
By feeding a dictionary of key/value pairs, where the values are lists of values, the invert_dict
function will invert the dictionary and return the values with the key associated with them.

First, it loops over the dictionary, then for each list of values in that key of the dictionary, it loops
over the values and checks to see if it is already in the _inverse dictionary. 

If they are not, it adds them to the dict and if they are it appends them to it.
'''

def invert_dict(d):
    _inverse = dict()
    for key in d:
        _value = d[key]
        for item in _value:
            if item not in _inverse:
                _inverse[item] = [key]
            else : _inverse[item].append(key)
    return _inverse


'''
The second with open below creates a file Results.json with Write enabled, and assigns the file to the fp
variable.

Then json.dump writes the dictionary that has been inverted to the Results.json file.
'''
with open('./Unit 8/Results.json', 'w') as fp:
    json.dump(invert_dict(_moon_list), fp)