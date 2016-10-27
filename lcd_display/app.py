class Matrix():
    def __init__(self):
        self.dict = {1: ['000', '001', '000', '001', '000'],
                     2: ['020', '001', '020', '100', '020'],
                     3: ['020', '001', '020', '001', '020'],
                     4: ['000', '101', '020', '001', '000'],
                     5: ['020', '100', '020', '001', '020'],
                     6: ['020', '100', '020', '101', '020'],
                     7: ['020', '001', '000', '001', '000'],
                     8: ['020', '101', '020', '101', '020'],
                     9: ['020', '101', '020', '001', '020'],
                     0: ['020', '101', '000', '101', '020']}


    def read_config(self):
        """Returns a list of all params from config file"""
        return [line.rstrip('\n') for line in open('app.conf')]

    def print_lines(self, lines):
        for _l in lines:
            _w = _l.split()

            if _w[0] is not '0':
                for _line in range(3 + int(_w[0])):
                    for number in _w[1]:
                        self.print_line(_line)
                    print "\r"
            else:
                break

    def print_line(self, key):
        for _point in self.dict[key]:
            return self.decode_value(_point)

    def decode_value(self, point):
        for _g in self.dict[int(point)]:
            if _g == '0':
                print_digit(" ")
            elif _g == '1':
                print_digit("|")
            elif _g == '2':
                print_digit("-")

    def print_digit(self, symbol):
        print(symbol),


def main():
    # 2 12345
    # 3 67890
    # 0 0
    # print_single_digit(8)
    # print_multiple_digits(1234567890, 2)
    # print_line(22)
    """
    " " - 0
    "|" - 1
    "-" - 2
    """
    matrix = Matrix()
    lines = matrix.read_config()
    matrix.print_lines(lines)

if __name__ == '__main__':
    main()
