# {} словарь dict-dictionary
# dict1 = {}
# print = (type (dict1))

# d = dict (short = 'dict', long = 'dictionary')
# print (d, end= ' ')
# можно { } переносить в низ

# сначала ключ потом : значение    писать через запитую
# можно добавть список через [] и кортедж через ()
# len считает количество ключей 
# добака ключа  dict1 ['one'] = 1    обращение к словарю через [' '] и = значение 
# переназначить можно так же
# extend обьеденить списки
# .updtae добавление словарей 
# .pop работает на словарях и удаляет по ключу 
# .get возвращение по ключу значение 
# print (person ['name']) выводит значение по ключам
# .clear чистит словарь
# .copy() копия словаря на переменную
# .setdefault (ключ , 'значение') нельзя менять можно только добавить, создает новую пару
# .values() выводит только значения 
# .keys () выводит только ключи
# .items () выводит и ключ и значения 

# for key in d:
    # print (key)
# проходит по словаю и выводит только ключи

# for value in d.values():
    # print (value, end = ' ')

# for key, value in d.items():
    # print(f'{key} = {value}')

# нету ключа и значения
# rooms = {'bathroom', 'dining-room', 'hall', 'bedroom00'}
# print (type(rooms))

# создание чистого множества
# set1 = set()
# a = 10
# b = 'str'
# d = True
# add добвление 
# set1.add(a)
# set1.add(b)
# set1.add(d)
# print (set1)

# множества хранит только уникальные данные     повторяющиеся не выводит
# set1 = {1,2,3,4,4,4,4,4,4,5,6,7,8}
# print(set1)

# фишка множества всегда по порядку выводит
# set3 = {5,4,3,9,1,2,}
# print (set3)

# set1 = {'bakai', 'nurdik', 'dair', 'mars', 'beka'}
# set2 = {'azat', 'bakai', 'alex', 'beka', 'mars'}
# set1.update(set2)
# print (set1)

#  разница множевств   выводит те элеметы которых нету
# set3 = set1.difference(set2)

# a = {1,2,3}
# b = {4,5,6}
# в множествах можно использовать update 
# b.update(a)
# print(a)

# a = {1,2,3}
# b = {4,5,6}
# b.remove(1)
# print(b)

# intersection выводит одинаковые данные из множеств

# a = {
    # 'number' : [4,7,8]set1 = {'bakai', 'nurdik', 'dair', 'mars', 'beka'}
# set2 = {'azat', 'bakai', 'alex', 'beka', 'mars'}
# set1.update(set2)
# print (set1)
# menu = {
    # 'lagman': 120, 
    # 'plov': 120, 
    # 'borsh': 100,
    # 'drinks':('Coca-cola','Sprite' , 'Fanta')
# }
# menu['besh_barmak'] = 130
# menu['lagman'] = 135
# menu.pop('borsh')
# print(menu)

# set1 = {'add', 'uppdate', 'difference'}
# set2 = {'min', 'max', 'add', 'uppdate'}
# set3 = set1.intersection(set2)
# print (set3)
# print (set2)



# a = input ('Введите имя: ')
# b = input ('ВВедите пароль: ')
# c = input ('Введите имя: ')
# d = input ('Введите пароль: ')
# e = input ('Введите имя: ')
# f = input ('Введите пароль: ')

# person = {
# 
#    
    # 
# }
# for i in range (3):
    # name = input ('Введите имя: ')
    # password = input ('ВВедите пароль: ')
    # person[name] = password
    # 
# print (person)


# a = {
    # # 'Aidar': 'Swarshik',
    # # 'Beka': 'Aldap sayar',
    # # 'Doni': 'Santehnik',
    # # 'Adi': 'Kabluck',
    # 'Mara': 'Jurnalist'
# }
# items писать без start оно без этого работает
# for key,value in a.items():
    # print(f'Здравстуйте {key}, {value} это прекрассная профессия')

# set1 = set()

# for i in range(10):
#     input('Введите число: ')
#     set1.add(i)
#     # print(i)

# print (set1)

# south_american_countries = {'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela'}
# print(south_american_countries)

# case = []
# items= input('Что вы хоитите взять: ')
# for i in range(5):
#     items
#     case.append(items)
#     print(i)

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_3 = farm_1.intersection(farm_2)
# print (farm_3)

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_3 = farm_2.difference(farm_1)
# print(farm_3)

# for i in range (1,10):
    # for j in range(1,10):
        # print (f'{i} ** {j} = {i ** j} \n')
# 3 цикла по 9 чисел   первый цикл с одного до десяти   второй     и третий     пока j не закончится i не начнтся
# цикл в цикле

# dict1 = {
    # '2134231521' : {
        # 'name': 'Alex',
        # 'surname': 'Kawalski',
        # 'age': '30',
        # 'gender': 'm'
    # }, 
# 
    # '32141251234' : {
        # 'name': 'John',
        # 'surname': 'Ibra',
        # 'age': '20',
        # 'gender': 'm'
    # },
    # '1234123512' : {
        # 'name': 'Kristina',
        # 'surname': 'Kardashyan',
        # 'age': '25',
        # 'gender': 'f'
    # } 
#    
# }
# print(dict1['32141251234']['name'])
# 
# for key,value in dict1['2134231521'].items():
    # print(key,value, end= (','))

# for i in dict1.items():
    # if i == dict1.value == 'f':
        # print('Это девушка')
    # else:
        # print (i)
    # print(i)
# парсинг 