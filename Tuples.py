#Ordered, but immutable (cannot be changed after creation).
#Tuples are generally a little faster than lists because they cannot be modified
#If your data should remain constant, use a tuple.

colors = ("red", "green", "blue")
colors2 = ("yellow", "orange")
colors3 = colors + colors2 # concatenation of tuples #colors3 is also a tuple
print(colors3) #('red', 'green', 'blue', 'yellow', 'orange')
print(type(colors3)) #<class 'tuple'>
