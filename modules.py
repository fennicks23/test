# import random можно и так  
# from random import choise as ch
# from random import random,randrange, shufle 
# randrange приимает старт стоп степ
# a = random.random()
# sample радомные числа по заданному числу 
# print(a) рандомное число до 1
# b = random.randint(1,100)
# print(b) 
# randit поле рандома старт стоп есть 
# c = [234,24,25,62,11,54]
# print(random.choice(c))
# достает из списка рандомное число  имена 
# print (ch(c))
# print(randint(1,100))
# print(sample(c,3))
# random.shuffle(c)
# print(c)

# from time import sleep
# c = [234,24,25,62,11,54]
# for i in c:
    # print(i)
    # sleep(0.1)
    # sleep указывает тайминг 

# from datetime import date, datetime,time
# now = datetime.now()
# print(now)
# datetime выводит время сейчас
# timeobj= time(8,1,00)
# print(timeobj)
# timeobj2= time(8,1,45)
# print(timeobj2)

# start= datetime.now()
# for i in range (1,100):
    # print(i)
# end = datetime.now()
# print(end-start)

# print(datetime.today().strftime('%d-%m-%y  %H-%M-%S'))
# тире и двоиточия для красоты

# from random import randint
# a = [randint(0,10) for i in range (20)]
# print(a)
# print(len(a))

# import calendar
# c = calendar.TextCalendar()
# print(c.formatyear(2023))

# import os 
# os.mkdir('hello')
# os добавить папку 
# os.rmdir('hello')
# rm - rf удаление папки
# rmdir удаление папки
# os.system('clear')
# можно терминаловские команды через систем
# os.system('touch run.py')

# import math
# print(math.e)
# print(math.pi)
# from math import pi, factorial
# a = pi
# print(factorial(668))

# import math
# print(math.cos(-10))


# from my_modules import team, team1,team2,team3
# from random import random, choice as ch, sample
# b = []
# b.append(sample(lst1,5))
# while len(b) != 4 :
    # b.append(ch(room_301))
# print(b)
# на уровне что бы цикл не отработал
# from string import ascii_letters
# ascii_letters англ алфавит

# from string import ascii_letters
# from random import choice
# from time import sleep
# 
# count = 0
# password = ''
# password1 = 'QWE'
# while len(password) != 4:
    # l = choice(ascii_letters)
    # if password != password1:
        # password = choice(ascii_letters) 
        # password += l
        # count += 1
        # print(password,count)
        # sleep(0.001)
# print(count)
# шифт таб удаляет лишие пробелы
  
# from string import ascii_letters
# from random import choice
# from time import sleep
# password1 = 'QWE'
# count = 0
# letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# while True:
    # password = ''
    # while len(password) != 3:
        # l = choice(letters)
        # password += l
    # if password != password1:
        # count += 1
# 
    # else:
        # print(password)
        # print(count)
        # break


