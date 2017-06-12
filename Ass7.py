# 7. Write a Python program to read a file line by line store it into an array. 

def file_read(python):  
        content_array = []  
        with open(python) as file:         
                for line in file:  
                        content_array.append(line)  
                print(content_array)  
file_read('file3.txt') 

'''OUTPUT :
[root@python FileHandling]# python Ass7.py
['Apple\n', 'Mango\n', 'Guava\n', 'Raspberry\n', 'Peach\n', 'Orange\n']'''
