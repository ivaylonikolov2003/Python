grades = int(input())
time_of_day = input()
outfit = ""
shoes = ""

if time_of_day == 'Morning':
    if 10 <= grades <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < grades <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "T-Shirt"
        shoes = "Sandals"

elif time_of_day == 'Afternoon':
    if 10 <= grades <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < grades <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    else:
        outfit = "Swim suit"
        shoes = "Barefoot"

elif time_of_day == 'Evening':
    if 10 <= grades <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < grades <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {grades} degrees, get your {outfit} and {shoes}.")
