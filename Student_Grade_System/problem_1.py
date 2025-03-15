# user_age = int(input("Enter Your Age : "))
# if user_age <= 5:
#     print("You are Baby")
# elif user_age <=18:
#     print("You are teenager")
# elif user_age <=30:
#     print("You are Young")
# elif user_age <= 50:
#     print("You are Middle Age")
# else:
#     print("You are Old")                

age = int(input("Enter your age : "))
price = 12 if age >= 18 else 8
day = input("Enter the day : ") 
if day == "wednesday":
    price = price -2
    print(f"Your ticket price is ${price}") 
else:
    print(f"Your ticket price is ${price}")     