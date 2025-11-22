phone_book = {}

while True: 
    name = input("enter name: \n")
    if name.replace(" ", "") == "":
        break

    phone = input("enter phone number: \n")
    phone_book[name] = phone 

print(phone_book)


    
     