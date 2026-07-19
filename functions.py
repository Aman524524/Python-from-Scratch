#no arguments but return value
def greet():
    return "Hello, welcome to our program!"

greet2 = greet()
print(greet2)

#no arguments no return value
def greet():
    print("hello")

greet()

#arguments but no return value
def greet(name):
    print("Hello,"+name)

greet("Automation Anywhere")

#arguemnts and return value
def greet(name):
    return "Hello,"+name
greet1 = greet("Automation Anywhere")
print(greet1)


