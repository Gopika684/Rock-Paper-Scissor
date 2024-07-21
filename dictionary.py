d1={'id':101,'name':'Gopika','age':20}
print(d1['name'])
print(d1['age'])
d1['id']=101
d1['name']="Govind"
d1['age']=17
print(d1)
d1['grade']='A'
d1['salary']=10000
print(d1)
print(d1['id'])
print(d1.get('id',"key Not Found"))
print(d1.keys())
print(d1.values())
print(d1.items())