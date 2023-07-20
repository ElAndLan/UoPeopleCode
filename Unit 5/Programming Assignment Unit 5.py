import math

def my_sqrt(a):
    x = 4.5
    while True:
     y = (x + a/x) / 2.0
     if y == x:
          break
     x = y
     return x


def test_sqrt(num):
     while num > 0: 
          print(f"num = {num} | my_sqrt(num) = {my_sqrt(num)} | math.sqrt(num) = {math.sqrt(num)} | diff = {abs(my_sqrt(num) - math.sqrt(num))}")
          num -= 1
     
test_sqrt(25)