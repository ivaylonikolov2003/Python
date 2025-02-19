import sys
max_number = -sys.maxsize

while True:
    num = input()

    if num == "Stop":
        break

    num = int(num)
    if num >= max_number:
        max_number = num

print(max_number)