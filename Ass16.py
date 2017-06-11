def remove_newlines(file3):  
    filelist = open(file3).readlines()  
    return [s.rstrip('\n') for s in filelist]    
print(remove_newlines("file3.txt")) 
