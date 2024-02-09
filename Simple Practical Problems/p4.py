'''Create a program that simulates a simple ATM machine. It should ask the user for their PIN, 
verify it, and then allow them to withdraw money if the balance is sufficient.'''

pin = 1122
balance = 1000
enter_pin = int(input("Enter the Pin "))
enter_balance = int(input("Enter the Amount you want "))
if enter_pin == pin and enter_balance <= balance:
    print("With draw compelete ")
elif enter_pin == pin and enter_balance > balance:
    print("Insufficient Balance")
else:
    print("Wrong pin")