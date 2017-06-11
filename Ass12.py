from shutil import copyfile
import os
os.system("touch file3.txt ")
copyfile('file1.txt', 'file3.txt')
