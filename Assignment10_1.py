from sys import *
import os

def fun(dirName, fileExtension):
    flag = os.path.isabs(dirName)
    if flag == False:
        dirName = os.path.abspath(dirName);

    exists = os.path.isdir(dirName)

    if exists:
        cnt = 0
        for FolderName, SubFolderName, FileName in os.walk(dirName):
            # print("Current Directory:",FolderName)
            for fileN in FileName:
                ext = os.path.splitext(fileN)[1]
                if (fileExtension == ext):
                    print("File name is", fileN)
                    cnt = cnt + 1

        if (cnt == 0):
            print("No file found with extension", fileExtension)


def main():
    print("----------------- Application Name -------------------", argv[0]);
    print(
        "----------------- accept directory name and file extension from user. Display all files with that extension.")
    print()

    if (len(argv) < 3):
        print("Invalid number of arguments")
    try:
        fun(argv[1], argv[2]);
    except Exception as e:
        print("Exception occred ", e)


if __name__ == "__main__":
    main();

