import os

tree = os.walk('/home/sarang/AMZSYS/Learn Python Basics/Modules/')
for paths , dirs , files in tree:
    print("Paths is : -- {}".format(paths))
    print("Directories is : -- {}".format(dirs))
    print("Files is : -- {}".format(files))
    print()