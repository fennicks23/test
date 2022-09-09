# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
# c = input('+, -, /, *, **, //, %:')
# if c == '+':
    # print(a + b)
# elif c == '-':
    # print(a-b)
# elif c == '/':
    # print(a/b)
# elif c == '*':
    # print(a*b)
# elif c == '**':
    # print(a**b)
# elif c == '%':
    # print(a%b)
# else:
    # print('Такого выражения нету')

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# n = enumerate(languages)
# for i in (n):
    # print(i)

# a = []
# for i in range(1,1001):
    # if i % 3 == 0 and i % 5 == 0 :
        # a.append(i)
# print(sum(a))

# a = input('Введите дату в формате: "2020-10-24 18:30"')
# print(a)
# dict1= {
    # 
# 
# 
# 
# }


# a = "4729461084"
# b = ','.join(a)
# c = int(str(b))
# # c = int(list(a))
# print(b + b)


# from random import random

# city = ['Bishkek', 'Osh', 'Batken', 'NewYork']
# 
# commands = input('''Выберите действие:
# 1. Добавить 
# 2. Отобразить
# 3. Заменить город 
# 4. Удалить город 
# 5. Посетить слудующий город \n>>> ''').lower()
# if commands == 'добавить':
    # new_city = input('Введите название города: ')
    # if new_city in city:
        # print('Такой город уже есть')
    # else:
        # city.append(new_city)
        # print(city)
# elif commands == 'отобразить':
    # print(city)
# elif commands == 'Заменить город':
    # replace_city = input(f'какой город хоитие заменить: {city}')
    # replaced_city = input('На какой город вы хоитие заменить: ')
    # city[replace_city] = replaced_city
    # print(city)   
# elif commands == 'Удалить город':
    # remove_city = input('Какой город хотите удалить: ')
    # if remove_city in city:
        # city.pop(remove_city)
    # else:
        # print('Такого города нету')
# elif commands == 'Посетить следующий город':
    # print(random(city))