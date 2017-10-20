

# all the computations for HW 1 shall be done using binary arithmetic
# only the user input and the final output will be in decimal.
# dec2bin and bin2dec convert between binary and decimal.

# functions provided: Add, Mult, Divide and many supporting functions such as
# Compare to compare two unbounded integers, bin2dec and dec2bin etc.

# missing functions: subtraction, exp, gcd, Problem1, Problem2, Problem3 and the main function
# for user interface

########################################################
### SAMPLE INPUT/OUTPUT                              ###
########################################################
# Problem1
# Inputs: 99,101,101,99
# Output: 3621042145110495340304913321770092884828963481118630680783443137199360424701178235489444339150903695510140270221458360654677736177726261420668704432019096568923217654887729426654819147812495289601990198

# Problem1
# Inputs: 101,100,102,101
# Output: -73624909023231670869261708087644352879856062771895622746310308401235838873720979357266761267201142320719562605934027588808477220968934718015196126899431090054281838673459558997083139194957867884875198351

# Problem2
# Inputs: 921,97,376,49
# Output: Quotient: 223346796471162164452913306468608511973357088088077011223389370777657713512498752849853123746821473506392127360180733334528455377517683142902106402854175807704081
#         Remainder: 868589458788803459890025777897148259540992011101528169885851420031124037456917859918715079950453053934476646860356569316780185

# Problem3
# Input: 71
# Output: Numerator: 3028810706851429109067025637383
#         Denominator: 624893729741902836283505236800
#>>>
##########################################################

import random
import sys
import time


sys.setrecursionlimit(10000000)

from random import *

def shift(A, n):
    if n == 0:
        return A
    return [0]+shift(A, n-1)

def mult(X, Y):
    # mutiplies two arrays of binary numbers
    # with LSB stored in index 0
    if zero(Y):
        return [0]
    Z = mult(X, div2(Y))
    if even(Y):
        return add(Z, Z)
    else:
        return add(X, add(Z, Z))

def Mult(X, Y):
    X1 = dec2bin(X)
    Y1 = dec2bin(Y)
    return bin2dec(mult(X1,Y1))

def zero(X):
    # test if the input binary number is 0
    # we use both [] and [0, 0, ..., 0] to represent 0
    if len(X) == 0:
        return True
    else:
        for j in range(len(X)):
            if X[j] == 1:
                return False
    return True

def div2(Y):
    if len(Y) == 0:
        return Y
    else:
        return Y[1:]

def even(X):
    if ((len(X) == 0) or (X[0] == 0)):
        return True
    else:
        return False


def add(A, B):
    A1 = A[:]
    B1 = B[:]
    n = len(A1)
    m = len(B1)
    if n < m:
        for j in range(len(B1)-len(A1)):
            A1.append(0)
    else:
        for j in range(len(A1)-len(B1)):
            B1.append(0)
    N = max(m, n)
    C = []
    carry = 0
    for j in range(N):
        C.append(exc_or(A1[j], B1[j], carry))
        carry = nextcarry(carry, A1[j], B1[j])
    if carry == 1:
        C.append(carry)
    return C


def Add(A,B):
    return bin2dec(add(dec2bin(A), dec2bin(B)))

def exc_or(a, b, c):
    return (a ^ (b ^ c))

def nextcarry(a, b, c):
    if ((a & b) | (b & c) | (c & a)):
        return 1
    else:
        return 0

def bin2dec(A):
    if len(A) == 0:
        return 0
    val = A[0]
    pow = 2
    for j in range(1, len(A)):
        val = val + pow * A[j]
        pow = pow * 2
    return val

def reverse(A):
    B = A[::-1]
    return B

def trim(A):
    if len(A) == 0:
        return A
    A1 = reverse(A)
    while ((not (len(A1) == 0)) and (A1[0] == 0)):
        A1.pop(0)
    return reverse(A1)


def compare(A, B):
    # compares A and B outputs 1 if A > B, 2 if B > A and 0 if A == B
    A1 = reverse(trim(A))
    A2 = reverse(trim(B))
    if len(A1) > len(A2):
        return 1
    elif len(A1) < len(A2):
        return 2
    else:
        for j in range(len(A1)):
            if A1[j] > A2[j]:
                return 1
            elif A1[j] < A2[j]:
                return 2
        return 0

def Compare(A, B):
    return bin2dec(compare(dec2bin(A), dec2bin(B)))



