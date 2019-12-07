from sys import *
import os


def fun(dirName, fileExtension1, fileExtension2):
    flag = os.path.isabs(dirName)

    if flag == False:
        dirName = os.path.abspath(dirName);

    exists = os.path.isdir(dirName)

    if exists:
        for FolderName, SubFolderName, FileName in os.walk(dirName):
            # print("Current Directory:",FolderName)

            for fileN in FileName:
                ext1 = os.path.splitext(fileN)[1]

                pre, ext = os.path.splitext(fileN)
                if (ext1 == fileExtension1):
                    #   os.rename(fileN, pre + fileExtension2)

                    infilename = os.path.join(dirName, fileN)
                    if not os.path.isfile(infilename): continue
                    oldbase = os.path.splitext(fileN)
                    newname = infilename.replace(ext1, fileExtension2)
                    output = os.rename(infilename, newname)


def main():
    print("----------------- Application Name -------------------", argv[0]);
    print(
        "accept directory name and two file extensions from user. Rename all files with first file extension with the second file extenntion.")
    print()

    if (len(argv) < 3):
        print("Invalid number of argumrnts")

    try:
        fun(argv[1], argv[2], argv[3]);
    except Exception as e:
        print("Exception occred ", e)


if __name__ == "__main__":
    main();
