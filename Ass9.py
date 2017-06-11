file=open("file3.txt","r+")
wordcount={}
for w in file.read().split():
    if w not in wordcount:
        wordcount[w] = 1
    else:
        wordcount[w] += 1
for n in wordcount.items():
    print n
