"""
Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two
elements of the triplet equals the third element using numbers below n.

Please note that (a, b, c) and (b, a, c) represent same triplet.

Output: triplets(5)
[(1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 2, 4)]
"""


def triplets(n):
    t = []
    for i in range(1, n):
        for e in range(1, n):
            s = i + e
            if s < n:
                if (e, i, s) not in t:
                    t.append((i, e, s))
    print(t)


triplets(5)
