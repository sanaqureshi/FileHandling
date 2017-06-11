def file_size(python):  
        import os  
        statinfo = os.stat(python)  
        return statinfo.st_size  
print("File size in bytes of the File3 is : ", file_size("file3.txt"))  
