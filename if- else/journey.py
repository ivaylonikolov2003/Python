budget = float(input())
season = input()

destination = 0
kind_of_vacation = 0
price_for_trip = 0

if season == 'summer':
    kind_of_vacation = 'Camp'
    if budget <= 100:
        destination = 'Bulgaria'
        price_for_trip = 0.3 * budget
    elif budget <= 1000:
        destination = 'Balkans'
        price_for_trip = 0.4 * budget
    else:
        kind_of_vacation = 'Hotel'
        destination = 'Europe'
        price_for_trip = 0.9 * budget
elif season == 'winter':
    kind_of_vacation = 'Hotel'
    if budget <= 100:
        destination = 'Bulgaria'
        price_for_trip = 0.7 * budget
    elif budget <= 1000:
        destination = 'Balkans'
        price_for_trip = 0.8 * budget
    else:
        destination = 'Europe'
        price_for_trip = 0.9 * budget

print(f'Somewhere in {destination}')
print(f'{kind_of_vacation} - {price_for_trip:.2f}')