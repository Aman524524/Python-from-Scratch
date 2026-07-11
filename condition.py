age=int(input("Enter your age: ")) 
#Here it takes input from user and converts it into integer type
if age<18:
    print("You are a minor and not eligible to vote and cant do Government Job.")
elif age>=18 and age<60:
    print("You are eligible to vote and can do Government Job")
else:
    print("you are eligible for vote but cannot do government job" )




# percentage={
# "totalPercentage1":60,
# "totalPercentage2":70,
# "totalPercentage3":80
# }
# for key, value in percentage.items():
#     if value>75:
#         print(f"Percentage greater than 75 is {key} and Percentage is {value}%")
#     elif value < 75 and value > 65:
#         print(f"Percentage between 65 and 75 is {key} and Percentage is {value}%")
#     else:
#         print(f"Percentage less than 65 is {key} and Percentage is {value}%")
