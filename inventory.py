run=True

bag=[]

print("For options input [O]")
while run==True:
    print("Heyo")
    choice=input("What's the plan big man ")
    if choice.lower()== "v":
        for i in bag:
            print(i)
    elif choice.lower()=="o":
        print("View inventory [V]")
        print("Save information [S]")
        print("Disregard information in specific spot[R]")
        print("Disregard specific information [SR]")
        print("Quit the program [Q]")
        print()
    elif choice.lower()=="s":
        bag.append(input("Type in what you want to save "))
    elif choice.lower()=="r":
        while True:
            try:
                sure=input("Are you sure you want to remove an item? [y/n]")
                if sure=="y":
                    bag.pop(int(input("Input the index of the item you wish to remove ")))
                    break
                else:
                    break
            except:
                print("Invalid input")
    elif choice.lower()=="sr":
        while True:
            try:
                sure=input("Are you sure you want to remove an item? [y/n]")
                if sure=="y":
                    bag.remove(input("Input the information you wish to remove. Note that this is character and case-sensitive "))
                    break
                else:
                    break
            except:
                print("Invalid input")
    elif choice.lower() == "q":
        run=False
    else:
        print("Nonsense gibberish, try again")