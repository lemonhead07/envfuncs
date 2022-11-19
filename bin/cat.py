import os
import sys


def main():
    args = sys.argv[1:]
    flags = ""
    flagletters = "AbeEnstTuv"
    longflags = ["--show-all", "--number-nonblank", "--show-ends", "--number",
                 "--squeeze-blank", "--show-tabs", "--show-nonprinting", "--help", "--version"]
    valid_flags = [f"-{c}" for c in flagletters] + longflags

    for arg in args:
        if arg[0] == "-" and len(arg) != 1:
            flags += arg[1:]

    if len(flags) == 0:
        if ">" in args:
            pos = args.index(">")
            files = []
            for arg in range(pos):
                files.append(arg)
            with open(args[-1], "x") as f:
                for i in files:
                    with open(i) as fsub:
                        test1 = fsub.read()
                        print(test1)
                        f.write(test1)
        # TODO: check if file exists, if it doesnt, check if '-' was inputted check  if it wasnt show an error


if __name__ == "__main__":
    main()
