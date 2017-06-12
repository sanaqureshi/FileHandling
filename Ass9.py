# 9. Write a Python program to count the frequency of words in a file. 

file=open("file3.txt","r+")
wordcount={}
for w in file.read().split():
    if w not in wordcount:
        wordcount[w] = 1
    else:
        wordcount[w] += 1
for n in wordcount.items():
    print n
'''OUTPUT :
[root@python FileHandling]# python Ass9.py
('Guava', 1)('Apple', 1)('Peach', 1)('Mango', 1)('Orange', 1)('Raspberry', 1)
'''
