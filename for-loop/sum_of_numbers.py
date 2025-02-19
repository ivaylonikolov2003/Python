numbers = int(input())
sum_numbers = 0

while True:
    curr_number = int(input())
    sum_numbers += curr_number

    if sum_numbers >= numbers:
        print(sum_numbers)
        break


