#1 method:
file1=open('first.txt','r')
for a in file1:
    print(a)
file1.close()

#2 method:
file1=open('first.txt','r')
print(file1.read())
file1.close()

#3 method:

with open("first.txt") as file:
    data=file.read()
print(data)
file.close()

#read certain no of char
file=open("first.txt",'r')
print(file.read(4))
print(file.readline()) 
print(file.readline(3))#read no of files
file.seek(3) #move read write position
print(file.read())
file1.close()

#use of read
file=open("first.txt",'r')
data=file.readline()
for line in data:
    word=line.split()
    print(word)
