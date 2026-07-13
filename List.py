name=["aman","rahul","sachin","rohit"]
mixed=[1,2.33,"aman",True]
length=len(name)
print(length)
first=name[0] # Accessing by index
print(first)

firstSecond=name[0:2] ## Accessing by slicings
print(firstSecond)

print(type(mixed[3])) # here it iwill show the type of data present in that list

removeLast=name.pop() # it will remove the last element from the list
print(name)