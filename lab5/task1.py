def count_numbers(numbers):
    unique_numbers = set(numbers)
    return len(unique_numbers)


input_data_1 = [1, 2, 3, 2, 1]
unique_count_1 = count_numbers(input_data_1)
print(unique_count_1)

input_data_2 = [1, 2, 3, 4, 5, 6, 7]
unique_count_2 = count_numbers(input_data_2)
print(unique_count_2)

input_data_3 = [1, 1, 1, 1, 1]
unique_count_3 = count_numbers(input_data_3)
print(unique_count_3)

input_data_4 = [1, 2, 3, 1, 1]
unique_count_4 = count_numbers(input_data_4)
print(unique_count_4)
