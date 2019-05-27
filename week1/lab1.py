#################################################
# Lab1
#################################################

import cs112_s17_linter
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Lab1 problems
#################################################

def nearestOdd(n):
    int_n = int(n)

    def isOdd(n):
        if n % 2 == 1: return True
        return False
    def isEven(n):
        if n % 2 == 0: return True
        return False

    if isEven(n): return n - 1

    if isOdd(int_n): 
        return int_n
    elif n > 0: 
        return int_n + 1
    else:
        return int_n - 1

def rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    # def isXOvl(x1,x2):
    #     def isP1Left(x1,x2):
    #         return x1 < x2
    #     if isP1Left(x1,x2):
    #         return x1 + w1 >= x2
    #     else: return x2 + w2 >= x1

    # def isYOvl(y1,y2):
    #     def isP1Up(y1,y2):
    #         return y1 < y2
    #     if isP1Up(y1,y2):
    #         return y1 + h1 >= y2
    #     else: return y2 + h2 >= y1

    # simple version about above
    def isOvl(x1,x2,inc1,inc2):
        if x1 < x2: return x1 + inc1 >= x2
        else: return x2 + inc2 >= x1

    return isOvl(x1,x2,w1,w2) and isOvl(y1,y2,h1,h2)


def isPerfectSquare(n):
    if not isinstance(n, int) or n < 0: return False
   
    # I just don't know how to make it without recursion or loop..
    # so I just make a loop version about this question
    # n >= 2 case
    index = 0
    perfectNum = 0
    while True:
        if perfectNum == n:
            return True
        elif perfectNum > n:
            return False
        else:
            perfectNum = perfectNum + 2*index + 1
            index += 1


def getKthDigit(n, k):
    return abs(n) // 10**k % 10

def setKthDigit(n, k, d):
    isNeg = False
    if n < 0 : 
        n = -n
        isNeg = True

    memo = n % 10**k
    Appendix  = n // 10**k

    newApp = Appendix // 10 * 10 + d
    result = newApp * 10**k + memo

    if isNeg:
        result = -result
    return result

def riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent):
    def quad(a,b,c):
        j = (b**2 - 4*a*c)**(1/2)
        if -b + j >= 0: return (-b+j)/(2*a)
        return (-b-j)/(2*a)
    a = totalTime
    b = -totalDistance
    c = -totalTime * riverCurrent**2
    cruiseSpeed = quad(a,b,c)

    return (totalDistance/2)/(cruiseSpeed - riverCurrent)

#################################################
# Lab1 Test Functions
################################################

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    print('Passed.')

def testRectanglesOverlap():
    print('Testing rectanglesOverlap()...', end='')
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3,4,5,6) == False)
    print('Passed.')

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(1234**2) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(17) == False)
    assert(isPerfectSquare(-16) == False)
    assert(isPerfectSquare(1234**2+1) == False)
    assert(isPerfectSquare(1234**2-1) == False)
    assert(isPerfectSquare(4.0000001) == False)
    assert(isPerfectSquare('Do not crash here!') == False)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed.')

def testRiverCruiseUpstreamTime():
    print('Testing riverCruiseUpstreamTime()... ', end='')
    # example from the source notes:
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 2 # km/hour
    assert(almostEqual(riverCruiseUpstreamTime(totalTime,
                                               totalDistance,
                                               riverCurrent),
                       1.7888736053508778)) # 1.79 in notes
    # another simple example
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 0 # km/hour
    assert(almostEqual(riverCruiseUpstreamTime(totalTime,
                                               totalDistance,
                                               riverCurrent),
                       1.5))
    assert(almostEqual(riverCruiseUpstreamTime(4,56,2),2.2801098892805185))
    print('Passed.')

#################################################
# Lab1 Main
################################################

def testAll():
    testNearestOdd()
    testRectanglesOverlap()
    testIsPerfectSquare()
    testGetKthDigit()
    testSetKthDigit()
    testRiverCruiseUpstreamTime()

def main():
    # bannedTokens = (
    #     #'False,None,True,and,assert,def,elif,else,' +
    #     #'from,if,import,not,or,return,' +
    #     'as,break,class,continue,del,except,finally,for,' +
    #     'global,in,is,lambda,nonlocal,pass,raise,repr,' +
    #     'try,while,with,yield,' +
    #     #'abs,all,any,bool,chr,complex,divmod,float,' +
    #     #'int,isinstance,max,min,pow,print,round,sum,' +
    #     '__import__,ascii,bin,bytearray,bytes,callable,' +
    #     'classmethod,compile,delattr,dict,dir,enumerate,' +
    #     'eval,exec,filter,format,frozenset,getattr,globals,' +
    #     'hasattr,hash,help,hex,id,input,issubclass,iter,' +
    #     'len,list,locals,map,memoryview,next,object,oct,' +
    #     'open,ord,property,range,repr,reversed,set,' +
    #     'setattr,slice,sorted,staticmethod,str,super,tuple,' +
    #     'type,vars,zip,importlib,imp,string,[,],{,}')
    # cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
