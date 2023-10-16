with open('data.txt', 'r', encoding='utf-8') as file:
    children_data = [line.strip().split() for line in file]

children_data = [(surname, name, int(age)) for surname, name, age in children_data]

youngest_child = min(children_data, key=lambda x: x[2])
oldest_child = max(children_data, key=lambda x: x[2])

with open('youngest.txt', 'w', encoding='utf-8') as file:
    file.write(f"Фамилия: {youngest_child[0]}\n")
    file.write(f"Имя: {youngest_child[1]}\n")
    file.write(f"Возраст: {youngest_child[2]}\n")

with open('oldest.txt', 'w', encoding='utf-8') as file:
    file.write(f"Фамилия: {oldest_child[0]}\n")
    file.write(f"Имя: {oldest_child[1]}\n")
    file.write(f"Возраст: {oldest_child[2]}\n")
