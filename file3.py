def listsum(x1):
    max=0
    fp=open("file1.txt","w")
    for x in x1:
        if x>max:
            max=x
    fp.write(str(max))
    fp.close()
    fp=open("file1.txt","r")
    data=fp.read()
    print(data)
l1=[10,20,30,1000,50]
listsum(l1)