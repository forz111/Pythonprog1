def get_str(lst):
    return ' '.join(map(str, lst))


size = int(input("Введите количество строк треугольника Паскаля: "))
triangle_sp = []

for i in range(size):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle_sp[i - 1][j - 1] + triangle_sp[i - 1][j]
    triangle_sp.append(row)

width = len(get_str(triangle_sp[-1]))

for line in triangle_sp:
    print(get_str(line).center(width))
