with open('input1.txt', 'r') as file:
    numbers = file.read().split()

numbers = [int(num) for num in numbers]

total = 1
for num in numbers:
    total *= num

with open('output1.txt', 'w') as file:
    file.write(str(total))