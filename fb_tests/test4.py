"""
n: number of win
m: total qty
"""
import random


def lotto(n, m):
    t = []

    while len(t) < n:
        r = random.randint(1, m)
        if r not in t:
            t.append(r)

    t.sort()
    print t


lotto(5, 12)
lotto(6, 14)
lotto(7, 20)
