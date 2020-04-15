# iTunesの重複ファイルを検索して同じものがある場合は、ゴミ箱へ
from send2trash import send2trash
import os.path
import sys

def erase_file(f_path):
    if os.path.isdir(f_path):
        filelist = os.listdir(f_path)
        for file in os.listdir(f_path):
            basename = os.path.basename(file)
            #print(basename)
            filename, ext = os.path.splitext(basename)
            #print(filename)
            if filename.endswith(' 1') or filename.endswith(' 2') or filename.endswith(' 3'):
                checkfile = filename[:len(filename) - 2]
                if (checkfile + ext in filelist):
                    erasefilename = os.path.join(f_path, basename)
                    print(erasefilename)
                    send2trash(erasefilename)

def dirExistCheck(dir):
    if os.path.isdir(dir):
        for subdir in os.listdir(dir):
            if os.path.isdir(os.path.join(dir, subdir)):
                return True
    return False


def checkDir(dir):
     for subdir in os.listdir(dir):
        fullpath = os.path.join(dir, subdir)
        if dirExistCheck(fullpath):
           checkDir(fullpath)
        else:
            erase_file(fullpath)


# main
root_path = 'C:\\Users\\tsakata\\Music\\iTunes\\iTunes Media\\Music'

for dir in os.listdir(root_path):
    fullpath = os.path.join(root_path, dir)
    if dirExistCheck(fullpath):
        checkDir(fullpath)
    else:
        erase_file(fullpath)

sys.exit(0)
