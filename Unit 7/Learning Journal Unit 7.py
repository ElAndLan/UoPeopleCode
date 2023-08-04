_moons = {"Earth": ["Luna"], 
          "Mars": ["Phobos", "Deimos"], 
          "Jupiter": ["Io", "Europa", "Ganymede", "Callisto"], 
          "Saturn": ["Titan", "Enceladus"],
          "Uranus": ["Umbriel", "Titania", "Puck"],
          "Neptune": ["Triton", "Sao", "Hippocamp","Proteus"]}

'''
By feeding a dictionary of key/value pairs, where the values are lists of values, the invert_dict
function will invert the dictionary and return the values with the key associated with them.

First, it loops over the dictionary, then for each list of values in that key of the dictionary, it loops
over the values and checks to see if it is already in the _inverse dictionary. 

If they are not, it adds them to the dict and if they are it appends them to it.

This is useful as a concept in this example because you can find out exactly which planet the moons
belong to, and you could use it in other ways.

Replace the Planets with certain places, like chain restaurant names or university names, then for the 
list of values you could set them equal to the city/state/address where those different places are located.
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

print("The original dictionary is:")
print(_moons)
print(' ')
print("The inverted dictionary is:")
print(invert_dict(_moons))