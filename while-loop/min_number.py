import sys
min_number = sys.maxsize

while True:
    num = input()

    if num == "Stop":
        break

    num = int(num)
    if num <= min_number:
        min_number = num

print(min_number)