import os

class Map():
    def __init__(self):
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


class Main():
    def __init__(self, s, numbers):
        self.target = {}  # a target array
        self.transmap = {'0': ' ', '1': '|', '2': '-'}  # a translation map
        self.s = int(s)  # size of symbol; 's' is int here!
        self.numbers = numbers  # string with input numbers for printing

    def create(self, map):
        """Create the target array for further printing"""
        for key in self.numbers:
            if int(key) not in self.target:  # trying to avoid replacing of already existing numbers to array
                self.target[int(key)] = [self.insert_str(one) for one in self.insert_list(map[int(key)])]
        return self.target

    def print_it(self, array):
        """Return printed image from mapped values, i.e. '0220' -> ' -- '"""
        for column in range(2 * self.s + 3):
            for key in self.numbers:
                print (self.transcode(array[int(key)][column])),
            print "\r"

    def transcode(self, word):
        """Return a word in the ready-to-print format"""
        for k, v in self.transmap.iteritems():
            word = word.replace(k, v)
        return word

    def insert_str(self, string):
        """Return a string with inserted a multiplied element [1] by s, i.g.'020' -> '02220'"""
        delta = ''.join([string[1] for _x in range(1, self.s)])
        return string[:1] + delta + string[1:]

    def insert_list(self, source_list):
        """Return a list with inserted multiplied elements by s. Begins to add elements to the list from end!"""
        dest_list = source_list[:]  # clone existing string for further manipulations
        for pos in [3, 1]:
            self.duplicate_str(pos, dest_list)
        return dest_list

    def duplicate_str(self, param, list):
        """Return the modified list with inserted duplicates, multiplied by s"""
        for counter in range(1, self.s):
            list.insert(param, list[param])
        return list


class Config():
    def __init__(self):
        self.config_name = 'app.conf'
        self.application_path = os.path.dirname(os.path.realpath(__file__)) + os.sep
        self.config_file = os.path.join(self.application_path, self.config_name)

    def read(self):
        """Return a list with parameters from config file"""
        return [line.rstrip('\n') for line in open(self.config_file)]


def app():
    c = Config()
    m = Map()
    try:
        config = c.read()
    except:
        raise IOError("Config file {} is absent".format(c.config_name))

    for line in config:  # take each line from config file
        (s, numbers) = line.split()  # get 2 separate parameters, they're global, both
        if s is not '0':  # proceed it until not equal '0'; 's' is string here!
            main = Main(s, numbers)
            array = main.create(m.map)  # fill out just created object
            main.print_it(array)  # print it

    """Check if m.map is an immutable object"""
    s = '4'
    numbers = '99999'
    main2 = Main(s, numbers)
    array2 = main2.create(m.map)
    main2.print_it(array2)


if __name__ == '__main__':
    app()
