# Анализатор погоды
# Метеостанция каждый час передаёт данные о температуре в текущий момент времени.
# Проанализируйте полученные данные и выведите среднюю температуру за сутки.
# Ввод: 24 дробных числа, каждое в отдельной строке - температура в определённый час.
# Вывод: одно число - средняя температура по полученным данным

def weather_analisator():
    number_of_hours = 24                    # Убрал кол-во часов в переменную,
    data_sum = 0                            # чтобы проще менять на меньшие значения для проверки
    for i in range(number_of_hours):
        data_sum += data_input()
    return data_sum / number_of_hours


def data_input():
    while True:
        try:
            weather_data = float(input('Введите температуру: '))
            return weather_data
        except ValueError:
            print('Температуру необходимо ввести в виде числа, попробуй ещё раз')


answer = weather_analisator()
print(f'Средняя температура: {round(answer, 2)}')
