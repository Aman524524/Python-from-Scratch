#A set is an unordered collection of unique elements. Assigned inside curly brackets {}.
# Why Use Sets?
# Suppose you have duplicate values:
# Duplicates are automatically removed.
fruits = {"apple", "banana", "mango", "grapes", "banana", "apple"}
print(fruits) # {'banana', 'grapes', 'mango', 'apple'}

removed = fruits.pop() #Since sets are unordered, pop() removes an arbitrary element, not necessarily the "first" one as it would in a list.
print(removed)
print(fruits)

# copy()	Create a copy of the set
# union()	Combine two sets
# intersection()	Common elements
# difference()	Elements in one set but not the other
# symmetric_difference()	Elements in either set, but not both
a={1, 2, 3, 4, 5}
b={4, 1, 3, 7, 5}
c=(a|b) # union of two sets
d=(a&b) # intersection of two sets
e=(a-b) # difference of two sets
f=(a^b) # symmetric difference of two sets
g=a.copy() # copy of set a
print(c) 
print(d) 
print(e) 
print(f) 
print(g) 