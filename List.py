#Assigned inside square brackets [].lists are ordered, changeable (mutable), and allow duplicate values.
name=["aman","rahul","sachin","rohit"]
mixed=[1,2.33,"aman",True]

length=len(name)
print(length)
#4
first=name[0] # Accessing by index
print(first)
#aman

firstSecond=name[0:2] ## Accessing by slicings
print(firstSecond)
#['aman', 'rahul']

lastAccess=name[-1] # Accessing by negative index
print(lastAccess)
#rohit

print(type(mixed[3])) # here it iwill show the type of data present in that list
#<class 'bool'>

removeLast=name.pop() # it will remove the last element from the list
print(name) #OPERATIONS ON LIST IS DONE LIKE IT IS UPDATED and go simultanesoustly
#['aman', 'rahul', 'sachin'] 

removeIndex=name.pop(1) # it will remove the element present at index 1
print(name)#['aman', 'sachin']
print(removeIndex) #rahul (shows the removed element/poped element)

insertIndex=name.insert(1,"rohit") # it will insert the element at index 1
print(name) #['aman', 'rohit', 'sachin'] # inserted the element at index 1 and updated the list