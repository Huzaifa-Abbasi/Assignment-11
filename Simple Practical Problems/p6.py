'''Implement a program that takes a user's input of a year and month and prints out the number 
of days in that month, considering leap years.'''

year = int(input("Enter the year "))
month = input("Enter the month ")

short_months = ["april","june","september","november"]
long_months = ["january", "march", "may", "july", "august", "october", "december"]
alone = ["february"]

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month in short_months:
    print(f"The year {year} is leap, and {month} has 30 days.")
elif (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month in long_months:
    print(f"The year {year} is leap, and {month} has 31 days.")
elif (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month in alone:
    print(f"The year {year} is leap, and {month} has 29 days.")
else:
    print(f"The year {year} is not leap, and {month} has 28 or 30 or 31 days.")



