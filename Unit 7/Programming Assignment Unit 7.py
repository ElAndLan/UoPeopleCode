alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

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
    _dict = dict()
    
    for char in s:
        if char in _dict:
            print(char)
            return True
        _dict[char] = True

    return False



print(has_duplicates(test_dups))