random_array = [1, 4, 3, 2, 5, 8, 7, 3, 2, 5, 8, 6]
for j in range(len(random_array)):
    for i in range(len(random_array) - 1):
        if random_array[i] > random_array[i + 1]:
            random_array[i], random_array[i + 1] = random_array[i + 1], random_array[i]


print(random_array)
