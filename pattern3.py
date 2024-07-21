n=1
for i in range(1,6):
    for k in range(1,6-i):
        print(end=' ')
    for j in range(1,n+1):
        print(end='*')
    n=n+2
    print()
