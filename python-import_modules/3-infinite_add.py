#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argv = sys.argv
length = len(argv)
res = 0

if (length == 1):
    print("{}".format(res))

for i in range(1, length):
        if (int(argv[i])):
            res += int(argv[i])

print("{}".format(res))

