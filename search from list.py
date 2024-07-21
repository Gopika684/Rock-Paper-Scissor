l1=[]
size=int(input("Enter any size:"))
for x in range(size):
    data=int(input("Enter the data:"))
    l1.append(data)
print(l1)
count=0
key=int(input("search number:"))
for x in l1:
    if(x==key):
        count+=1
if(count==0):
    print("not found")
else:
    print("found")
