# Анализатор погоды-3 (частичное среднее)
# Метеостанция каждый час передаёт данные о температуре в текущий момент времени.
# Анализируйте полученные данные и выводите среднюю температуру по уже переданным данным.
# Ввод: В первой строке вводится натуральное число n - количество замеров температуры.
# В следующих n строках записаны дробные числа - отдельные измерения времени.
# Вывод: Вывести n чисел в одну строку через пробел(допускается лишний
# пробел после последнего числа). k-е число должно представлять собой
# среднюю температуру по первым k переданным данным.

# Пример:
# Ввод:
# 5
# 23.5
# 25.5
# 23
# 20.5
# 18.5
# Вывод:
# 23.5
# 24.5
# 24.0
# 23.125
# 22.2

def weather_analisator():
    number_of_hours = number_of_measurments_input()
    data_sum = 0
    avg = 0
    for i in range(number_of_hours):
        entered_weather = data_input()
        data_sum += entered_weather
        avg = data_sum / (i + 1)
        print(f'Avg: {round(avg, 2)}')


def data_input():
    while True:
        try:
            weather_data = float(input('Введите температуру: '))
            return weather_data
        except ValueError:
            print('Температуру необходимо ввести в виде числа, попробуй ещё раз')


def number_of_measurments_input():
    while True:
        try:
            number_of_measurments = int(input('Введите количество замеров температуры: '))
            if number_of_measurments < 1:
                print('Введите пожалуйста натуральное число')
                continue
            return number_of_measurments
        except ValueError:
            print('Необходимо ввести целое число, попробуйте ещё раз.')


weather_analisator()