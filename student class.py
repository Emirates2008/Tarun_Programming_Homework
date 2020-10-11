filename = ["student1.txt","student2.txt","student3.txt","student4.txt","student5.txt"]
b=[]
for files in filename:
    f=open(files,'r')
    contents=f.read()
    contents=contents.split('\n')
    b.append(contents[-1])
    f.close()
count1=0
for element in b:
    count1=count1+1
    if b.count(element)>1:
        print(element)
        print(filename[count1-1])
    
