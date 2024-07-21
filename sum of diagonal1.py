l1=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
print("Normal matrix")
for x in range(len(l1)):
    for y in range(len(l1[x])):
        print(l1[x][y],end=' ')
        if(x+y==2):
            sum=sum+l1[x][y]
    print()
print(sum)
