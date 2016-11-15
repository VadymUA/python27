"""Given: sorted array of integers
Return: sorted array of squares of those integers
Ex: [1,3,5] -> [1,9,25]

Integers can be negative."""
import sys

array = [3,1,5, -5, -20]
a = [x**2 for x in array]
a.sort()
print a

