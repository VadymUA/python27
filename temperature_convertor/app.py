# temperature convertor

import math

def f2c(Tf):
    return (5.0 / 9) * (int(Tf) - 32)


def c2f(Tc):
    return (9.0 / 5) * int(Tc) + 32


print "Temperature converter\n"
value = raw_input("Enter a temperature: ")
mode = raw_input("Convert to (F)ahrenheit or (C)elsius? ")
if mode == "f" or mode == "F":
    print "{} C = {:3.0f} F".format(value, c2f(value))
elif mode == "c" or mode == "C":
    print "{} F = {:3.0f} C".format(value, f2c(value))
else:
    print("Wrong answer!")
    exit(1)
