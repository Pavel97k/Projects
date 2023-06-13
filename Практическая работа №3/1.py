import os, hashlib, pyodbc

server = 'MSI-PAVEL\SQLSERVERPAVEL' 
database = 'Fettuccine_with_porcini_mushrooms_Datebase'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.

cnxn = pyodbc.connect(f'Driver=SQL Server; Server={server}; Database={database}; Trusted_Connection=yes;')
cursor = cnxn.cursor()


def _Authorization(Login, Password):
    global Name_Post_ID
    cursor.execute(f"select [ID_Users], [Name_Post_ID] from [dbo].[Users] where [Login_Users] = \'{Login}\' and [Password_Users] = \'{Password}\' ")
    row = cursor.fetchone()
    # Name_Post_ID = row[0]
    print(row)

_Authorization(input("  Ввдите логин\n"), input("  Введите пароль\n"))