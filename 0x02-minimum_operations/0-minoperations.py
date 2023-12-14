#!/usr/bin/python3
'''Minimum operations'''


def minOperations(n):
    '''
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    '''
    if not isinstance(n, int):
        return 0
    count = 0
    divisor = 2
    while (divisor <= n):
        if not (n % divisor):
            n = int(n / divisor)
            count += divisor
            divisor = 1
        divisor += 1
    return count
