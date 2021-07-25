
file1 = open('users.txt','w')
file1.write("Hello!")
file1.close()
file1 = open('users.txt','r')
print(file1.readlines())
file1.close()
