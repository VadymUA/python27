input = [1, 2, 3]

for _i in range(1,len(input)):
    if sum(input[:_i]) == sum(input[_i:]):
        print (input[:_i], input[_i:])

