def number_of_repetitions(strings):
    occurrences = {}
    for string in strings:
        if string in occurrences:
            occurrences[string] += 1
        else:
            occurrences[string] = 1
    return occurrences.values()


# Входные данные 1
input_data_1 = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
occurrences_1 = number_of_repetitions(input_data_1)
print(*occurrences_1)

# Входные данные 2
input_data_2 = ['aaa', 'bbb', 'ccc']
occurrences_2 = number_of_repetitions(input_data_2)
print(*occurrences_2)

# Входные данные 3
input_data_3 = ['abc', 'abc', 'abc']
occurrences_3 = number_of_repetitions(input_data_3)
print(*occurrences_3)
