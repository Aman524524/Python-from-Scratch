#Ordered, but immutable (cannot be changed after creation).Assigned inside parentheses ().
#Tuples are generally a little faster than lists because they cannot be modified
#If your data should remain constant, use a tuple.

colors = ("red", "green", "blue")
colors2 = ("yellow", "orange")

colors3 = colors + colors2 # concatenation of tuples #colors3 is also a tuple

print(colors3) #('red', 'green', 'blue', 'yellow', 'orange')

print(type(colors3)) #<class 'tuple'>

slice=colors3[1:4] #slicing of tuples
print(slice) #('green', 'blue', 'yellow')

slice1=colors3[-3:-1] # -3 is the index of 'blue' and -1 is the index of 'orange' 
#but it will not include the last index
print(slice1) #('blue', 'yellow')

slice2=colors3[0:5:2] # slicing with step #takes 1st index then 3rd index then 5th index and so on
print(slice2) #('red', 'blue', 'orange')

