num = int(input("Введите количество ступенек пирамиды: "))


def as_str(i):
    s = ""
    if i < 10:
        s = "  "
    elif i < 100:
        s = " "
    return s + str(i)


allrows = ""
for j in range(1, num + 2):
    # пробелы для выравнивания
    row = " " * 4 * (num - j + 1)
    # левая часть
    for i in range(1, j):
        s = as_str(i)
        row += s + " "
    # правая часть
    for i in range(j - 1, 1, -1):
        s = as_str(i - 1)
        row += s + " "

    row += "\n"
    allrows += row

print(allrows)
