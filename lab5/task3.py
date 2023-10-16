def check_city(city_list, new_city):
    if new_city in city_list:
        return "REPEAT"
    else:
        city_list.append(new_city)
        return "OK"


n = int(input("Введите количество названных городов: "))

city_list = []

for _ in range(n):
    city = input(("Введите названный город: "))
    result = check_city(city_list, city)
    print(result)
