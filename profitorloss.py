cp=int(input("Enter the cost price"))
sp=int(input("Enter the selling price"))
if(sp>cp):
    pro=sp-cp
    print("Profit",pro)
else:
    if(cp>sp):
        loss=cp-sp
        print("Loss",loss)
    else:
        print("No profit No Loss")
