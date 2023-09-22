def check(a, b, c):
    if a == b and b == c:
        return 3
    if a == b or a == c or b == c:
        return 2
    if a != b and a != c and b != c:
        return 0


print("Введите значения")
print(check(int(input()), int(input()), int(input())))
