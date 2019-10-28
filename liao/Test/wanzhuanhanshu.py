import sys


def Hours(minute):
    if minute < 0:
        raise ValueError("Input number can't be negative")
    else:
        print('{} H, {} M'.format(int(minute / 60), minute % 60))

try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")