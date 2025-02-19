needed_money = float(input())
owned_money = float(input())

consecutive_day_count = 0
total_days_count = 0

while owned_money < needed_money and consecutive_day_count < 5:
    command = input()
    money = float(input())
    total_days_count += 1

    if command == 'save':
        owned_money += money
        consecutive_day_count = 0
    elif command == 'spend':
        owned_money -= money
        consecutive_day_count += 1
        if owned_money < 0:
            owned_money = 0

if consecutive_day_count == 5:
    print("You can't save the money.")
    print(total_days_count)

if owned_money >= needed_money:
    print(f"You saved the money for {total_days_count} days.")
