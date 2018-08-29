#Que1-->Write a Pyhton program to read n lines of a file.
f=open("que1.txt",'r')
"""open is used to open the file in r mode i.e. read mode"""
data=f.read()
"""read reads the content of file"""
print(data)
f.close()
"""close closes the file"""
print()

#Que2-->Write a pyhton program to count the frequency of words in a file.
f=open("que2.txt",'r')
data=f.read()
words=data.split()
dict={}
for word in words:
    dict[word]=words.count(word)
print(dict)
f.close()
print()

#Que3-->Write a python program to copy the contents of a file to another file
f=open("que1.txt",'r')
line=f.readlines()    
for l in line:
    f1=open("que3.txt",'a')
    f1.write(l)
    f1.close()
f.close()
print()

#Que4-->Write a python program to combine each line from first file with the corresponding line in second file.
f=open("que1.txt",'r')
f1=open("que3.txt",'r')
for l1,l2 in zip(f,f1):
    f2=open("que4.txt",'a')
    f2.write(l1+l2)
    f2.close()
f.close()
f1.close()
print()

#Que5-->Read a file and sort it to another file.
import random
f=open("que5.txt",'w+')
for i in range(10):
    f.write(str(random.randint(0,9)))
    f.write('\n')
f.close()
f=open("que5.txt",'r')
f1=open("que5_1.txt",'w+')
l=[]
for line in f:
    l.append(int(line.strip("\n")))
l=sorted(l)
for i in l:
    print(i)
    f1.write('%s\n' %i)
f1.close()
f.close()

