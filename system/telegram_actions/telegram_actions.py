# -*- coding: utf-8 -*-
import os
import getpass
from telethon.errors import SessionPasswordNeededError
from rich import print
from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest

from system.Error.TelegramErrors import telegram_user_deactivated_ban_error
from system.auxiliary_functions.global_variables import console


def deleting_an_invalid_session(phone):
    """Удаляем не валидную сессию, если аккаунт banned"""
    telegram_user_deactivated_ban_error(phone)
    try:
        os.remove(f'accounts/{phone}.session')
    except FileNotFoundError:
        print(f"[green]Файл {phone}.session был ранее удален")


name_client = "me"


def telegram_connect(phone, api_id, api_hash):
    """Account telegram connect, с проверкой на валидность, если ранее не было соединения, то запрашиваем код"""
    client = TelegramClient(f"accounts/{phone}", api_id, api_hash)
    client.connect()
    first_name, last_name = account_name(client, name_client)
    print(f"[bold red][!] Account connect {first_name} {last_name} {phone}")
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
    return client


def telegram_connect_new_accounts(phone, api_id, api_hash):
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
    return client


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
