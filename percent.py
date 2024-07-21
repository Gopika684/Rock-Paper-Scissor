m1=int(input("Enter first marks"))
m2=int(input("Enter second marks"))
m3=int(input("Enter third marks"))
m4=int(input("Enter fourth marks"))
m5=int(input("Enter fifth marks"))
per=(m1+m2+m3+m4+m5)//5
print("per=",per,"%")
if(per>=60):
    print("first division")
else:
    if(per>=45 and per<60):
        print("second division")
    else:
        if(per>=33 and per<45):
            print("third division")
        else:
            print("Fail")
