run=True

bag=[]

print("For options input [O]")
while run==True:
    choice=input("What's the plan big man ")
    if choice.lower()== "v":
        for i in bag:
            print(i)
    elif choice.lower()=="o":
        print("View inventory [V]")
        print("Display number of contents [N]")
        print("Save information [S]")
        print("Disregard information in specific spot[R]")
        print("Disregard specific information [E]")
        print("Quit the program [Q]")
        print()
    elif choice.lower()=="s":
        bag.append(input("Type in what you want to save "))
        print("Successfully saved the item.")
    elif choice.lower()=="n":
        print("The bag contains ",len(bag)," items.")
    elif choice.lower()=="r":
        while True:
            try:
                sure=input("Are you sure you want to remove an item? [y/n]")
                if sure=="y":
                    bag.pop(int(input("Input the index of the item you wish to remove (0,1,2...) ")))
                    print("Successfully removed the item.")
                    break
                else:
                    break
            except:
                print("Invalid input")
    elif choice.lower()=="e":
        while True:
            try:
                sure=input("Are you sure you want to remove an item? [y/n]")
                if sure=="y":
                    bag.remove(input("Input the information you wish to remove. Note that this is character and case-sensitive "))#This only removes the first instance of the target
                    print("Successfully removed the item.")
                    break
                else:
                    break
            except:
                print("Invalid input")
    elif choice.lower() == "q":
        run=False
    else:
        print("Nonsense gibberish, try again")