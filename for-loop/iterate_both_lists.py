list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
reverse_list2 = list2[::-1]

for x, i in zip(list1, reverse_list2):
    print(x, i)


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for x in list1:
    if x == "":
        list1.remove(x)

print(list1)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1[2][2])


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)

list1 = [5, 10, 15, 20, 25, 50, 20]
list1[3] = 200
print(list1)

for x in list1:
    if x == 20:
        list1.remove(x)

print(list1)

def swaplist(newlist):
    size = len(newlist)
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size - 1] = temp

    return newlist


newList = [12, 35, 9, 56, 24]

print(swaplist(newList))


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))