# def print_text():
    # print('Hello')
# 
# print_text()

# def sum1():
    # a = 5
    # b = 34
    # return a + b
# print(sum1())

# def sum2 (a,b):
    # return a*b
# print(sum2(5,99))
# print(sum2(16,99))
# print(sum2(60,365))


# можно с разными названиями 
# def my_len(a):
    # s = 0
    # for i in a:
        # s += 1    
    # print(s)
# a = [1,2,3,4,5,6,7,8,9]
# b = ['a', 'b', 'c', 'd','e']
# my_len(a)
# my_len(b)

# def my_sum(a,b,d):
    # return a +b +d
# print(my_sum(20,30,50))


# def umnozh(a, b):
    # return a*b
# print(umnozh(60,6.21))

# def naoborot():
    # a = ['age', 'name', 1, 19]
    # d = []
    # print(a)
    # mid = len(a) //2
    # b = a[:mid]
    # c = a[mid:]
    # b.reverse()
    # c.reverse()
    # d.extend(b)
    # d.extend(c)
    # print(d)
# 
# naoborot()


# a = []
# for i in range(11):
    # print(i)
# print(a)


# def fibonacci(a):
#     if a in (1, 2):
#         return 1
#     return fibonacci(a - 1) + fibonacci(a - 2) 
# print(fibonacci())


# a = int(input('Введите число: '))
# b = int(input('Введите число: '))

# def sum1(a,b):
#     return a+b
# print(sum1(a,b))

# def minus1(a, b):
#     return a-b
# print(minus1(a,b))

# def chisla(a,b):
#     return a,b
# print(a,b)

# def miniimath():
#     sum1
#     minus1
#     chisla

# miniimath

# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
# z = input(f'Введиет имя файла: ')
# def sum1(a,b):
#     return a+b
# print(sum1(a,b))

# def minus1(a, b):
#     return a-b
# print(minus1(a,b))

# def chisla(a,b):
#     return a,b
# print(a,b)

# def miniimath():
#     sum1
#     minus1
#     chisla


# b = miniimath
# print(b)

# from string import ascii_letters
# from random import choice
# from time import sleep
# 
# count = 0
# password = ''
# password1 = 'QWE'
# while len(password) != 3:
    # l = choice(ascii_letters)
    # if password != password1:
        # password = choice(ascii_letters) 
        # password += l
        # count += 1
        # print(password,count)
        # sleep(0.001)
# print(count)
# 
# from string import ascii_letters
# from random import choice
# from time import sleep
# 
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



# from random import randint, choice
# numbers = '145790'
# count = 0
# for i in range(numbers):
    # x = randint(i,10)
    # print(x)
# while True:
    # nomer = ''
    # while len(nomer) != 10:
        # l = choice(numbers)
        # nomer =+ l
        # if nomer != len(10):
            # count +=1 
        # else:
            # print(nomer)
            # print(count)