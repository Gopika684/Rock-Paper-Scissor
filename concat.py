l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l3=['none']*len(l1+l2)
print(l3)
for i in range(len(l1+l2)):
    if(i<5):
        l3[i]=l1[i]
    else:
        l3[i]=l2[i-5]
print(l3)
