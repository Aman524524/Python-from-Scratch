#A dictionary stores data in key-value pairs.
man = {
    "name": "Aman",
    "age": 22,
    "course": "Python"
}

print(man)
print(man["name"]) #Accessing the value of key "name" which is "Aman"

man["city"] = "Mumbai"
print(man) # Prints the updated dictionary with the new key-value pair

man["age"] = 23
print(man)  # Updates the value of key "age" to 23

man.pop("course") # Removes the key "course" and its value from the dictionary
print(man) # Prints the updated dictionary without the "course" key   

print(man.items()) # Returns a view object that displays a list of a dictionary's key-value tuple pairs

man.update({
    "age": 21,
    "city": "Delhi"
}) #Upadates multiple values in the dictionary at once. Here, it updates "age" to 21 and "city" to "Delhi"

print(man) 

# A nested dictionary is a dictionary where the values are themselves dictionaries. 
# It's useful for storing related information, such as records for multiple students.
student = {
    "student1": {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
},
    "student2": {
    "name": "Aman",
    "age": 22,
    "course": "Java"
    } 
}

for key, value in student.items():
    print(key, value) #prints the key and value of each student in the dictionary
# print(student["student1"]) #prints data of student1 which is inside student

   