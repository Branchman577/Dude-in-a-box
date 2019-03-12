from dice import d
import os


def main():
    print("Hello, Do you want a random character or do you want to build one?")
    char = startchoice()
    if char == 1:
        print("Let's get started making your character!")
        os.system('clear')
        print("Now you have to choose a race")
    else:
        print("Here is your random character!")
        os.system('clear')
        print("Here is your character!")


def startchoice():
    print("1. Build Own.")
    print("2. Random.")
    try:
        ch = input()
        if ch == 1:
            return ch
        elif ch == 2:
            return ch
        else:
            print("You need to choose either 1 or 2.")
            startchoice()
    except(NameError):
        print("You need to write in a number.")
        startchoice()
    except(SyntaxError):
        print("You need to write in a number.")
        startchoice()




if __name__ == '__main__':
    main()
