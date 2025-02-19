const = 10000
sum_steps = 0

while sum_steps < const:
    steps = input()
    if steps == 'Going home':
        home_steps = input()
        sum_steps += int(home_steps)
        break
    sum_steps += int(steps)

steps_difference = abs(sum_steps - const)
if sum_steps == const or sum_steps > const:
    print("Goal reached! Good job!")
    print(f"{steps_difference} steps over the goal!")

if sum_steps < const:
    print(f"{steps_difference} more steps to reach goal.")




