d1={'id':201,'name':'govind','age':17}
print(d1)
d1['id']=101
d1['name']='Gopika'
d1['age']=20
print(d1)
for x in d1.keys():
    print(x)
for x in d1.values():
    print(x)
for key,value in d1.items():
    print(key,">>>",value)

