bot = input("Convert from? Enter '1' for miles(default) or '2' for kilometre:\n ")
while True:
    try:
        distance = int(input("what is the distance:\n "))
        break
    except ValueError:
        print("Please enter an integer.")
if bot == "1":
    distance = distance * 1.6 
    print(distance) 
else:
    distance = distance / 1.6
    distance = round(distance, 2)
    print(distance)
