def password_check():
    user_password = input("enter ur password:\n ")
    counter = 0

    if len(user_password) >= 8:
        counter = counter + 1
    else:
        print("password must be at least 8 characters long")

    contains_digit = False
    for character in user_password:
        if character.isdigit():
            contains_digit = True
            break

    if contains_digit == True:
        counter = counter + 1
    else:
        print("password must contain digits")


    contains_upper = False
    for upper in user_password:
        if upper.isupper():
            contains_upper = True
            break

    if contains_upper == True:
        counter = counter + 1
    else:
        print("password must contain uppercase letters")



    if counter == 3:
        print("strong password")
    elif counter == 2:
        print(" medium password")
    else:
        print("weak password")

password_check()
