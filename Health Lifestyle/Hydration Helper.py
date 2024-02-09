'''Design a program that prompts the user for their weight and desired level of 
hydration (e.g., light, moderate, intense exercise). Use nested if-else statements to suggest the 
amount of water they should drink throughout the day.'''

weight = int(input("Enter the weight in kg: "))
exercise = input("Enter the level of hydration (light, moderate, intense): ")

if weight < 50:
    if exercise == "light":
        print("You should drink 6 liters of water")
    elif exercise == "moderate":
        print("You should drink 7 liters of water")
    elif exercise == "intense":
        print("You should drink 8 liters of water")
    else:
        print("Invalid exercise level")
elif weight >= 50:
    if exercise == "light":
        print("You should drink 7 liters of water")
    elif exercise == "moderate":
        print("You should drink 9 liters of water")
    elif exercise == "intense":
        print("You should drink 10 liters of water")
    else:
        print("Invalid exercise level")
else:
    print("Invalid input")