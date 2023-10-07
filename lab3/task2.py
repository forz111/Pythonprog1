def most_frequent_characters(string):
    string = string.replace(" ", "")

    counter = {}

    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    # Сортируем словарь по частоте символов в порядке убывания
    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    most_common = sorted_counter[:3]

    return most_common


input_string = input("Введите строку для подсчета количества символов: ")
frequent_characters = most_frequent_characters(input_string)
print("Три наиболее часто встречающихся символа:")
for char, count in frequent_characters:
    print(f"Символ: {char}, Количество: {count}")
