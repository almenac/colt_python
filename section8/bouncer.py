age = input("How old are you? ")

#Normaali versio

# if age:
#     age = int(age)
#     if age >= 18 and age < 21:
#         print("You can enter, but need a wristband.")
#     elif age >= 21:
#         print("You're good to enter and you can drink.")
#     else:
#         print("You can't come in, little one :(")
# else:
#     print("Please enter an age.")

# Tehokkaampi versio

if age:
    age = int(age)
    if age >= 21:
        print("You're good to enter and you can drink.")        
    elif age >= 18:
        print("You can enter, but need a wristband.")
    else:
        print("You can't come in, little one :(")
else:
    print("Please enter an age.")