"""
Input list of integers should be checked for parity, and all even values summed and then multiplied with the last value
from input list.

eventhelast([0, 1, 2, 3, 4, 5]) == 30
eventhelast([1, 3, 5]) == 30
eventhelast([6]) == 36
eventhelast([]) == 0
"""


def eventhelast(i):
    if not i:
        return 0
    r = 0
    for x in range(len(i)):
        if x % 2 == 0:
            r += i[x]
    return r * i[-1]


print eventhelast([6])
