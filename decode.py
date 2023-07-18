list = [12,32,14,98]
item = input("Enter the number: ")
for item in list:
    if item in list:
        print("yes")
        print ("Your number is in index", list.index(item) )
        break
    else:
        print("noo")