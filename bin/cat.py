import os
import sys


# TODO: how do i handle flags in the terminal
def main():
    args = sys.argv[1:]
    flagletters = "AbeEnstTuv"
    longflags = ["--show-all", "--number-nonblank", "--show-ends", "--number",
                 "--squeeze-blank", "--show-tabs", "--show-nonprinting", "--help", "--version"]
    flags = [f"-{c}" for c in flagletters] + longflags

    print(args)

    print(flags)


if __name__ == "__main__":
    main()
