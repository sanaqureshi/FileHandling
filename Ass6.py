# 6. Write a Python program to read a file line by line store it into a variable. 

def file_read(python):  
        with open (python, "r") as file:  
                data=file.readlines()  
                print(data)  
file_read('file3.txt')

'''OUTPUT :
[root@python FileHandling]# python Ass6.py
['Apple\n', 'Mango\n', 'Guava\n', 'Raspberry\n', 'Peach\n', 'Orange\n']'''












