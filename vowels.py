Input = input("enter a string: \n")
vowels = "aeiouAEIOU"
count = 0
for i in Input:
    if  i in vowels:
        count = count + 1 
        
    
print(count)