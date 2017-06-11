def file_read(python):  
        with open (python, "r") as file:  
                data=file.readlines()  
                print(data)  
file_read('file3.txt')
