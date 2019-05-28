#################################################
# Lab3
#################################################

import cs112_s17_linter
import math, string

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
# Exercises
#################################################

def longestCommonSubstring(s1, s2):
    return 42

def encodeRightLeftCipher(text, rows):
    return 42

def decodeRightLeftCipher(cipher):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed!")

def testEncodeRightLeftCipher():
    print("Testing encodeRightLeftCipher()...", end="")
    text = "WEATTACKATDAWN"
    rows = 4
    # W T A W
    # E A T N
    # A C D z
    # T K A y
    rightLeft = "4"+"WTAWNTAEACDzyAKT"
    cipher = encodeRightLeftCipher(text, rows)
    assert(rightLeft == cipher)
    print("passed!")

def testDecodeRightLeftCipher():
    print("testing decodeRightLeftCipher()...", end="")
    text = "WEATTACKATDAWN"
    rows = 6
    cipher = encodeRightLeftCipher(text, rows)
    plaintext = decodeRightLeftCipher(cipher)
    assert(plaintext == text)
    print("passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testLongestCommonSubstring()
    testEncodeRightLeftCipher()
    testDecodeRightLeftCipher()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        #'break,continue,for,in,while,' +
        'as,class,del,except,finally,' +
        'global,is,lambda,nonlocal,pass,raise,repr,' +
        'try,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        #'range,reversed,str,string,[,],ord,chr,input,len'+
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,issubclass,iter,' +
        'list,locals,map,memoryview,next,object,oct,' +
        'open,property,repr,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'type,vars,zip,importlib,imp,{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
