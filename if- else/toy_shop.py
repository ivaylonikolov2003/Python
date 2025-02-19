price_for_trip = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())
discount = 0
money_left_over = 0
missing_money = 0


price = number_of_puzzles * 2.60 + number_of_dolls * 3 + number_of_bears * 4.10 + number_of_minions * 8.20 + number_of_trucks * 2
number_of_toys = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks

if number_of_toys >= 50:
    discount = price * 0.25

final_price = price - discount
rent = final_price * 0.1
profit = final_price - rent

if profit >= price_for_trip:
    money_left_over = profit - price_for_trip
    print(f"Yes! {money_left_over:.2f} lv left.")

if profit <= price_for_trip:
    missing_money = price_for_trip - profit
    print(f"Not enough money! {missing_money:.2f} lv needed.")