while True:
    try:
        x = int(input("Input birth day: "))
    except (NameError, SyntaxError, TypeError) as err:
        print("{0}! Try again...".format(err))
    else:
        print("You are {} years old.".format(2016 - x))
        break
    finally:
        print("That's it!")
