'''Write a Python script that takes a user's input of three sides of a triangle and determines 
whether it is equilateral, isosceles, or scalene.'''

side_1 = int(input("Enter The 1st side of triangle "))
side_2 = int(input("Enter The 2nd side of triangle "))
side_3 = int(input("Enter The 3rd side of triangle "))

if side_1 == side_2 == side_3:
    print("The Triangle is Equilateral")
elif (side_1 != side_3) or (side_1 != side_2):
    print("The Triangle is Isosceles")
else:
    print("The Triangle is Scalene ")