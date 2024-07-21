x=input("Enter any character")
y=ord(x)
if(y>=65 and y<=90):
      print("Uppercase")
else:
    if(y>=97 and y<=122):
       print("Lowercase")
    else:
        if(y>=48 and y<=57):
            print("Numbers")
        else:
            print("Special Symbols")
