import sqlite3

""" 
Работа с базой данных sqlite3
https://proproprogs.ru/modules/podklyuchenie-k-bd-sozdanie-i-udalenie-tablic
"""


def opening_the_list_for_inviting(members_db):
    """Открываем список с username для inviting"""
    # Открываем parsing список для inviting в группу
    with sqlite3.connect(f'{members_db}', timeout=10) as sqlite_connection_members:
        cursor_members = sqlite_connection_members.cursor()
        # Считываем таблицу members в файле setting/members_group.db
        cursor_members.execute("""SELECT * from members""")
        return cursor_members


def opening_a_database_with_accounts():
    """Открытие базы данных для работы с аккаунтами"""
    # Открываем файл config.db, где хранятся аккаунты телеграмм
    with sqlite3.connect('accounts/config.db', timeout=10) as sqlite_connection:
        cursor = sqlite_connection.cursor()
        # Считываем таблицу
        cursor.execute("""SELECT * from config""")
        return cursor


def opening_the_database(folder, file):
    """Открываем базу sqlite3"""
    with sqlite3.connect(f'{folder}/{file}', timeout=10) as sqlite_connection:
        cursor = sqlite_connection.cursor()
        return cursor, sqlite_connection

