#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#
#  Solutions to a few problems on Project Euler
#
#
import numpy as np
from util_euler import MeasureTime


# Problem 1
@MeasureTime
def SumOfMultiples(n):
    s = 0
    i = 3
    j = 5
    while i < n:
        s += i
        i += 3
        if j < n:
            if j % 3:
                s += j
            j += 5
    return s


@MeasureTime
def SumOfMultiples2(n):
    return sum([i for i in xrange(int(n)) if (i % 3 == 0) or (i % 5 == 0)])


# Problem 2
@MeasureTime
def SumOfFibonacci(up):
    if up < 2:
        return 0
    ele_one = 1
    ele_two = 2
    sumval = 2
    while ele_two <= up:
        ele_two = ele_one + ele_two
        ele_one = ele_two - ele_one
        if not ele_two % 2:
            sumval += ele_two
    return sumval


# Problem 3 (largest prime factor)

@MeasureTime
def PrimeFactors(n):
    num = n
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num = num // 2
    i = 3
    while num > 1:
        if num % i == 0:
            factors.append(i)
            num = num // i
            i = 3
        else:
            i += 2
            if i > np.sqrt(num):
                factors.append(num)
                break
    return factors


# Problem 4 (largest palindrome product)

def IsPalindromeString(n):
    return str(n) == str(n)[::-1]


# tests the leading and trailing digits against each other, should be most efficient algorithm in both space and time
def IsPalindrome(n):
    div = 1
    while n // div >= 10:
        div *= 10
    while n != 0:
        lead = n // div
        trail = n % 10
        if lead != trail:
            return False
        n = (n % div) // 10
        div = div // 100
    return True


@MeasureTime
def LargestPalindromeProd(nup, nlow=1):
    pal = 0
    for i in xrange(nup, nlow - 1, -1):
        for j in xrange(nup, i - 1, -1):
            if IsPalindromeString(i * j):
                pal = i * j
                break
        if pal > 0:
            break
    # now we have the first palindrome and the numbers i, j
    # either it's the largest palindrome or there is a larger one at x * y, with x * y > i * j
    low = (i * j) // nup
    for i in xrange(low, nup + 1):
        for j in xrange(nup, i + 1, -1):
            if i * j <= pal:
                break
            if IsPalindromeString(i * j):
                pal = i * j
    return pal


# Problem 5 (smallest multiple)
@MeasureTime
def LowestCommonMultiple(divup):
    # find prime factors
    facs = range(1, divup + 1)
    for i in xrange(len(facs)):
        for j in xrange(i + 1, len(facs)):
            if facs[j] % facs[i] == 0:
                facs[j] = facs[j] // facs[i]
    return reduce(lambda a,b: a * b, facs)


# Problem 6 (sum square difference)
@MeasureTime
def SumSquareDiff(n):
    sqsumn = (n * (n + 1) / 2) ** 2
    sumnsq = n * (n + 1) * (2 * n + 1) / 6  # can be derived with induction for example see wiki (Faulhaber's formula)
    return sqsumn - sumnsq


# Problem 7 (10001st prime)
@MeasureTime
def NthPrime(n):
    import numpy as np

    if n < 1:
        return 0
    if n < 2:
        return 2

    count = 1
    i = 3
    while count < n:
        prime = True
        for j in xrange(3, int(np.sqrt(i) + 1), 2):
            if i % j == 0:
                prime = False
                break
        if prime:
            count += 1
        i += 2
    return i - 2


# Problem 8 (largest product in series)
series = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""


@MeasureTime
def LargestProduct(s, l=13):
    # remove line breaks and whitespace (somehow strip() doesn't work here)
    s = s.replace("\n", "")
    # s = s.replace(" ", "")
    print "Scanning {} digit number.".format(len(s))
    # split at occurring zeros, this is only helpful because we are looking for products of adjacent digits
    subs = s.split("0")
    # consider only long enough substrings
    subs = [sub for sub in subs if len(sub) >= l]
    # now, need to scan each remaining substring manually (I think...)
    maxprod = 0
    for sub in subs:
        val = reduce(lambda a, b: int(a) * int(b), sub[:l])
        if val > maxprod:
            maxprod = val
        # can insert some other heuristic here looking at remaining len(sub) - l digits
        # compared to the first ones and skip further computation if the number can never
        # reach maxprod
        i = 0
        # could also scan from left and right at the same time for better performance here
        while i < (len(sub) - l):
            val *= int(sub[l + i]) * 1. / int(sub[i])
            if val > maxprod:
                maxprod = val
            i += 1
            # small optimization to skip last check
            if i == (len(sub) - l - 1):
                if int(sub[i]) >= int(sub[-1]):
                    break
    return int(maxprod)


# Problem 9 (Pythagorean triplet)
@MeasureTime
def PythagoreanTriplet(sumval):
    # see calc. on paper
    for c in xrange(sumval / 3 + 1, sumval / 2):
        for b in xrange(c / 2, c):
            a = sumval - c - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c, [a, b, c]


# Problem 10 (Summation of primes)
# adjusted from earlier problem 7
@MeasureTime
def SumOfPrimes(n):
    import numpy as np

    if n < 1:
        return 0
    if n < 2:
        return 2

    s = 2
    i = 3
    while i < n:
        prime = True
        for j in xrange(3, int(np.sqrt(i) + 1), 2):
            if i % j == 0:
                prime = False
                break
        if prime:
            s += i
        i += 2
    return s


@MeasureTime
def SumOfPrimesSieve(n):
    """ Using simple sieve of erasthones. """
    import numpy as np

    nums = np.arange(2, n, 1, dtype=int)  # optimize step here? getting confusing afterwards though...
    sieve = np.ones(len(nums), dtype=bool)
    for i in xrange(len(nums)):

        if not sieve[i]:
            continue

        num = nums[i]
        if num > np.sqrt(n):
            break

        for j in xrange(num * num, int(n), num):
            sieve[j - 2] = False

    return np.sum(nums[sieve])


# Problem 11 (largest product in a grid)

grid = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

# pre-processing because too lazy to properly type matrix above
grid = grid.split("\n")
grid = [g1.split() for g1 in grid]
grid = np.asarray(grid, dtype=int)
# now matrix is 2d numpy array


@MeasureTime
def LargestProductInGrid(g, nn=4):
    # idea: use numpy tricks to create nn - 1 translated matrices and multiple them with the
    # original matrix to get a product matrix, have to repeat for each direction though (and diagonals are tricky)
    # seems very complicated, so maybe it's easier to just manually scan and keep maxima...
    pass


if __name__ == "__main__":
    print LargestProductInGrid(grid)

