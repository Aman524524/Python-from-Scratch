# """ #no arguments but return value
# def greet():
#     return "Hello, welcome to our program!"

# greet2 = greet()
# print(greet2)

# #no arguments no return value
# def greet():
#     print("hello")

# greet()

# #arguments but no return value
# def greet(name):
#     print("Hello,"+name)

# greet("Automation Anywhere")

# #arguemnts and return value
# def greet(name):
#     return "Hello,"+name
# greet1 = greet("Automation Anywhere")

# print(greet1)



# #####################################################3
# def missingNumber(arr):
#     n = len(arr)
#     flag = False

#     # Check if 1 is present in array or not
#     for i in range(n):
#         if arr[i] == 1:
#             flag = True
#             break

#     # If 1 is not present
#     if not flag:
#         return 1

#     # Change out of range values to 1
#     for i in range(n):
#         if arr[i] <= 0 or arr[i] > n:
#             arr[i] = 1

#     # Mark the occurrence of numbers 
#     # directly within the same array
#     for i in range(n):
#         arr[(arr[i] - 1) % n] += n

#     # Finding which index has value less than n
#     for i in range(n):
#         if arr[i] <= n:
#             return i + 1

#     # If array has values from 1 to n
#     return n + 1

# if __name__ == "__main__":
#     arr = [2, -3, 4, 1, 1, 7]
#     print(missingNumber(arr))

#  """

# city=["london","new york","Delhi","tokyo"]
# Numbers=[1,2,3,4,43,21]
# def LenOf(a):
#     print(len(a))

# LenOf(city)
# LenOf(Numbers)
# 4
# 6

# Numbers=[2,3,4,43,21]

# def ListPrint(list):
#  for i in list:
#   print(i,end=" ")
  
# ListPrint(Numbers)

# def factorial(n):
#     for i in range(1,n):
#         n=i*n
#     print(n)

# factorial(5)
# 120

# def converter(usd):
#     inr=usd*98.47
#     print(inr)

# converter(2)
# 196.94


def OddEvenCheck():
    n=int(input("Enter a number: "))
    if n%2==0:
     print(f"{n} is even")
    else:
     print(f"{n} is odd")

OddEvenCheck()