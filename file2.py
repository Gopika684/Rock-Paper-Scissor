def listsum(x1):
    sum=0
    fp=open("file1.txt","w")
    for x in x1:
        sum=sum+x
    fp.write(str(sum))
l1=[10,20,30,40,50]
listsum(l1)