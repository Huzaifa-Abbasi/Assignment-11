''': Create a program that implements the Pomodoro Technique (25 minutes 
work, 5 minutes break). Use a loop and if statements to track time intervals and notify the user 
when to switch between work and breaks'''

pomodoro = 0
work = 25
target = 4

while pomodoro < target:

    work_time = int(input("enter minuets you work ")) 
    if work_time < work:
        
        print(f"You should work more {work - work_time} minutes")
    else:
        pomodoro += 1
        print("You should take a rest")
   
    if pomodoro == target:
        break
print(pomodoro)