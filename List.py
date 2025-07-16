a = input("Enter a list of numbers")
userlist = list(a)
#print(userlist)

userlist = userlist[::-1]
print userlist

b = input("Enter another list")

inputlist = list(b)
inputlist = inputlist[::-1]
print inputlist


numberlist = inputlist + userlist 
numberlist.sort()

print(numberlist)
elements = len(numberlist)
print("There are total " + str(elements) + " elements in list")






