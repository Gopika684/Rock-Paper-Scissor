t1=()
print(type(t1))
t1=list(t1)
print(type(t1))
size=int(input("Enter the size:"))
for x in range(size):
    data=int(input("Enter data"))
    t1.append(data)
print(t1)
t1=tuple(t1)
print(type(t1))
print(t1)