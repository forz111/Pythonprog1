def number_to_text(number):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять',
             'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
             'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

    if number == 0:
        return 'ноль'

    if number < 0 or number > 1000:
        return 'Число должно быть в диапазоне от 1 до 1000'

    if number < 20:
        return units[number]

    if number < 100:
        return tens[number // 10] + ' ' + units[number % 10]

    if number < 1000:
        return hundreds[number // 100] + ' ' + number_to_text(number % 100)

    if number == 1000:
        return 'тысяча'


while True:
    try:
        number = int(input('Введите число от 1 до 1000: '))
        result = number_to_text(number)
        print(result)
        break
    except ValueError:
        print('Неверный формат числа. Попробуйте ещё раз.')
