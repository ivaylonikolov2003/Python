type_flower = input()
number_flower = int(input())
budget = int(input())

price_per_flower = 0
discount = 0
higher_rate_percent = 0

if type_flower == 'Roses':
    price_per_flower = 5
    if number_flower > 80:
        discount = 0.1
elif type_flower == 'Dahlias':
    price_per_flower = 3.80
    if number_flower > 90:
        discount = 0.15
elif type_flower == 'Tulips':
    price_per_flower = 2.80
    if number_flower > 80:
        discount = 0.15
elif type_flower == 'Narcissus':
    price_per_flower = 3
    if number_flower < 120:
        higher_rate_percent = 0.15
elif type_flower == 'Gladiolus':
    price_per_flower = 2.50
    if number_flower < 80:
        higher_rate_percent = 0.20

final_price = number_flower * price_per_flower
final_price -= final_price * discount
final_price += final_price * higher_rate_percent

if budget >= final_price:
    money_left = budget - final_price
    print(f"Hey, you have a great garden with {number_flower} {type_flower} and {money_left:.2f} leva left.")
else:
    money_more_needed = final_price - budget
    print(f"Not enough money, you need {money_more_needed:.2f} leva more.")