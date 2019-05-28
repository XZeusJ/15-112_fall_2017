#################################################
# Hw9
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
# isHappyNumber(n)
##############################################

def isHappyNumber(n):
    return 42

def testIsHappyNumber():
    print('Testing isHappyNumber()...', end='')
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print('Passed.')

##############################################
# binarySearchValues(L, v)
##############################################

def binarySearchValues(L, v):
    return 42

def testBinarySearchValues():
    print('Testing binarySearchValues()...', end='')
    L = ['a', 'c', 'f', 'g', 'm', 'q']
    assert(binarySearchValues(L, 'a') == [(2,'f'), (0,'a')])
    assert(binarySearchValues(L, 'c') == [(2,'f'), (0,'a'), (1,'c')])
    assert(binarySearchValues(L, 'f') == [(2,'f')])
    assert(binarySearchValues(L, 'g') == [(2,'f'), (4, 'm'), (3, 'g')])
    assert(binarySearchValues(L, 'm') == [(2,'f'), (4, 'm')])
    assert(binarySearchValues(L, 'q') == [(2,'f'), (4, 'm'), (5, 'q')])
    assert(binarySearchValues(L, 'z') == [(2,'f'), (4, 'm'), (5, 'q')])
    assert(binarySearchValues(L, 'b') == [(2,'f'), (0,'a'), (1,'c')])
    print('Passed.')

##############################################
# evalPrefixNotation(L)
##############################################

def evalPrefixNotation(L):
    return 42

def testEvalPrefixNotation():
    print('Testing evalPrefixNotation()...', end='')
    assert(evalPrefixNotation([42]) == 42)
    assert(evalPrefixNotation(['+', 3, 4]) == 7)
    assert(evalPrefixNotation(['-', 3, 4]) == -1)
    assert(evalPrefixNotation(['-', 4, 3]) == 1)
    assert(evalPrefixNotation(['+', 3, '*', 4, 5]) == 23)
    assert(evalPrefixNotation(['+', '*', 2, 3, '*', 4, 5]) == 26)
    assert(evalPrefixNotation(['*', '+', 2, 3, '+', 4, 5]) == 45)
    assert(evalPrefixNotation(['*', '+', 2, '*', 3, '-', 8, 7,
                               '+', '*', 2, 2, 5]) == 45)
    raisedAnError = False
    try:
        evalPrefixNotation(['^', 2, 3])
    except:
        raisedAnError = True
    assert(raisedAnError == True)
    print('Passed.')

##############################################
# intPairsAsTuples(L)
##############################################

def intPairsAsTuples(L):
    return 42

def testIntPairsAsTuples():
    print('Testing intPairsAsTuples()..', end='')
    L = [ 1, 2, True, "wow!", (3, 4), [5, 6], [7, 8, 9]]
    assert(intPairsAsTuples(L) == ((3, 4), (5, 6)))
    L = [[1,2,3],True,[4],[5,"six"],[7,8], 8.5, "nine!",(10,11), "zz"]
    assert(intPairsAsTuples(L) == ((7,8),(10,11)))
    print('Passed.')

##############################################
# longestStrippedLine(lines)
##############################################

def longestStrippedLine(lines):
    return 42

def testLongestStrippedLine():
    print('Testing longestStrippedLine()...', end='')
    lines = """
    abc def
    ghij
    kl
    mnop qrst
    uv
    """
    assert(longestStrippedLine(lines) == 'mnop qrst')
    lines = '''
    This is a test.
    This is only a test.
    Wahoo.
    '''
    assert(longestStrippedLine(lines) == 'This is only a test.')
    print('Passed.')

##############################################
# Polynomial class
# (from http://www.kosbie.net/cmu/spring-14/15-112/handouts/hw9.html)
##############################################

class Polynomial(object):
    pass

def testPolynomialClass():
    print('Testing Polynomial class...', end='')
    testPolynomialBasics()
    testPolynomialEq()
    testPolynomialConstructor()
    testPolynomialInSets()
    print('Passed.')

def testPolynomialBasics():
    # we'll use a very simple str format...
    assert(str(Polynomial([1,2,3])) == "Polynomial(coeffs=[1, 2, 3])")
    p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5
    assert(p1.degree() == 2)
    # p.coeff(i) returns the coefficient for x**i
    assert(p1.coeff(0) == 5)
    assert(p1.coeff(1) == -3)
    assert(p1.coeff(2) == 2)
    # p.evalAt(x) returns the polynomial evaluated at that value of x
    assert(p1.evalAt(0) == 5)
    assert(p1.evalAt(2) == 7)
    # p.scaled(scale) returns a new polynomial with all the
    # coefficients multiplied by the given scale
    p2 = p1.scaled(10) # 20x**2 - 30x + 50
    assert(isinstance(p2, Polynomial))
    assert(p2.evalAt(0) == 50)
    assert(p2.evalAt(2) == 70)

def testPolynomialEq():
    assert(Polynomial([1,2,3]) == Polynomial([1,2,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,3,0]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,0,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,-2,3]))
    assert(Polynomial([1,2,3]) != 42)
    assert(Polynomial([1,2,3]) != "Wahoo!")
    # A polynomial of degree 0 has to equal the same non-Polynomial numeric!
    assert(Polynomial([42]) == 42)

def testPolynomialConstructor():
    # If the list is empty, treat it the same as [0]
    assert(Polynomial([]) == Polynomial([0]))
    assert(Polynomial([]) != Polynomial([1]))
    # Remove leading 0's
    assert(Polynomial([0,0,0,1,2]) == Polynomial([1,2]))
    assert(Polynomial([0,0,0,1,2]).degree() == 1)
    # Require that the constructor be non-destructive
    coeffs = [0,0,0,1,2]
    assert(Polynomial(coeffs) == Polynomial([1,2]))
    assert(coeffs == [0,0,0,1,2])
    # Require that the constructor also accept tuples of coefficients
    coeffs = (0, 0, 0, 1, 2)
    assert(Polynomial(coeffs) == Polynomial([1,2]))

def testPolynomialInSets():
    s = set()
    assert(Polynomial([1,2,3]) not in s)
    s.add(Polynomial([1,2,3]))
    assert(Polynomial([1,2,3]) in s)
    assert(Polynomial([1,2,3]) in s)
    assert(Polynomial([1,2]) not in s)

##############################################
# ignore_rest: place bonus below here!
##############################################

##############################################
# testAll and main
##############################################

def testAll():
    testIsHappyNumber()
    testBinarySearchValues()
    testEvalPrefixNotation()
    testIntPairsAsTuples()
    testLongestStrippedLine()
    testPolynomialClass()

def main():
    lintAll()
    testAll()

if (__name__ == '__main__'):
    main()
