with open('file2.txt') as f2, open('file1.txt') as f1:  
	for l1, l2 in zip(f2, f1):  
        	print(l1+l2) 
