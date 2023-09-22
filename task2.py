# n = int(input())
# str1 = ''
# for i in range(1, n + 1):
#     str1 += str(i)
#     print(str1)


n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
