# -*- coding: utf-8 -*-
import getpass
import os

from rich import print
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, PhoneNumberBannedError, UserDeactivatedBanError
from telethon.tl.functions.users import GetFullUserRequest

from system.Error.TelegramErrors import telegram_user_deactivated_ban_error, telegram_phone_number_banned_error
from system.auxiliary_functions.auxiliary_functions import clearing_console_showing_banner
from system.auxiliary_functions.global_variables import console
from system.sqlite_working_tools.sqlite_working_tools import opening_a_database_with_accounts


def open_database_accounts():
    """Выводим список аккаунтов"""
    cursor = opening_a_database_with_accounts()
    # Количество аккаунтов на данный момент в работе
    records = cursor.fetchall()
    print(f"[bold red]Всего accounts: {len(records)}")
    return


def we_get_username_user_id_access_hash(rows):
    """Получаем username, user_id, access_hash"""
    user = {'username': rows[0], 'id': rows[1], 'access_hash': rows[2]}
    username = user["username"]
    user_id = user["id"]
    access_hash = user["access_hash"]
    return username, user_id, access_hash, user


def deleting_an_invalid_session(phone):
    """Удаляем не валидную сессию, если аккаунт banned"""
    telegram_user_deactivated_ban_error(phone)
    try:
        os.remove(f'accounts/{phone}.session')
    except FileNotFoundError:
        print(f"[green]Файл {phone}.session был ранее удален")


def print_name_phone_account_connect(client, phone):
    """Выводим командой print: имя, фамилию, номер телефона аккаунта"""
    # Делаем запрос на получение имени аккаунта
    name_client = "me"
    # Показываем имя аккаунта с которым будем взаимодействовать
    first_name, last_name = account_name(client, name_client)
    # Выводим результат полученного имени и номера телефона
    print(f"[bold red][!] Account connect {first_name} {last_name} {phone}")


def checking_accounts_for_validity():
    """Проверка аккаунтов на валидность, если аккаунт не валидный, то удаляем сессию"""
    clearing_console_showing_banner()
    print(f"[bold red][!] Проверяю аккаунты на валидность")
    # Открываем базу данных для работы с аккаунтами accounts/config.db
    cursor = opening_a_database_with_accounts()
    # Количество аккаунтов на данный момент в работе
    records = cursor.fetchall()
    for row in records:
        # Получаем со списка phone, api_id, api_hash
        phone, api_id, api_hash = get_from_the_list_phone_api_id_api_hash(row)
        client = TelegramClient(f"accounts/{phone}", api_id, api_hash)
        try:
            # Подключаемся к аккаунту
            client.connect()
            # Если аккаунт не авторизирован, то удаляем сессию
            if not client.is_user_authorized():
                # Если не валидная сессия, удаляем со списка accounts/config.db и файл session
                deleting_an_invalid_session(phone)
            # Отключаемся от аккаунта
            client.disconnect()
        except (PhoneNumberBannedError, UserDeactivatedBanError):
            # Удаляем номер телефона с базы данных
            telegram_phone_number_banned_error(client, phone)
            continue


def telegram_connect(phone, api_id, api_hash):
    """Account telegram connect, с проверкой на валидность, если ранее не было соединения, то запрашиваем код"""
    client = TelegramClient(f"accounts/{phone}", api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        try:
            # Если ранее аккаунт не подсоединялся, то просим ввести код подтверждения
            client.sign_in(phone, code=console.input("[bold red][+] Введите код: "))
        except SessionPasswordNeededError:
            """
            https://telethonn.readthedocs.io/en/latest/extra/basic/creating-a-client.html#two-factor-authorization-2fa
            """
            # Если аккаунт имеет password, то просим пользователя ввести пароль
            client.sign_in(password=getpass.getpass())
    print_name_phone_account_connect(client, phone)
    return client


# def telegram_connect_new_accounts(phone, api_id, api_hash):
#     """Account telegram connect, с проверкой на валидность, если ранее не было соединения, то запрашиваем код"""
#     client = TelegramClient(f"accounts/{phone}", api_id, api_hash)
#     client.connect()
#     if not client.is_user_authorized():
#         client.send_code_request(phone)
#         try:
#             # Если ранее аккаунт не подсоединялся, то просим ввести код подтверждения
#             client.sign_in(phone, code=console.input("[bold red][+] Введите код: "))
#         except SessionPasswordNeededError:
#             """
#             https://telethonn.readthedocs.io/en/latest/extra/basic/creating-a-client.html#two-factor-authorization-2fa
#             """
#             # Если аккаунт имеет password, то просим пользователя ввести пароль
#             client.sign_in(password=getpass.getpass())
#     return client


def account_name(client, name_account):
    """Показываем имя аккаунта с которого будем взаимодействовать"""
    full = client(GetFullUserRequest(name_account))
    for user in full.users:
        first_name = ""
        if user.first_name:
            first_name = user.first_name
        last_name = ""
        if user.last_name:
            last_name = user.last_name
        return first_name, last_name


def get_from_the_list_phone_api_id_api_hash(row):
    """Получаем со списка phone, api_id, api_hash"""
    users = {'id': int(row[0]), 'hash': row[1], 'phone': row[2]}
    # Вытягиваем данные из кортежа, для подстановки в функцию
    phone = users['phone']
    api_id = users['id']
    api_hash = users['hash']
    return phone, api_id, api_hash
