# Анализатор погоды-2
# Метеостанция каждый час передаёт данные о температуре в текущий момент времени.
# Проанализируйте полученные данные и выведите среднюю, минимальную и
# максимальную температуры за всё время наблюдений.
# Ввод: В первой строке вводится натуральное число n - количество замеров температуры.
# В следующих n строка записаны дробные числа - отдельные измерения времени.
# Вывод: Вывести одну строку в формате:
# 'Avg: a; Min: mn; Max: mx', где a - средняя, mn - минимальная,
# mx - максимальная температуры за время наблюдений.

def weather_analisator():
    number_of_hours = number_of_measurments_input()
    data_sum = 0
    min_ = 9999
    max_ = -9999
    for i in range(number_of_hours):
        entered_weather = data_input()
        data_sum += entered_weather
        if entered_weather > max_:
            max_ = entered_weather
        if entered_weather < min_:
            min_ = entered_weather
    avg = data_sum / number_of_hours
    print(f'Avg: {round(avg, 2)}; Min: {min_}; Max: {max_}')


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
