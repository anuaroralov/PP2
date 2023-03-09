import math
import time
def test1(list):
    product=1
    for i in list:
        product*=i
    return product

def test2(string):
    lowerCase=len([i for i in string if i.islower()])
    upperCase=len([i for i in string if i.isupper()])
    return f"lowerCase- {lowerCase}\nupperCase- {upperCase}"

def test3(string):
    return string==string[::-1]

def test4(number,milliSec):
    time.sleep(milliSec/1000)
    return math.sqrt(number)

def test5(tuple):
    return all(tuple)
