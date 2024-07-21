l1=[]
size=int(input("enter the size:"))
for x in range(size):
    data=int(input("enter data"))
    l1.append(data)
print(l1)
max=l1[0]
for x in l1:
    if(x>max):
        max=x
print("Max=",max)
