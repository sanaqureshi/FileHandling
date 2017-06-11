MyFruits = ['Apple', 'Mango', 'Guava', 'Raspberry', 'Peach', 'Orange']   
with open('file1.txt', "w") as file:   
  for f in MyFruits:   
    file.write("%s\n" % f)       
content = open('file1.txt')   
print(content.read())   

