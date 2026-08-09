# Recursion is when a function calls itself to solve a smaller version of the same problem.

# def factorial(n):
#     if (n==1):
#         return 1
#     else:
#         n=n*factorial(n-1)
#         return n

# print(factorial(5))


# def sumRecurion(n):
#     if n==0:
#      return 0
#     else:
#        return n+sumRecurion(n-1)

# print(sumRecurion(4))


def Elements(list,Index):
    if Index==len(list):
        return
    print(list[Index],end=" ")
    Elements(list,Index+1)

Elements([1,2,3,4,5,23,45],0)

