age=int(input("Enter your age"))
try:
    if(age>=18):
        print("you can vote")
    else:
        raise Exception("Greater than 18")
except Exception as ex:
    print(ex)
    print("Greater than 18")
