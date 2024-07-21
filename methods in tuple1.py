t1=(10,20,30,40,50,[1,2,3],(11,22,33))
for x in t1:
    if(type(x)==list or type(x)==tuple):
        for y in x:
            print(y,end=' ')
    else:
        print(x,end=' ')