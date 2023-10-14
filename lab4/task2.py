def count_common_numbers(list1, list2):
    common_numbers = set(list1) & set(list2)
    return len(common_numbers)


list1 = [int(x) for x in input("Введите 1-ю числовую последовательность через пробел: ").split()]
list2 = [int(x) for x in input("Введите 2-ю числовую последовательность через пробел: ").split()]
count = count_common_numbers(list1, list2)
print("Количество общих чисел:", count)
