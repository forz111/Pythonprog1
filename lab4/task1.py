def swap_min_max(numbers):
    if len(numbers) < 2:
        return numbers

    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))

    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

    return numbers


input_list = [int(x) for x in input("Введите числовую последовательность через пробел: ").split()]
result_list = swap_min_max(input_list)
print(result_list)
