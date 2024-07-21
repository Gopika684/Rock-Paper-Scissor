l1=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for x in range(len(l1)):#3
    for y in range(len(l1[x])):#3
        print(l1[x][y],end=' ')
        sum=sum+l1[x][y]
    print("Sum=",sum)
    sum=0
    print()
