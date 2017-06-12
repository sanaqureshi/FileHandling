#2. Write a Python program to read first n lines of a file and print these lines.

file=open("file1.txt", "w+")
file.write("BByeee..!!!")
file.seek(0,0)
print(file.readlines())
file.close()

'''OUTPUT :
[root@python FileHandling]# python Ass2.py
['BByeee..!!!']
'''
