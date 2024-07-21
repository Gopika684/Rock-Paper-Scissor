d1={'id':[101,[11,22,33],103],'name':'amit','age':23}
for i,j in d1.items():
    if(type(j)==list):
        for x in j:
            if(type(x)==list):
                for y in x:
                   print(i,"===",y)
            else:
                   print(i,">>>",x)
    else:
        print(i,">>>",j)