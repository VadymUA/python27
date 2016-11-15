import random

t = []
while True:
    r = random.randint(1, 6)
    t.append(r)
    if r == 6:
        print t
        exit(0)
