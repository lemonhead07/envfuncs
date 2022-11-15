import os

files = os.listdir()
    
os.system("color")

for i in files:
    if os.path.isdir(os.path.abspath(i)):
        print(f"\033[34m{i}\033[0m ", end="")
    else:
        print(i, end=" ")

    
