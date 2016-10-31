class Lcd():
    def __init__(self):
        self.item = {}
        self.map = {1: ['000', '001', '000', '001', '000'],
                    2: ['020', '001', '020', '100', '020'],
                    3: ['020', '001', '020', '001', '020'],
                    4: ['000', '101', '020', '001', '000'],
                    5: ['020', '100', '020', '001', '020'],
                    6: ['020', '100', '020', '101', '020'],
                    7: ['020', '001', '000', '001', '000'],
                    8: ['020', '101', '020', '101', '020'],
                    9: ['020', '101', '020', '001', '020'],
                    0: ['020', '101', '000', '101', '020']}

    def create(self):  # tuple as input i.e. ('2', '12345')
        """Create the target array for further printing"""
        for key in numbers:
            self.item[int(key)] = [self.insert_str(one, s) for one in self.insert_list(self.map[int(key)])]
        # print self.item  # for debug only

    def print_it(self):
        """Return printed image from mapped values, i.e. '0220' -> ' -- '
        Print map is:
            " " - 0
            "|" - 1
            "-" - 2
        """
        for _column in range(2 * int(s) + 3):
            for _raw in self.item.keys():
                print (self.transcode(self.item[_raw][_column])),
            print "\r"

    def transcode(self, word):
        """Return a word in the ready-to-print format"""
        word = word.replace("0", " ")
        word = word.replace("1", "|")
        word = word.replace("2", "-")
        return word

    def insert_str(self, source_str, s):
        """Return a string with inserted a multiplied element [1] by s, i.g.'020' -> '02220'"""
        _delta = ''.join([source_str[1] for _x in range(1, int(s))])
        return source_str[:1] + _delta + source_str[1:]

    def insert_list(self, list):
        """Return a list with inserted multiplied elements by s. Begins to add elements to the list from end!"""
        for _x in range(1, int(s)):
            list.insert(3, list[3])
        for _x in range(1, int(s)):
            list.insert(1, list[1])
        return list


class Config():
    def __init__(self):
        return None

    def read(self):
        return [line.rstrip('\n') for line in open('app.conf')]


def main():
    c = Config()
    config = c.read()
    global s, numbers
    for line in config:  # process each line from config
        (s, numbers) = line.split()  # get 2 separate parameters, they're global, both
        if s is not '0':
            item = Lcd()
            item.create()  # fill out just created object
            item.print_it()  # print it


if __name__ == '__main__':
    main()
