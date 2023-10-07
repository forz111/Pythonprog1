def decompress_str(compressed_string):
    decompressed_string = ""
    total = 0

    while total < len(compressed_string):
        char = compressed_string[total]
        count = ""

        total += 1
        while total < len(compressed_string) and compressed_string[total].isdigit():
            count += compressed_string[total]
            total += 1

        count = int(count) if count else 1
        decompressed_string += char * count

    return decompressed_string


compressed_string = input("Введите сжатую строку: ")
decompressed_result = decompress_str(compressed_string)
print(f"Восстановленная строка: {decompressed_result}")
