def file_read(python):
      with open(python) as file:             
                 content_list = file.readlines()
                 print(content_list)
file_read('file1.txt')