def dec2bin(n):
    if n == 0:
        return []

    m = (n // 2)
    A = dec2bin(m)
    fbit = n % 2
    return [fbit] + A

def map(v):
    if v==[]:
        return '0'
    elif v ==[0]:
        return '0'
    elif v == [1]:
        return '1'
    elif v == [0,1]:
        return '2'
    elif v == [1,1]:
        return '3'
    elif v == [0,0,1]:
        return '4'
    elif v == [1,0,1]:
        return '5'
    elif v == [0,1,1]:
        return '6'
    elif v == [1,1,1]:
        return '7'
    elif v == [0,0,0,1]:
        return '8'
    elif v == [1,0,0,1]:
        return '9'

def bin2dec1(n):
    if len(n) <= 3:
        return map(n)
    else:
        temp1, temp2 = divide(n, [0,1,0,1])
        return bin2dec1(trim(temp1)) + map(trim(temp2))

def divide(X, Y):
    # finds quotient and remainder when A is divided by B
    if zero(X):
        return ([],[])
    (q,r) = divide(div2(X), Y)
    q = add(q, q)
    r = add(r, r)
    if (not even(X)):
        r = add(r,[1])
    if (not compare(r,Y)== 2):
        r = sub(r, Y)
        q = add(q, [1])
    return (q,r)

def Divide(X, Y):
    (q,r) = divide(dec2bin(X), dec2bin(Y))
    return (bin2dec(q), bin2dec(r))

def primality3( n, k ):
    bn = dec2bin(n)
    bk = dec2bin(k)
    if (divide(bn,[0,1])[1] == []) or (divide(bn,[1,1])[1] == []) or (divide(bn,[1,0,1])[1] == []) or (divide(bn,[1,1,1])[1] == []):
        return 'no'
    return primality2(n,k)

def primality2(n,k):
    for j in range(k):
       if(primality(n) == False):
           return 'no'

    return 'yes'


def primality(n):
    if n == 1:
        return True
    a = randrange(1,n)

    r = ( a**(n-1) - 1 ) % n
    if r == 0:
        return True
    else:
        return False



def gcd(X, Y):
    if (zero(Y) or (compare(X, Y) == 0)):
        return X
    if compare(X, Y) == 2:
        return gcd(Y, X)
    else:
        temp_X = bin2dec(X)
        temp_Y = bin2dec(Y)
        temp_mod = temp_X%temp_Y
        mod = dec2bin(temp_mod)
        return gcd(Y, mod)


def twosComp(X):
    for j in range(len(X)):
        X[j] = ( X[j] ^ 1 )
    X = add( X, [1] )
    return X
'''
def twos2dec(X):
    X = sub( X, [1] )
    for j in range( len(X) ):
        X[j] = ( X[j] ^ 1 )
    return X
'''

def sub(X, Y):
    if( compare( X, Y ) == 0 ):
        return [0]
    (X, Y) = samelen( X, Y )
    nY = twosComp(Y)
    return add( X, nY )


def samelen(X, Y):
    if( len(X) < len(Y) ):
        for j in range( ( len(Y) - len(X) ) ):
            X.append(0)
    elif( len(Y) < len(X) ):
        for j in range( ( len(X) - len(Y) ) ):
            Y.append(0)
    return (X, Y)




def floor( X, Y ):
    return ( dec2bin( bin2dec( X ) // bin2dec( Y ) ) )

def mod( X, Y ):
    return ( dec2bin( bin2dec( X ) % bin2dec( Y ) ) )
'''
def egcd(X,Y,r):
    if( zero( X ) ):
        return X
    elif ( (zero(Y) ) ):
        return ([1],[0],X,0)

    (xp,yp,d,s) = egcd(Y, mod( X, Y ), r)


    return ( yp, twoscomp( xp, mult( floor( X, Y ), yp ) ), d)
'''
def eegcd(a,b):
    if zero(b):
        return ([1],[0],a)
    ( x, y, d ) = eegcd( b, divide(a,b)[1] )

    yPrime = twosComp( mult( twosComp(y) , divide( a , b )[0]  ) )

    return (y, sub( x, yPrime ), d)

#(y*(a//b))
def nbprime(n):
    A = [1] + [randrange(2) for x in range( n - 2 )] + [1]

    return A

def rnbit(n):
    return [randrange(2) for x in range(n)]


def rsa(n,k):
    p = nbprime(n,k)
    q = nbprime(n,k)
    N = mult(p,q)
    E = rnbit(n)
    p1 = sub(p,[1])
    q1 = sub(q,[1])
    pq1 = mult(p1,q1)
    tgcd = [0]
    while( bin2dec(tgcd) is not 1):
        tgcd = gcd(E,pq1)
        if tgcd is not 1:
            E = rnbit(n)


    return tgcd , pq1 , E

def problem2(n,k):
    print( time.asctime( time.localtime(time.time())) )
    if n > 50:
        return ('n must be less than 50',n)
    v = nbprime(n)
    while primality3( bin2dec(v), k ) == 'no':
        v = nbprime(n)
    print( time.asctime( time.localtime(time.time())) )
    return v



if __name__ == "__main__":
    print("hi")
