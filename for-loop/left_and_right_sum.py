import math
number = int(input())
left_sum = 0
right_sum = 0

for i in range(number):
    numbers_for_left_side = int(input())
    left_sum += numbers_for_left_side

for i in range(number):
    numbers_for_right_side = int(input())
    right_sum += numbers_for_right_side

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')