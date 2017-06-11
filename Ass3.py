def file_read(python):  
        from itertools import islice  
        with open(python, "w") as file:  
                file.write("Python Exercises\n")  
                file.write("Java Exercises")  
        txt = open(python)  
        print(txt.read())  
file_read('File.txt')
