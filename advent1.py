list1 = []
list2 = []

with open("advent1.in") as file:
    for line in file:
        parts = line.split(' ')
        list1.append(int(parts[0]))
        list2.append(int(parts[-1]))

similarities = 0
for l1 in list1:
    similarities += l1 * list2.count(l1)

print(similarities)
