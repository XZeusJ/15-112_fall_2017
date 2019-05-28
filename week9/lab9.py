#################################################
# Lab9
#
# No iteration! no 'for' or 'while'.  Also, no 'zip' or 'join'.
# You may add optional parameters
# You may use wrapper functions
#
#################################################

from cs112_f16_wk9 import assertEqual, assertAlmostEqual, lintAll, testAll

import functools, math

def almostEqual(x, y, epsilon = 10**-8):
    return abs(x-y) < epsilon

##############################################
# alernatingSum(L)
##############################################

def alternatingSum(L):
    return 42

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    print('Passed.')

##############################################
# powerSum(n, k)
##############################################

def powerSum(n, k):
    return 42

def testPowerSum():
    print('Testing powerSum()...', end='')
    assert(powerSum(4, 6) == 1**6 + 2**6 + 3**6 + 4**6)
    assert(powerSum(0, 6) == 0)
    assert(powerSum(4, 0) == 1**0 + 2**0 + 3**0 + 4**0)
    assert(powerSum(4, -1) == 0)
    print('Passed.')

##############################################
# powersOf3ToN(n)
##############################################

def powersOf3ToN(n):
    return 42

def testPowersOf3ToN():
    print('Testing powersOf3ToN()...', end='')
    assert(powersOf3ToN(-42) == None)
    assert(powersOf3ToN(0.99) == None)
    assert(powersOf3ToN(1) == [1])
    assert(powersOf3ToN(3) == [1, 3])
    assert(powersOf3ToN(8.9999) == [1, 3])
    assert(powersOf3ToN(9) == [1, 3, 9])
    assert(powersOf3ToN(9.1111) == [1, 3, 9])
    assert(powersOf3ToN(100) == [1, 3, 9, 27, 81])
    print('Passed.')

##############################################
# myJoin(L, sep)
##############################################

def myJoin(L, sep):
    # You may only use reduce, map, and lambda here
    # and this must be one line only!
    return 42

def testMyJoin():
    print('Testing myJoin()...', end='')
    assert(myJoin(["a", "b", "c"], "-") == "a-b-c")
    assert(myJoin([1, 2, 3], "@@") == "1@@2@@3")
    assert(myJoin([1, 2, 3, 4], "") == "1234")
    assert(myJoin([42], "") == "42")
    print('Passed.')

##############################################
# myCount(fn, L)
##############################################

def myCount(fn, L):
    # You may only use reduce, filter, and lambda here
    # and this must be one line only!
    return 42

def testMyCount():
    print('Testing myCount()...', end='')
    assert(myCount(lambda val: val==1, [1, 2, 0, 1, 2, 3, 1, 4]) == 3)
    assert(myCount(lambda val: val==5, [1, 2, 0, 1, 2, 3, 1, 4]) == 0)
    L = ["wow", 42, "no way!", 99, 3.14159]
    assert(myCount(lambda val: isinstance(val, int), L) == 2)
    print('Passed.')

##############################################
# Line class
##############################################

'''
Line class
Write the Line class so that it passes testLineClass, and
uses the OOP constructs we learned this week as appropriate.
'''

class Line(object):
    pass

def testLineClass():
    print('Testing Line class...', end='')
    assert(str(Line(2,5))  == "y=2x+5")
    assert(str(Line(2,-5)) == "y=2x-5")
    assert(str(Line(0,5))  == "y=5")
    assert(str(Line(1,5))  == "y=x+5")
    assert(str(Line(-1,5)) == "y=-x+5")
    assert(str(Line(0,-5)) == "y=-5")
    assert(str(Line(0,0))  == "y=0")

    line1 = Line(2,3)
    assert(str(line1) == "y=2x+3")
    assert(line1.getSlope() == 2)
    assert(type(line1.getSlope()) == int)
    assert(line1.getIntercept() == 3)
    line2 = Line(6,-5)
    assert(str(line2) == "y=6x-5")
    assert(line2.getSlope() == 6)
    assert(line2.getIntercept() == -5)

    (x,y) = line1.getIntersection(line2) # (2, 7)
    assert(almostEqual(x, 2) and almostEqual(y, 7))

    line3 = Line(2, -3)
    (x,y) = line3.getIntersection(line2) # (0.5, -2)
    assert(almostEqual(x, 0.5) and almostEqual(y, -2))

    # parallel lines do not intersect
    assert(Line(2,3).getIntersection(Line(2,4)) == None)

    assert(line3.isParallelTo(line1) == True)
    assert(line3.isParallelTo(line2) == False)

    # getHorizontalLine returns a line that is horizontal
    # to the given line, intersecting at the given x value.
    line4 = line3.getHorizontalLine(4)
    assert(str(line4) == "y=5")
    assert(line4.getSlope() == 0)
    assert(line4.getIntercept() == 5)
    
    assert(Line(1, 2) == Line(1, 2))
    assert(Line(1, 2) != Line(1, 3))
    assert(not (Line(1, 2) == "don't crash here!"))

    s = set()
    assert(Line(1, 2) not in s)
    s.add(Line(1, 2))
    assert(Line(1, 2) in s)
    s.remove(Line(1, 2))
    assert(Line(1, 2) not in s)

    print('Passed.')

##############################################
# testAll and main
##############################################

def testAll():
    testAlternatingSum()
    testPowerSum()
    testPowersOf3ToN()
    testMyJoin()
    testMyCount()
    testLineClass()

def main():
    lintAll()
    testAll()

if (__name__ == '__main__'):
    main()
