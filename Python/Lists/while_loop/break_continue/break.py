correct_pin = "1234"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    pin = input("enter your pin")
    attempts += 1
    if pin == "":
        print("You have not entered anything")
        continue
    if pin == correct_pin:
        print("You have entered the correct pin")
        break
    remaining_attempts = max_attempts - attempts
if remaining_attempts>0:
    print(f" invalid pin.You have {remaining_attempts} attempts left")
else:
    print(" account locked.You have run out of attempts")