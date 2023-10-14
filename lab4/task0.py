def find_greater(numbers):
    greater_elements = []
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            greater_elements.append(numbers[i])
    return greater_elements


input_list = [int(x) for x in input("Введите числовую последовательность через пробел: ").split()]
result_list = find_greater(input_list)
print(result_list)
