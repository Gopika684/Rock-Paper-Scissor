l1=[[1,2,3],[4,5,6],[7,8,9]]
print("Normal matrix")
for x in range(len(l1)):#3
    for y in range(len(l1[x])):#3
        print(l1[x][y],end=' ')
    print()
print("Transpose matrix")
for x in range(len(l1)):
    for y in range(len(l1[x])):
        if(x==y or x+y==2):
            print("0",end=' ')
        else:
            print(l1[x][y],end=' ')
    print()
