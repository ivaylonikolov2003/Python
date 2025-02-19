n = 1
sum = 0

for i in range(1000000):
    if i % 2 == 0:
        sum += 4/n
    else:
        sum -= 4/n
    n += 2

print(sum)