''' Write a program that asks the user for their 
age, weight, and activity level, then calculates their daily 
calorie goal based on recommended guidelines. Use if/else statements to adjust the goal based on the user's activity 
level.'''

def calculate_calories(gender, height, age, weight, activity_level):
    if gender == "man":
        BMR = 88.362 + (13.397 * weight)  + (4.799 * height) - (5.677 * age )
        
    elif gender == "woman":
        BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        print("Invalid Spelling ")


    if activity_level == "sedentary":
       ted = BMR * 1.2
    elif activity_level == "lightly active":
        ted = BMR * 1.375
    elif activity_level == "moderately active":
        ted = BMR * 1.55
    
    return ted


gender = input("Enter the Gender ").lower()
height = int(input("Enter the Height in CM "))
age = int(input("Enter The Age in Year "))
weight = int(input("Enter the Weight In KG "))
activity_level = input("Enter the Level ").lower()

total = (calculate_calories(gender, height, age, weight, activity_level))
print(f"Daily Goal Of Calories Is {total} ")