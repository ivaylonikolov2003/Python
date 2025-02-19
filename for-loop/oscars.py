actor_name = input()
points_from_academy = float(input())
numbers_of_grade = int(input())

for i in range(0, numbers_of_grade):
    name_of_jury = input()
    points_from_jury = float(input())
    length_of_name = len(name_of_jury)

    curr_points = (length_of_name * points_from_jury) / 2

    points_from_academy += curr_points

    if points_from_academy >= 1250.5:
        break

if points_from_academy >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points_from_academy:.1f}!")
else:
    needed_points = 1250.5 - points_from_academy
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")