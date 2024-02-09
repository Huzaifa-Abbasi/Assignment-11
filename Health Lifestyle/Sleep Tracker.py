'''Sleep Tracker: Create a program that asks the user for their 
bedtime and wake-up time, then calculates their total sleep 
duration. Use if statements to determine if they met the recommended sleep amount and 
provide feedback accordingly.'''

bed_time = int(input("Enter the bed time "))
wake_up_time = int(input("Enter the wake up time  "))

duration = wake_up_time - bed_time

if duration < 8:
    print(duration,"You need proper sleep")
elif duration > 8:
    print(duration, "you should watcher your sleep ")
else:
    print("prefect sleep")