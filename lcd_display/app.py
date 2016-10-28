class Item():
    def __init__(self):
        self.item = {}
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

    def create(self, line):  # tuple as input i.e. ('2', '12345')
        """Create the target array for further printing"""
        (_s, _numbers) = get_params(line)
        for key in _numbers:
            print self.dict[int(key)]

def read_config():
    """Returns a list of all params from config file"""
    return [line.rstrip('\n') for line in open('app.conf')]


def get_params(line):
    """Returns weight and numbers as separate strings in tuple"""
    return line.split()


def main():
    """
    " " - 0
    "|" - 1
    "-" - 2
    """

    config = read_config()
    for line in config:
        (s, numbers) = get_params(line)
        if s is not '0':
            item = Item()
            item.create(line)  # fill out just created object
    #        item.type(line)  # print it


if __name__ == '__main__':
    main()
