with open('input2.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

numbers.sort(key=int)

with open('output2.txt', 'w') as file:
    for num in numbers:
        file.write(str(num) + '\n')
