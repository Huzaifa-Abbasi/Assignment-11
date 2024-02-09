'''Develop a Python script that takes a user's input of a month (as a number) and prints out the 
number of days in that month.'''

short_months = ["april","june","september","november"]
long_months = ["january", "march", "may", "july", "august", "october", "december"]
alone = ["february"]

month = input("Enter the Month ").lower()
if month in short_months:
    print("there are 30 days In ", month)
elif month in long_months:
    print("there are 31 days In ", month)
elif month in alone:
    print("There is 28 or 29 days in ",month)
else:
    print("Wrong Spelling")