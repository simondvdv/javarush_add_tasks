# Вводится n - количество элементов. В следующих n строках вводятся
# сами элементы - целые числа.
# Вывести сумму нечётных кубов тех чётных элементов, которые не кратны 12.
elements_num = int(input())
user_list = []
for i in range(elements_num):
    user_list.append(int(input()))
answer_list = [i**3 for i in user_list if i % 2 == 0 and i % 12 != 0]
print(sum(answer_list))
