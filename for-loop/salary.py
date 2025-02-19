tabs = int(input())
salary = int(input())

facebook = 150
instagram = 100
reddit = 50

for a in range(1, tabs + 1):
    tabs_open = (input())

    if tabs_open == 'Facebook':
        salary -= facebook
    elif tabs_open == 'Instagram':
        salary -= instagram
    elif tabs_open == "Reddit":
        salary -= reddit

if salary <= 0:
    print(f"You have lost your salary.")
else:
    print(salary)