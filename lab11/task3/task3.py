import csv
import matplotlib.pyplot as plt

with open('passengers.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)

months = [row[0] for row in data]
passengers = [int(row[1]) for row in data]

# Линейный график
plt.figure()
plt.plot(months, passengers)
plt.title('Пассажиропоток за все время')
plt.xlabel('Месяц')
plt.ylabel('Пассажиры')
plt.show()

months_1951_1955 = [months[i] for i in range(len(months)) if '1951' <= months[i][:4] <= '1955']
passengers_1951_1955 = [passengers[i] for i in range(len(months)) if '1951' <= months[i][:4] <= '1955']

# Гистограмма
plt.figure()
plt.hist(passengers_1951_1955, bins=12)
plt.title('Распределение пассажиров по месяцам, 1951 - 1955')
plt.xlabel('Пассажиры')
plt.ylabel('Частота')
plt.show()
