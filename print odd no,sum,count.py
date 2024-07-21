l1=[]
size=int(input("Enter the size"))
for x in range(size):
    data=int(input("Enter the data"))
    l1.append(data)
print(l1)
sum=0
count=0
for x in l1:
    if(x%2!=0):
        print("odd=",x)
        sum=sum+x
        count+=1
print("Sum=",sum)
print("odd count=",count)
