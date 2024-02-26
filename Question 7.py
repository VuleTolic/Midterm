import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

print("Original List:", random_numbers)

for i in range(len(random_numbers)):
    if random_numbers[i] % 2 == 1:
        random_numbers[i] = None
    else:
        random_numbers[i] *= 2

random_numbers = [num for num in random_numbers if num is not None]

print("Modified List:", random_numbers)
