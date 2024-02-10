'''Develop a program that allows the user to add tasks to a to-do list. Use if statements 
to categorize tasks as urgent, important, or less important based on their due date and priority.'''
   
urgent_task = []
important_task = []
less_important_task = []

while True:
    task = input("Enter the tasks ").lower()
    importance = input("Enter the Importance ").lower()

    if importance == "urgent":
        urgent_task.append(task)

    elif importance == "important":
        important_task.append(task)
    
    elif importance == "less important":
        less_important_task.append(task)

    else:
        print("Invalid Information")


    user_input = input("Do you want to add more task Yes/No ").lower()
    if user_input == "no":
        break

print("These are the urgent task ",urgent_task)
print("These are the important task ", important_task)
print("These are the less important task ", less_important_task)