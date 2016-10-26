def print_multiple_digits(numbers, weight):  # 2 ints on input
    _numbers = map(int, str(numbers))
    for _line in range(0, 5):
        for number in _numbers:  # make it as a list [1,2,3,4,5]
            _number = number * 10 + _line
            print_line(_number)
        print "\r"


def print_line(key):  # 10 -> 0 -> 0000
    for _point in lcd[key]:
        return decode_value(_point)


def decode_value(point):  # 0 -> 0000
    for _g in dictionary[int(point)]:
        if _g == '0':
            print " ",
        elif _g == '1':
            print "|",
        elif _g == '2':
            print "-",


def print_single_digit(number):
    for _line in range(0, 5):
        _number = number * 10 + _line
        print_line(_number)
        print "\r"


"""
{number:[points]}
_start_number + _delta -> _number
" " - 0
"|" - 1
"-" - 2
"""
dictionary = {0: '0000', 1: '0001', 2: '1000', 3: '1001', 4: '0220'}

lcd = {10: '0', 11: '1', 12: '0', 13: '1', 14: '0',
       20: '4', 21: '1', 22: '4', 23: '2', 24: '4',
       30: '4', 31: '1', 32: '4', 33: '1', 34: '4',
       40: '0', 41: '3', 42: '4', 43: '1', 44: '0',
       50: '4', 51: '2', 52: '4', 53: '1', 54: '4',
       60: '4', 61: '2', 62: '4', 63: '3', 64: '4',
       70: '4', 71: '1', 72: '0', 73: '1', 74: '0',
       80: '4', 81: '3', 82: '4', 83: '3', 84: '4',
       90: '4', 91: '3', 92: '4', 93: '1', 94: '4',
       00: '4', 01: '3', 02: '0', 03: '3', 04: '4'
       }


with open("test_LCD_display.conf") as f:
    for line in f:
        data = f.readlines()
        print data

# 2 12345
# 3 67890
# 0 0
# print_single_digit(8)
# print_multiple_digits(1234567890, 2)
# print_line(22)
