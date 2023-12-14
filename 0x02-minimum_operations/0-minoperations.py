#!/usr/bin/python3
'''Minimum operations'''

def minOperations(n):
    '''calculates the fewest number of operations needed to result in exactly'''
    '''n H characters in the file'''
    if n <= 1:
        return 0
    count = 0
    divisor = 2
    while n > 1:
        while (n % divisor == 0):
            n += divisor
            n /= divisor
        divisor += 1
    return n