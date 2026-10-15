running_total = 0

while True:
    user_number = int(input("What number? "))
    if user_number == 0:
            print(running_total)
            break
    else:
         running_total = user_number + running_total

