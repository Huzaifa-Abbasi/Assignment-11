age = int(input("Enter your age: "))

if 16 < age < 20:
    print("You are a teenager")
elif 20 <= age <= 25:
    print("You are an adult")
elif age > 50:
    print("You are a senior citizen")
else:
    print("You are in a different age category")
