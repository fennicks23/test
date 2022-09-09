# a = [True, True, True]
# print = (all(a))
# all выводит если они все одинаковые как тру и фолс 

# a = [2,4,6,8,7,6,4,20]
# b = []
# for i in a:
    # if i % 2 == 0:
        # b.append(True)
    # else:
        # b.append(False)
# print(all(b))

# a = [2,4,6,8,7,6,4,20]
# b = []
# for i in a:
    # if i % 2 == 0:
        # b.append(True)
    # else:
        # b.append(False)
# print(any(b)) 
# возврощает тру если верно хоть одно значение 
# a = [False,False,True]
# print(any(a))

# abs выводит минус числа как плюсы
# a = -25
# print(abs(a))

# min and max and sum 
# a = [2,3,4,5,6,7,8,9]
# print()

# идентично с реверс 
# a = [2,4,6,8,7,6,4,20]
# a.reverse()
# b = reversed(a)
# print (list(b))

# eveal
# a = eval('19 + 33')
# print(a)

# list1 = ['sadas', 'asdasf', 'asdqw']
# print(slice(list1, 1,3))

# round округляет до выбранного значение после запитой
# a = 10/3
# print(round(a,16))

# try 
# except выводит ошибку
# ZeroDevisionError писать после except
# else тоже работает
# finaly отработает в любом случае
# try:
    # a = int(input('chislo: '))
    # b = int(input('chislo: '))
    # print(round(a/b))
# except ZeroDivisionError:
    # print('Na nol delit nelzya')
# except ValueError:
    # print('Tolko chisla')
# Exception выводит ошибку в коде 


# str_1 = 'Python'
# a = slice(10)
# print(str_1[a])

# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
# try:
    # set(values)
    # print('Можно сконвертировать')
# except:
    # print('Нельзя конвертировать')

# пустой сет создаем с ()
# set1 = set()
# for i in range (5):
    # i = int(input('Введите число: '))
    # set1.add(i)
    # куда нужно добвить .add (что нужно добавить)
# print(min(set1))


# a = input('Введите функцию: ')
# try:
    # eval(a) 
    # print('функция есть')
# except:
    # print('Такой функции нету')

# a = int(input('Введите сумму:'))
# if a >= 50000:
    # x = 3.47
    # b = a *(x /100)
    # print(round(b))

# x = [34,23,46]
# try:
    # a = int(input('Введите цифру : '))
    # b = int(input('Введите индекс : '))
    # print(a / x[b])
# except NameError:
    # print('На ноль не делится')
# except TypeError:
    # print('Вводите только цифры')
# except IndexError:
    # print('Такого индекса нет')
# except ValueError:
    # print('Вводите только цифры')

# Rat = 10
# Rin = 15
# Rwo = 20
# try:

#     for e in range(-at, at):
#         print(wo / e)
#     if at > '5':
#         print("at > 5)
# except NameError:
#     print('На ноль не делится')
# except ValueError:
#     print('Вводите только цифры')
# except Exception as e:
#     print(f'Код вырубился из-за ошибки: {e}')

# lst1 = []
# for i in range(10):
#     a = list(reversed(lst1))
#     sls_obj = slice('0','8')
#     lst1.append(i)
#     print(a,sls_obj)


# a = (0)
# b = (1)
# numbers = []
# while b > a:
#     b += 1
#     numbers.append(b)
#     print(numbers)

# dict1 = {'name': 'john', 'lastname': 'Snow', 12:'age'}
# for x in dict1.keys():
    # x += 'abc'
    # print(dict1)
