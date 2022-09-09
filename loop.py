#  Циклы for, while
# a = ['Aidar', 'razzak', 'nurs']
# for i in a:
#     if i in a:
#         if i == 'dias'
#         print ('ok')
#     else:
#         print('netu')
# пройтись по списку

# for i in range (1,11):
#     a = i * 5
#     print (a)

# a = []
# b = int(input('chislo:'))
# for i in range(b):
#     a.append(i)
# print(a)
# генерация чисел

# count = 0 
# a = [1,2,3,4,5,5,5,5,5,5,6,7,8,9]
# for i in a:
#     if i == 5:
#         count += 1
#         сокращение count = count + 1
# print (count)

# count = 0
# for i in a:
#     if i == 4:
#         print ('est 4')
#     else:
#         count += 1
#         накапливание чисел 
# print (count)

# range генерация чисел
# for i in range (1,11):
#     b = 5
#     c = b * i
#     print (f'{b} * {i} = {c}')

# for i in range (10, 1, -1 ):
# наоборот
#     print (i)

# найти город по индексу 
# a = ['bishkek0', 'naryn', 'osh', 'tashkent']
# b = int(input('Введите число: 3'))
# for i in range (len(a)):
#     if b == i:
#         print (a[i])
#         если аписать i - 1 и написать 0 цикл перезапустит с обратной стороны
#         () обращение к переменной 

# a = ['bishkek0', 'naryn', 'osh', 'tashkent']
# for i in a :
#     if i == 'tashkent':
#         a.remove(i)
#         a.append ('naryn')
# print (a)
#  замена 

# while пока не выполнит условие не остановится
# i = 0
# while i < 10:
#     print (i)
#     i += 1

# while - пока
# count накапливается 
# count = 1
# a = int (input('Введите число: '))
# while a != 1:
#     print ('Repeat')
 


# a = [1,2,3]*5
# print (a)
# while 3 in a:
#     a.remove(3)
#     print (a)
#     пример остановки while

# for i in range(1,10):
#     if i == 5
#         break 
#     print (i)
# print (i) выведит 5

# lst = ['Alice', 'bob', 'Carl', 'Dave'] 
# x = 'Chris'
# i = 2
# замена карла на криса (это замена [])
# lst[i] = x
# print (lst)

# end = '' столб в строку
# for i in 'hello python':
#     print (i*2, end= '')
#     без end все в стоlб пойдет
#  continue игнор символа 
#  '' элемент который нужно игнорировать, не работает с and
# for i in 'hello world':

#     if i == 'h':
#         continue 
#     elif == 'w':
#         continue 
#     print (i, end='')

# a = 0
# while a < 5:
# a += 1
#  break 
# print (a)

# бесконечность
#     a = int(input('n= '))
#     if len(str(a)) != 3:
#         print('No')
#     else:
#         print('Yes')
#         break

# enumerate # номерует символы 
# b = 'Hello world'
# for i in enumerate(b):
    # print (i)

# guess = input ('enter password': )
# password = 'qwer'
# count = 0
# while guess != password:
#     count += 1 
#     print ('Wrong password')
#     guess = input('enter password: ')
# print (f'Вы потратили {count} попыток ')

# lang1 = 'Rust'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# if lang1 in languages:
#     print ('This languages is in list')


# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == 'php':
#         break
#     print(i)
        
# a = 7
# for i in range (5):
#     i = a * 7
#     print (i)

# languages = ('go', 'java', 'php', 'python', 'javascript', 'ruby')
# for i in enumerate(languages):
#      print (i)

# for i in range (1,11):
#     print (i, end=',')

# for a in range (9,0,-1):
#     print (a, end=',')   

# a = list(range (1,20))
# for i in a:
#     if i > 9:
#         a.reverse()
#     print (i, end= ',')

# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in names [2:14:2]:
#        print(i, end= ',')

# for i in names [1:14:2]:
#         print(i, end= ',')


# a = int(input('Введите чило: '))
# b = a
# for i in b:
#      if i >= 100 :
#          if i >= 100:
#             print ('Это число трехзначное ')
#          else:
#             print ('Это число не трехзначное')
    
#      elif i > 0 :
#             if i > 0 and i /2 :
#                 print ('Это число положительное и четное ')
#             else:
#                 print ('Это число отрицательное и не четное')
#      elif i /31:
#             if i == 0:
#                 print ('Делится без остатка')
#             else:
#                 print ('Делится с остатком')
                
#      else:
#          print('Дальше другие имена')
