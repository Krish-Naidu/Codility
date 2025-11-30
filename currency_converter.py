print("Currency Converter")
print("1. USD to INR")
print("2. USD to GBP")
print("3. GBP to INR")
print("4. GBP to USD")
print("5. INR to USD")
print("6. INR to GBP")

choice = int(input("Enter choice (1-6): "))
amount = float(input("Enter amount: "))

if choice == 1:
    result = amount * 83.12
    print(amount, "USD =", result, "INR")

if choice == 2:
    result = amount * 0.79
    print(amount, "USD =", result, "GBP")

if choice == 3:
    result = amount * 105.20
    print(amount, "GBP =", result, "INR")

if choice == 4:
    result = amount * 1.27
    print(amount, "GBP =", result, "USD")

if choice == 5:
    result = amount / 83.12
    print(amount, "INR =", result, "USD")

if choice == 6:
    result = amount / 105.20
    print(amount, "INR =", result, "GBP")
