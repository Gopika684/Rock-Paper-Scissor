d1=[{'id':101,'name':'Gopika','age':20},{'id':102,'name':'ajay','age':21},{'id':103,'name':'vijay','age':23}]
# for x in d1:
#     for i,j in x.items():
#         print(i,"><",j)
#     print()
for x in range(len(d1)):
    for i,j in d1[x].items():
        print(i,'===',j)
    print()