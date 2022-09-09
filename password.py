login = input('Введите ваш логин: ')
password = input('Введите пароль: ')
login1 = 'fennicks23'
password1 = 'pidrgandon'
if login != login1 and password != password1:
    print(f'Ваш логин {login} или пароль {password} неправельный \n    Попробуйте снова ')
elif login == login1 and password == password1:
    print ('Добро пожаловать')