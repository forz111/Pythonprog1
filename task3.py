n = int(input()) + 1
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print(*range(1, i), *range(1, i - 1)[::-1], sep='')
