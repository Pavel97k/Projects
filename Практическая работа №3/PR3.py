import os, hashlib, pyodbc, smtplib
import smtplib as smtp

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version

server = 'MSI-PAVEL\SQLSERVERPAVEL' 
database = 'Fettuccine_with_porcini_mushrooms_Datebase'

connectionString = (f'Driver=SQL Server; Server={server}; Database={database}; Trusted_Connection=yes;')
connection = pyodbc.connect(connectionString, autocommit=True)
dbCursor = connection.cursor()


def sendEMail(text):
    server = smtplib.SMTP("smtp.yandex.com", 587)
    server.ehlo()
    server.starttls()
    server.login("pavekryuchckov97@yandex.ru", "panda85wood-CRAK")
    message = "\r\n".join([
        "From: pavekryuchckov97@yandex.ru",
        "To: isip_p.a.kryuchkov@mpt.ru",
        "Subject: Тема",
        "",
        str(text)
    ]).encode('utf-8').strip()
    server.sendmail("pavekryuchckov97@yandex.ru", "isip_p.a.kryuchkov@mpt.ru", message)
    server.quit()

def _Authorization_Registration():
    print('''Добро пожаловать! Выберите пункт меню:
    1. Вход
    2. Регистрация
    3. Выход''')
    user_input = input()
    if user_input == '1':
        _Authorization(input("Введите логин: "), input("Введите пароль: "))
        sendEMail("Авторизация прошла успешно")
    if user_input == '2':
        _Register(input("Введите имя: "), input("Введите фамилию: "), input("Введите отчество: "), input("Введите логин: "), input('Введите пароль: '))
        sendEMail("Регистрация прошла успешно")
    if user_input == '3':
        print('Завершение работы')
        dbCursor.close()
        connection.close()
        exit()


def _Authorization(Login, Password):
    global ID_Users
    global Name_Post_ID
    dbCursor.execute(f"select [ID_Users], [Name_Post_ID] from [dbo].[Users] where [Login_Users] = '{Login}' and [Password_Users] = '{Password}' ")
    row = dbCursor.fetchall()
    ID_Users = row[0][0]
    Name_Post_ID = row[0][1]
    if(Name_Post_ID == 1):
        print("Вы вошли как Пользователь")
        getUserWindow()
    else:
        print("Вы вошли как Администратор")

def _Register(First_Name, Second_Name, Middle_Name, Login, Password):
    dbCursor.execute(f"insert into [dbo].[Users] ([Firt_Name_Users], [Second_Name_Users], [Middle_Name_Users], [Balance_Money], [Login_Users], [Password_Users], [Name_Post_ID]) values('{First_Name}', '{Second_Name}', '{Middle_Name}', '1000', '{Login}', '{Password}', '1')")
    dbCursor.commit()

def getUserWindow():
    global orderID
    global countDishes

    while (True):
        if(int(input("Выберите действие\n1) Сделать заказ\n2) Посмотреть историю заказов\n")) == 1):
            print("Введите кол-во блюд: ")
            countDishes = int(input())
            if(countDishes < 0): 
                print("Доп. продукты не будут добавлены!") 
                return
            for i in countDishes:
                _InsertOrder(input("Выберите продукт \n 1)Курица отварная \n 2)Курица жаренная \n 3)Креветки \n 4)Сыр Пекорино романо \n 5)Сыр Чеддер \n 6)Растительное масло \n 7)Петрушка \n 8)Лук Порей \n 9)Лук Батун \n"), input("Введите кол-во продукта: "))
                if (i == countDishes):        
                    if (int(input() == 2)):
                        print("2")
        elif (input() == 3):
            exit()

    
        

def _Login():
    while(True):
        print('''Добро пожаловать! Выберите пункт меню:
        1. Вход
        2. Регистрация
        3. Выход''')

        user_input = input()
        if user_input == '1':  # Условия можно заменить на: user_input.lower() == 'вход'
            print('Введите логин:')
            login = input()

            print('Введите пароль:')
            password = input()

            result = get_user(login, hashlib.sha256(password.encode()).hexdigest())

            if result:
                print('Вы вошли в систему')
                collection_of_dishes()
            else:
                print('Неверный логин или пароль')

        elif user_input == '2':
            print('Введите логин:')
            login = input()

            print('Введите пароль:')
            password = input()

            print('Повторите пароль:')
            password_repeat = input()

            if password != password_repeat:
                print('Пароли не совпадают!')

            result = add_user(login, hashlib.sha256(
                password.encode()).hexdigest())  # Вызываем функцию добавления пользователя. И хешируем пароль(безопасность)

            if not result:
                print('Пользователь с таким логином уже существует')
            else:
                print('Регистрация прошла успешно!')

        elif user_input == '3':
            print('Завершение работы')
            exit()


