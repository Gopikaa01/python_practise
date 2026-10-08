import random
choices=["stone","paper","scissor"]
user=input("enter ur choice:")
computer=random.choice(choices)

print("your choice :",user)
print("computer choice:",computer)

if user==computer:
    print("play again")
elif user=="stone" and computer=="scissor":
    print("user win")
elif user=="paper" and computer=="stone":
    print("user win")
elif user=="scissor" and computer=="paper":
    print("user win")
else:
    print("computer win")