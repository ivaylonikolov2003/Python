age_of_lily = int(input())
price_for_washing_machine = float(input())
price_for_toy = int(input())

toys = 0
money = 0


for curr_age in range(1, age_of_lily + 1):
    if curr_age % 2 != 0:
        toys += 1
    else:
        money_given = (curr_age * 5) - 1
        money += money_given

toys_money = toys * price_for_toy
money += toys_money


if money >= price_for_washing_machine:
    money_left = money - price_for_washing_machine
    print(f"Yes! {money_left:.2f}")
else:
    money_more_needed = price_for_washing_machine - money
    print(f"No! {money_more_needed:.2f}")