num=int(input("Enter any number"))
a=0
b=1
print(a)
print(b)
for x in range(1,num+1):
    c=a+b
    print(c)
    a=b
    b=c
