def compress_str(string):
    compressed_string = ""
    total = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            total += 1
        else:
            compressed_string += string[i - 1] + (str(total) if total > 1 else "")
            total = 1

    compressed_string += string[-1] + (str(total) if total > 1 else "")

    return compressed_string


input_string = input("Введите строку символов: ")
compressed_result = compress_str(input_string)
print(f"Сжатый формат строки: {compressed_result}")
