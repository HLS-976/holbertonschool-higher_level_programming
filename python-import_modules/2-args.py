#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argv = sys.argv
length = len(argv)

if (length == 1):
    print("{} arguments.".format(length - 1))
elif (length == 2):
    print("{} argument:".format(length - 1))
    print("{}: {}".format(length - 1, argv[length - 1]))
else:
    print("{} arguments:".format(length - 1))
    for i in range(1, length):
        print("{}: {}".format(i, argv[i]))
