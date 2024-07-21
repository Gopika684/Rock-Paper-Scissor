def msg():
    print("message called")
def add():
    a=int(input("Enter A"))
    b=int(input("Enter B"))
    c=a+b
    print("sum=",c)
def sub(a,b):
    c=a-b
    return c
def listsum(l1):
    sum=0
    for x in l1:
        sum=sum+x
    print("list sum=",sum)

