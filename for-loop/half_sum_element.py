import sys

number = int(input())
sum_numbers = 0
max_num = -sys.maxsize

for num in range(0, number):
    current_number = int(input())
    if current_number > max_num:
        max_num = current_number
    sum_numbers += current_number

# намира сумата без максималното число
sum_numbers -= max_num


if sum_numbers == max_num:
    print('Yes')
    print(f'Sum = {sum_numbers}')
else:
    diff = abs(sum_numbers - max_num)
    print('No')
    print(f'Diff = {diff}')
