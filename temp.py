# # for i in range(0, 4):
# #     print(i)

# # my_dict = {'a': 1, 'b': 2, 'c': 3}
# # for index, (key, value) in enumerate(my_dict.items()):
# #     print(index, key, value)

# # #loop throught a dictionary
# # for key in my_dict:
# #     print(key, my_dict[key])













# # for loop without index
# my_array = [3, 5, 76]
# my_array[2] = 10
# my_var = my_array[2]
# for x  in my_array:
#     print(x)

# #for loop with index 
# for i in range(len(my_array)):
#     print(my_array[i])

# #for loop without index
# my_dict = dict()
# my_dict["name"] = "krish"
# my_dict["last_name"] = "naidu"
# my_dict["age"] = 17 

# # option one iterate over keys 
# my_var = my_dict["name"]
# for key in my_dict:
#     print(key, my_dict[key])

# # iterate over keys and values 
# for key,value in my_dict.items():
#     print(key, value)


dob = "28042008"
birth_day = int(dob[0:2])
birth_month = int(dob[2:4])
birth_year = int(dob[4:8])
today_day = 9
today_month = 11
today_year = 2025
age_years = today_year - birth_year
age_months = today_month - birth_month
age_days = today_day - birth_day
print(age_years, age_months, age_days)


# for index, (key, value) in enumerate(my_dict.items()):
#     print(index, key, value)




# array = [2, 5, 6, 768]
# for x in array:
#     print(x)

# length = len(array)
# for i in range(length):
#     print(array[i])


# bot_dict = {"phone" : "IPhone", "ram" : "120gb"}
# bot_dict ["OS"] = "iOS"

# for key in bot_dict:
#     print(key, bot_dict[key])

# bot_dict["ram"] = "256gb"
# os_name = bot_dict["OS"]

# for i in range(length):
#     array[i] = array[i] + 1
# print(array)



# bot_dict = {"name" : "rohan", "last_name" : "phill"}
# bot_dict ["age"] = 18

# my_dict = dict()
# my_dict["name"] = "krish"
# my_dict["last_name"] = "naidu"
# my_dict["age"] = 17 

# # new_dict = bot_dict.copy()

# # bot_dict["age"] = my_dict["age"]
# # bot_dict["name"] = my_dict["name"]
# # bot_dict["last_name"] = my_dict["last_name"]
# # print(bot_dict)

# # my_dict["age"] = new_dict["age"]
# # my_dict["name"] = new_dict["name"]
# # my_dict["last_name"] = new_dict["last_name"]
# # print(my_dict)

# age = my_dict["age"]
# my_dict["age"] = bot_dict["age"]
# bot_dict["age"] = age 










# my_array = [3, 5, 76]
# bot_array = [4, 7, 43]
# final_array = [0, 0, 0]

# if my_array[0] > bot_array[0]:
#     final_array[0] = my_array[0]
# else:
#     final_array[0] = bot_array[0]

# if my_array[1] > bot_array[1]:
#     final_array[1] = my_array[1]
# else:
#     final_array[1] = bot_array[1]

# if my_array[2] > bot_array[2]:
#     final_array[2] = my_array[2]
# else:
#     final_array[2] = bot_array[2]

# final_array[0] = max(my_array[0], bot_array[0])
# final_array[1] = max(my_array[1], bot_array[1])
# final_array[2] = max(my_array[2], bot_array[2])

# for i in range(len(my_array)):
#     final_array[i] = max(my_array[i], bot_array[i])

# print(final_array)

# a = "asdasdasd"
# for i in a:
#     print(i)
# # a String is nothing but an array of characters. 
# for i in range(len(a)):
#     print(i, a[i])



# first_name = "krish"
# last_name = "naidu"

# first_name[0] = "K"
# last_name[0] = "N"
# full_name = first_name +" "+ last_name
# print(full_name)







bot = "krish is a bot"
# for x in bot:
#     print(x)


# for i in range(len(bot)):
#     print(i,bot[i])

counter = 0
my_dict = {}
list_of_words = bot.split()
for word in list_of_words:
    counter = counter + 1
    key_counter = str(counter)
    my_dict.update({key_counter : word}) 

print(my_dict)