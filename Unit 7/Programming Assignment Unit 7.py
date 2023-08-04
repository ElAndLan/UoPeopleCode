alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics", ] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 

 
def has_duplicates(s):
    _histogram = histogram(s)
    
    for key, value in _histogram.items():
        if value > 1: 
            return True

    return False



for item in test_dups:
    if has_duplicates(item):
        print(item, 'has duplicates')
    else: print(item, 'has no duplicates detected.')
    
def missing_letters(s):
    _histogram = histogram(s)
    _missing = []
    
    for char in alphabet:
        if char not in _histogram:
            _missing.append(char)
            
    return ''.join(_missing)

for item in test_miss:
    _missing = missing_letters(item)
    if len(_missing):
        print (item, 'is missing letters', _missing)
    else: print(item, 'uses all the letters.')
    