# -*- coding: utf-8 -*-
import os
import random
import sqlite3
import time

from rich import print
from rich.console import Console

from system.auxiliary_functions.auxiliary_functions import write_add_members
from system.auxiliary_functions.global_variables import config

console = Console()


"""Действия с username"""


def removing_a_participant_from_the_list(user):
    """Удаляем user списка members.db"""
    # Файл с настройками
    config.read('setting/time_inviting.ini')

    # Время между inviting
    time_inviting1 = config['cred']['time_inviting1']
    time_inviting2 = config['cred']['time_inviting2']

    time_inviting_1 = int(time_inviting1)
    time_inviting_2 = int(time_inviting2)

    with sqlite3.connect('setting/members_group.db', timeout=10) as sqlite_connection_members:
        cursor_members = sqlite_connection_members.cursor()
        # Считываем таблицу members в файле setting/members_group.db
        cursor_members.execute("""SELECT * from members""")
        # Удаляем отработанный user
        cursor_members.execute("""DELETE from members where id = ?""", (user['id'],))
        sqlite_connection_members.commit()
        cursor_members.close()
        print(f"[green][+] Пождите {time_inviting_1}-{time_inviting_2} Секунд...")
        time.sleep(random.randrange(time_inviting_1, time_inviting_2))


def client_disconnect_telegram(client):
    """Отключаем клиент, спим 20-25 секунд"""
    client.disconnect()
    # Файл с настройками

    config.read('setting/time_changing_accounts.ini')

    # Время между сменой аккаунтов
    time_changing_accounts1 = config['cred']['time_changing_accounts1']
    time_changing_accounts2 = config['cred']['time_changing_accounts2']

    time_changing_accounts_1 = int(time_changing_accounts1)
    time_changing_accounts_2 = int(time_changing_accounts2)
    print(f"[green][+] Пождите {time_changing_accounts_1}-{time_changing_accounts_2} Секунд...")
    time.sleep(random.randrange(time_changing_accounts_1, time_changing_accounts_2))


def telegram_flood_error(client):
    """Предупреждение о Flood от telegram"""
    print("[red][!] Предупреждение о Flood от telegram.")
    client_disconnect_telegram(client)


def telegram_channel_private_error(client):
    """Чат является приватным, или закрыт доступ добавления участников"""
    print("[red][!] Чат является приватным, или закрыт доступ добавления участников.")
    client_disconnect_telegram(client)


def telegram_chat_write_forbidden_error(client):
    """Вы не подписаны на группу / канал, открываем функцию подписки и подписываемся, запускаем inviting"""
    print("[red][!] Вы не подписаны на группу нет возможности добавить user.")
    print("[red][!] Для дальнейшего избежания ошибки, запускаю подписку на группы, это займет некоторое время")
    client_disconnect_telegram(client)
    # """Запускаем отписку"""
    # unsubscribe_from_groups_and_channels()
    # """Запускаем подписку"""
    # subscription_from_groups_and_channels()


def telegram_user_id_invalid_error(client):
    """Вы неправильно закрыли программу, сформируйте список members.db"""
    print("[bold red][!] Вы не правильно закрыли программу, сформируйте список  members.db")
    client_disconnect_telegram(client)


def telegram_user_banned_in_channel_error(client):
    """Вам запрещено отправлять сообщения в супергруппу"""
    print("[bold red][!] Вам запрещено отправлять сообщения в супергруппу.")
    client_disconnect_telegram(client)


def telegram_bot_groups_blocked_error(user):
    """Вы не можете добавить бота в группу."""
    user_info_add = "  Вы не можете добавить бота в группу."
    print(f"[bold red][!] {user_info_add}")
    write_add_members(f"{user} {user_info_add}")
    removing_a_participant_from_the_list(user)


def telegram_user_not_mutual_contact_error(user):
    """User не является взаимным контактом."""
    user_info_add = "  User не является взаимным контактом."
    print(f"[bold red][!] {user_info_add}")
    write_add_members(f"{user} {user_info_add}")
    removing_a_participant_from_the_list(user)


def telegram_chat_admin_required_error(user):
    """Требуются права администратора."""
    user_info_add = "  Требуются права администратора."
    print(f"[bold red][!] {user_info_add}")
    write_add_members(f"{user} {user_info_add}")
    removing_a_participant_from_the_list(user)


def telegram_user_kicked_error(user):
    """Пользователь был удален ранее из супергруппы."""
    user_info_add = "  Пользователь был удален ранее из супергруппы."
    print(f"[bold red][!] {user_info_add}")
    write_add_members(f"{user} {user_info_add}")
    removing_a_participant_from_the_list(user)


def telegram_exceeded_the_limit_of_super_groups(user):
    """Превышен лимит у user каналов / супергрупп."""
    user_info_add = "  Превышен лимит у user каналов / супергрупп."
    print(f"[bold red][!] {user_info_add}")
    write_add_members(f"{user} {user_info_add}")
    removing_a_participant_from_the_list(user)


def telegram_invalid_user_name(user):
    """Не корректное имя user"""
    user_info_add = "  Не корректное имя user"
    print(f"[bold red][!] {user_info_add}")
    write_add_members(f"{user} {user_info_add}")
    removing_a_participant_from_the_list(user)


"""Действия с аккаунтами"""


def delete_phone_ac(phone):
    """Удаляем не валидный аккаунт"""
    with sqlite3.connect('accounts/config.db', timeout=10) as sqlite_connection:
        cursor = sqlite_connection.cursor()
        cursor.execute("""SELECT * from config""")
        cursor.execute("""DELETE from config where phone = ?""", (phone,))
        sqlite_connection.commit()
        cursor.close()


def telegram_phone_number_banned_error(client, phone):
    """Аккаунт banned, удаляем banned аккаунт"""
    print(f"[bold red][!] Аккаунт Banned {phone}")
    # Разрываем соединение с аккаунтом, для удаления session файла
    client.disconnect()
    delete_phone_ac(phone)
    try:
        # Находим и удаляем сессию
        os.remove(f"accounts/{phone}.session")
    except FileNotFoundError:
        # Если номер не найден, то выводим сообщение
        print(f"[green]Файл {phone}.session был ранее удален")


def telegram_user_deactivated_ban_error(phone):
    """Не валидная сессия"""
    print(f"[bold red][!] Не валидная сессия {phone}")
    # write_add_account_actions(phone)
    delete_phone_ac(phone)
