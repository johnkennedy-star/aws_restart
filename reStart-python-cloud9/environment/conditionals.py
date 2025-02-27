

userReply=input("Do you need to ship a package? (Enter yes or no) ")

if userReply=="yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
    
    

userReply=input("Would you like to buy stamps, buy an envelop, or make a copy? (Enter stamps, envelop, or copy) ")
if userReply=="stamps":
    print("We have many stamp designs to choose from.")
elif userReply=="envelops":
    print("We have many envelop sizes to choose from.")
elif userReply=="copy":
    copies=input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies." .format(copies))
else:
    print("Thank you, please come again.")
