import os
import sys
files = os.listdir()
args = sys.argv[1] if len(sys.argv) > 1 else ""
os.system("color")

if "-" in args:
    endline = "\n" if "l" in args else ""
    for i in files:
        if "a" not in args:
            if i[0] == ".": continue
        if os.path.isdir(os.path.abspath(i)):
            print(f"\033[34m{i}\033[0m ", end=endline)
        else:
            print(i, end=endline)
    exit()




for i in files:
    if i[0] == ".": continue
    if os.path.isdir(os.path.abspath(i)):
        print(f"\033[34m{i}\033[0m ", end="")
    else:
        print(i, end=" ")

    
