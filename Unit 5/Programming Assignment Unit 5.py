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
     _my_sqrt = my_sqrt(num)
     _sqrt = math.sqrt(num)
     print(f"num = {num} | my_sqrt(num) = {_my_sqrt} | math.sqrt(num) = {_sqrt} | diff = {abs(_my_sqrt - _sqrt)}")
     
test_sqrt(1)
test_sqrt(2)
test_sqrt(3)
test_sqrt(4)
test_sqrt(5)
test_sqrt(6)
test_sqrt(7)
test_sqrt(8)
test_sqrt(9)
test_sqrt(10)
test_sqrt(11)
test_sqrt(12)
test_sqrt(13)
test_sqrt(14)
test_sqrt(15)
test_sqrt(16)
test_sqrt(17)
test_sqrt(18)
test_sqrt(19)
test_sqrt(20)
test_sqrt(21)
test_sqrt(22)
test_sqrt(23)
test_sqrt(24)
test_sqrt(25)