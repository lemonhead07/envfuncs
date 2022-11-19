import sys

args = sys.argv[1:]

for i in args:
    with open(i, "x") as f:
        pass
