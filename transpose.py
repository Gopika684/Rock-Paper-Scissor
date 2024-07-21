l1=[[1,2,3],[4,5,6],[7,8,9]]
print("Normal matrix")
for x in range(len(l1)):
    for y in range(len(l1[x])):
        print(l1[x][y],end=' ')
    print()
print("Transpose matrix")
for x in range(len(l1)):
    for y in range(len(l1[x])):
        print(l1[y][x],end=' ')
    print()
