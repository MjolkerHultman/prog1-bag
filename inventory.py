run=True

bag=[]

print("Heyo")
print("View inventory [V]")
print("Save information [S]")
print("Quit the program [Q]")
print()

while run==True:
    choice=input("What's the plan big man ")
    if choice.lower()== "v":
        for thing in bag:
            print(thing)
    elif choice.lower() == "q":
        run=False
    elif choice.lower()=="s":
        bag.append(input("Type in what you want to save "))
    else:
        print("Nonsense gibberish, try again")