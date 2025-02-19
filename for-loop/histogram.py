num = int(input())
counter_p1 = 0
counter_p2 = 0
counter_p3 = 0
counter_p4 = 0
counter_p5 = 0

for i in range(0, num):
    curr_number = int(input())
    if curr_number < 200:
        counter_p1 += 1
    elif 200 <= curr_number <= 399:
        counter_p2 += 1
    elif 400 <= curr_number <= 599:
        counter_p3 += 1
    elif 600 <= curr_number <= 799:
        counter_p4 += 1
    elif curr_number >= 800:
        counter_p5 += 1

print(f'{counter_p1 / num * 100:.2f}%')
print(f'{counter_p2 / num * 100:.2f}%')
print(f'{counter_p3 / num * 100:.2f}%')
print(f'{counter_p4 / num * 100:.2f}%')
print(f'{counter_p5 / num * 100:.2f}%')




