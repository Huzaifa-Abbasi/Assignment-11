''': Design a program that helps users find a common meeting time among a 
group. Use if-else statements to check for available time slots in each user's calendar and 
suggest suitable meeting times.'''

user1 = set(["monday", "friday", "sunday"])
user2 = set(["tuesday", "thursday", "sunday"])
user3 = set(["sunday", "monday", "friday"])



common_day = user1.intersection(user2, user3)

if common_day:
    print("Common meeting times:", common_day)
else:
    print("No common meeting time.")