def _InsertOrder(Name_Product_Order_ID, Count_Product_Order):
    dbCursor.execute(f"insert into [dbo].[Order] ([Name_Product_Order_ID], [Count_Product_Order]) values ( {Name_Product_Order_ID}, {Count_Product_Order})")
    dbCursor.commit()
    print("Вы успешно добавили заказ!")

def _HistoryOrder(): ##########################
    dbCursor.execute(f"select * from [dbo].[Order] where ")
    dbCursor.commit()
    print("Вы успешно добавили заказ!")

def _InsertHistoryOrder(Name_Product_Order_ID, Count_Product_Order):
    dbCursor.execute(f"insert into [dbo].[History_of_Orders] ([Name_Loyal_Cards_ID], [Second_Name_Users_ID]) values ( {Name_Product_Order_ID}, {Count_Product_Order})")
    dbCursor.commit()
    print("Вы успешно добавили заказ!")

def collection_of_dishes():
    print("Состав блюда: ", dish)   
    print("\nОсновной состав блюда:")   
    while(True):
       i = 0
       i1 = 0
       v = 0
       for lenght in IngredientsFirts:
            print("№",i, IngredientsFirts[i])
            i += 1
       print("\nСоберите блюдо:")
       for lenght in IngredientsSeconds:
            print("№",i1, IngredientsSeconds[i1])
            i1 += 1
       print("Ваше блюдо:", dish)
       number = int(input())
       if(number > len(IngredientsSeconds) - 1): 
           print("Хотите добавить ещё блюдо?\n 1. Да \n 2. Нет")
           v = int(input())
           match v:
               case 1:
                   add_dish(dish)
                   dish.clear()
                   continue
               case 2:             
                   break
       if(v !=  1 and number <= len(IngredientsSeconds) - 1): 
           dish.append(IngredientsSeconds[number])
       
       os.system('CLS') 

 

def init_file():  # Инициализация файла, если этого не сделать програма вылетит м ошибкой, что файла нет
    if not os.path.exists('dish_count.txt'):
        with open('dish_count.txt', 'w'):
            pass

def init_file_users():  # Инициализация файла, если этого не сделать програма вылетит м ошибкой, что файла нет
    """Создает файл пользователей"""
    if not os.path.exists('users.txt'):
        with open('users.txt', 'w'):
            pass


def add_dish(string: str):
    """Добавляет пользователя в файл"""
    with open('dish_count.txt', 'r') as f:
        dish_p = f.read().splitlines()  # Считываем всех пользователей из файла

    for DISH_List in dish_p:
        DISH_List.split(':')

    with open('dish_count.txt', 'a') as f:
        f.write(f'{string}\n')  # Добавляем нового пользователя
    return True

def add_user(login: str, password: str) -> bool:
    """Добавляет пользователя в файл"""
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()  # Считываем всех пользователей из файла

    for user in users:
        args = user.split(':')
        if login == args[0]:  # Если логин уже есть, пароль не проверяем, шанс взлома увеличится(кто-то мб узнает пароль)
            return False  # Тут можно написать что угодно, будь то HTML статус(409 - conflict), либо просто фразу ошибки

    with open('users.txt', 'a') as f:
        f.write(f'{login}:{password}\n')  # Добавляем нового пользователя
    return True


def get_user(login: str, password: str) -> bool:
    """Проверяет логин и пароль пользователя"""
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()  # Считываем всех пользователей из файла

    for user in users:
        args = user.split(':')
        if login == args[0] and password == args[1]:  # Если пользователь с таким логином и паролем существует
            return True
    return False


def main_loop(login: str):
    """Главный цикл программы"""
    print(f'Привет, {login}!')  # Тут основная часть программы

print("Привет дорогой друг - это мини бизнес по сбору Феттучини с белыми грибами")
input("Вы хотите начать?\n")
os.system('CLS')
_Authorization_Registration()