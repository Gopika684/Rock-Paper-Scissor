import random
item=["Rock","Paper","Scissor"]
user=input("Enter your move =Rock,Paper,Scissor =")
comp=random.choice(item)
print(f"User choice ={user} , Computer choice={comp}")
if user==comp:
    print("Both chooses same:=Match Tie")
elif user=="Rock":
    if comp=="Paper":
        print("Paper covers Rock =Computer wins")
    else:
        print("Rock samshes Scissor=You Win")
elif user=="Paper":
    if comp=='Scissor':
        print("Scissor cuts paper,Computer win")
    else:
        print("Paper covers Rock, You win")
elif user=="Scissor":
    if comp=="Paper":
        print("Scissor cuts Paper,You Win")
    else:
        print("Rock smashes Scissor,Computer wins")
