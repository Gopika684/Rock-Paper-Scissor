num=int(input("Enter the number"))
n1=num
rev=0
while(num>0):
    r=num%10
    rev=rev*10+r
    num=num//10
print("Rev=",rev)
if(n1==rev):
    print("Palindrome")
else:
    print("not palindrome")
