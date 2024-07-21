l1=[]
row=int(input("enter the row:"))
col=int(input("enter the col:"))
for i in range(row):
    a=[]
    for j in range(col):
        data=int(input("Enter data:"))
        a.append(data)
    l1.append(a)
print(l1)
