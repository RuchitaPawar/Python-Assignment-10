from sys import *
import os
from shutil import *


def fun(dirName1, dirName2, fileExt):
    accessright = 0o777
    flag = os.path.isabs(dirName1)

    if flag == False:
        dirName1 = os.path.abspath(dirName1);

    # check whether source directory exists or not
    exists = os.path.isdir(dirName1)

    if exists:
        existsDir2 = os.path.isdir(dirName2)
        list = os.listdir(dirName1)
        fpath = os.path.abspath(dirName1);

        if (existsDir2):
            print("Destinaton Deirctory already exist")
            for i in list:
                dir = os.path.isdir(i)
                file = os.path.isfile(i)
                s = os.path.join(dirName1, i)
                d = os.path.join(dirName2, i)
                if (dir):
                    try:
                        ext = os.path.splitext(i)[1]
                        if (fileExt == ext):
                         copytree(s, d)
                    except Error as exc:
                     print("Got exception {} while copying {} to {}".format(exc, dirName1, dirName2))
                else:
                     ext = os.path.splitext(i)[1]
                     if (fileExt == ext):
                       copy2(s, d)


        else:
                 os.mkdir(dirName2, accessright)
                 for i in list:
                    dir = os.path.isdir(i)
                    file = os.path.isfile(i)
                    s = os.path.join(dirName1, i)
                    d = os.path.join(dirName2, i)
                    ext = os.path.splitext(i)[1]
                    if (dir):
                        if (fileExt == ext):
                          copytree(s, d)
                    else:
                        if (fileExt == ext):
                          copy2(s, d)

    else:
        print("Sorce directory not exists.")


def main():
    print("----------------- Application Name -------------------", argv[0]);
    print(
        "accept two directory names and one file extension. Copy all files with the specified extension from first directory into second directory")
    print()

    if (len(argv) < 4):
        print("Invalid number of argumrnts")

    try:
        fun(argv[1], argv[2], argv[3]);
    except Exception as e:
        print("Exception occred :", e)


if __name__ == "__main__":
    main();
