#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 1:
        print("0 arguments.")
    else:
        print("{} arguments".format((len(sys.argv) - 1)))
    for i in range(1, len(sys.argv)):
        if len(sys.argv[i]) == 1:
            print("1 argument:")
            print("{}: {}".format(i, sys.argv[i]))
        else:
            print("{}: {}".format(i, sys.argv[i]))
