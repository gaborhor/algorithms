import math
import random
import sys
from time import time

sys.setrecursionlimit(10**9)

def isPrime(p):
    max_divisor = int(round(math.sqrt(p),0))

    divisor_array = [i for i in range(2,max_divisor+1)]

    for i in reversed(divisor_array):
        if p % i == 0:
            return False
            exit()
    return True

    ## Recursive option that didn't work out:
    # def recursive_check(divisor):
    #     if divisor == 1:
    #         return True
    #     elif p % divisor == 0:
    #         return False
    #     else:
    #         return recursive_check(divisor-1)
    #
    # return recursive_check(i)

## Some test cases
# print(isPrime(29))
# print(isPrime(30))
# print(isPrime(31))
# print(isPrime(36))

def nBitPrime(n):
    multiplier = random.random()
    num_to_check = multiplier * (2**n)
    num_to_check = round(num_to_check, 0)

    if num_to_check == 1:
        return nBitPrime(n)
    elif isPrime(num_to_check) == True:
        return num_to_check
    elif isPrime(num_to_check) == False:
        return nBitPrime(n)

## Some test cases
# print(nBitPrime(3))
# print(nBitPrime(8))
# print(nBitPrime(16))
# print(nBitPrime(20))

def factor_and_time(pq):
    t1 = time()
    max_divisor = int(round(math.sqrt(pq),0))
    divisor_array = [i for i in range(1,max_divisor+1)]

    for i in reversed(divisor_array):
        if pq % i == 0:
            t2 = time()
            runtime = (t2 - t1) * 1000
            print(runtime)
            return (i, pq//i)
            exit()

## Some test cases
# PQ = nBitPrime(16) * nBitPrime(16)
# print(PQ)
# print(factor_and_time(PQ))
#
# PQ = nBitPrime(22) * nBitPrime(22)
# print(PQ)
# print(factor_and_time(PQ))
#
# vvvv Recursive factoring methods don't work below this point due to default
# ---- limits in python and integer size handling
#
# PQ = nBitPrime(23) * nBitPrime(23)
# print(PQ)
# print(factor_and_time(PQ))
#
# PQ = nBitPrime(24) * nBitPrime(24)
# print(PQ)
# print(factor_and_time(PQ))
#
# PQ = nBitPrime(25) * nBitPrime(25)
# print(PQ)
# print(factor_and_time(PQ))
#
# vvvv Hitting 1000+ ms as of here
# PQ = nBitPrime(26) * nBitPrime(26)
# print(PQ)
# print(factor_and_time(PQ))
#
# vvvv Regularly 3000+ ms here
# PQ = nBitPrime(27) * nBitPrime(27)
# print(PQ)
# print(factor_and_time(PQ))
#
# vvvv "Minimum" 3000 here, hitting ~16000 occasionally
# PQ = nBitPrime(28) * nBitPrime(28)
# print(PQ)
# print(factor_and_time(PQ))
#
#
# PQ = nBitPrime(30) * nBitPrime(30)
# print(PQ)
# print(factor_and_time(PQ))
#
#
# PQ = nBitPrime(32) * nBitPrime(32)
# print(PQ)
# print(factor_and_time(PQ))
#
# vvvv Seems to be functional endpoint for my PC. Memory capacity issues
# ---- related to the sheer size/number of numbers to operate on
# PQ = nBitPrime(33) * nBitPrime(33)
# print(PQ)
# print(factor_and_time(PQ))

## From plotting/fitting in Wolfram, we get the following time-estimates for cracking a 1024-bit key
##
## Time in Milliseconds = 1.066026167254143e+445
## There are approximately 3.154e+10 milliseconds per calendar year, which leads to...
## Time in Years = 3.389590356928912e+434
## This is clearly close enough to infinity, it will simply never be cracked by a standard computer