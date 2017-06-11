def file_read(python):  
        content_array = []  
        with open(python) as file:  
                #Content_list is the list that contains the read lines.       
                for line in file:  
                        content_array.append(line)  
                print(content_array)  
file_read('file3.txt') 
