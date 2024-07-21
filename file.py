fp=open("file1.txt","w")
data="My name is gopika nair.I am a B-tech Engineering student"
fp.write(data)
print("Data saved")
fp=open("file1.txt","r")
data=fp.readline()
print(data)