array = []

for i in range(0, 1000, 3):
    array.append(i)
for i in range(0, 1000, 5):
    array.append(i)

array = list(set(array))

print(sum(array))
