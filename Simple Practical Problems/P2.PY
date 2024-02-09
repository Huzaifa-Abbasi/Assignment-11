'''Develop a program that prompts the user to enter their current temperature in Celsius and 
prints out whether they should wear a jacket (if temperature is below 20°C) or not.'''

temperature = int(input("Enter the temperature in Celsius "))
if temperature <= 20:
    print('wear the jacket ')
else:
    print("NO Need Jacket")