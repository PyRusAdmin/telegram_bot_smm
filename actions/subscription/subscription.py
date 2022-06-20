# -*- coding: utf-8 -*-
import os
import random
import sqlite3
import time

from rich import print
from rich.progress import track
from telethon import TelegramClient
from telethon.errors import ChannelPrivateError
from telethon.errors import ChannelsTooMuchError
from telethon.errors import FloodWaitError
from telethon.errors import PeerFloodError
from telethon.errors import PhoneNumberBannedError
from telethon.errors import UserDeactivatedBanError
from telethon.tl.functions.channels import JoinChannelRequest

from system.Error.TelegramErrors import telegram_phone_number_banned_error
from system.auxiliary_functions.auxiliary_functions import clearing_console_showing_banner
from system.auxiliary_functions.global_variables import config
from system.auxiliary_functions.global_variables import console
# from system.auxiliary_functions.global_variables import file_path_gr
from system.auxiliary_functions.global_variables import toaster
from system.sqlite_working_tools.sqlite_working_tools import opening_a_database_with_accounts
from system.sqlite_working_tools.sqlite_working_tools import opening_the_database
# from system.telegram_actions.telegram_actions import connecting_to_the_telegram_client
# from system.telegram_actions.telegram_actions import telegram_connect
from system.telegram_actions.telegram_actions import get_from_the_list_phone_api_id_api_hash

config.read('setting/time_subscription.ini')

# Время между подпиской
time_subscription1: str = config['cred']['time_subscription1']
time_subscription2: str = config['cred']['time_subscription2']

folder: str = "setting"
file: str = "members_group.db"


def writing_group_links_to_file():
    """Запись ссылок групп / каналов в файл setting/members_group.db"""
    # Чистим консоль, выводим банер
    clearing_console_showing_banner()
    print("[bold red][+] Для остановки введите слово [bold green]stop")
    writing_group = ''
    # Запускаем программу в бесконечном цикле, пока не будет введено слово для остановки
    while writing_group != "stop":
        writing_group: str = console.input("[bold red][+] Введите ссылку на группу, для записи в файл, или слово stop: ")
        if writing_group != "stop":
            """Записываем ссылку на группу для parsing в файл setting/members_group.db"""
            # Открываем файл setting/members_group.db и проверяем на наличие
            cursor, sqlite_connection = opening_the_database(folder, file)
            """
            IF NOT EXISTS поможет при попытке повторного подключения к базе данных.
            Запрос проверит, существует ли таблица. Если да — проверит, ничего ли не поменялось.
            """
            cursor.execute("CREATE TABLE IF NOT EXISTS writing_group_links(writing_group_links)")
            cursor.execute("INSERT INTO writing_group_links VALUES (?)", (writing_group,))
            sqlite_connection.commit()
            # Закрываем файл setting/members_group.db
            cursor.close()
        else:
            print("[bold red][!] Данные записали!")
            toaster.show_toast("Telegram_BOT_SMM", "Данные записаны!", icon_path="system/ico/custom.ico", duration=5)


def cleaning_the_list_with_groups_for_subscription(writing_group):
    """Создание нового списка для подписки на группы / каналы"""
    # Удаление списка с группами
    sqlite_connection = sqlite3.connect(f'{folder}/{file}')
    cursor = sqlite_connection.cursor()
    # Удаляем таблицу writing_group_links, функция execute отвечает за SQL-запрос
    cursor.execute('DELETE FROM writing_group_links;')
    # Создаем таблицу writing_group_links, функция execute отвечает за SQL-запрос
    """
    IF NOT EXISTS поможет при попытке повторного подключения к базе данных.
    Запрос проверит, существует ли таблица. Если да — проверит, ничего ли не поменялось.
    """
    cursor.execute("CREATE TABLE IF NOT EXISTS writing_group_links(writing_group_links)")
    # Записываем ссылку на группу, для дальнейшей подписки
    cursor.execute("INSERT INTO writing_group_links VALUES (?)", (writing_group,))
    sqlite_connection.commit()
    cursor.close()


def deleting_groups_and_channels(folder, file, groups_wr):
    """Удаляем не валидные группы или каналы"""
    with sqlite3.connect(f'{folder}/{file}', timeout=10) as sqlite_connection_members:
        cursor_members = sqlite_connection_members.cursor()
        # Считываем таблицу
        cursor_members.execute("""SELECT * from writing_group_links""")
        # Удаляем строку
        cursor_members.execute("""DELETE from writing_group_links where writing_group_links = ?""", (groups_wr,))
        sqlite_connection_members.commit()
        cursor_members.close()
        print("[green][+] Пождите 1-2 Секунд...")
        time.sleep(random.randrange(1, 2))


def subscription_all():
    """Подписываемся на каналы и группы, работаем по базе данных"""
    clearing_console_showing_banner()
    # Открываем базу данных для работы с аккаунтами accounts/config.db
    cursor = opening_a_database_with_accounts()
    # Количество аккаунтов на данный момент в работе
    records = cursor.fetchall()
    print(f"[bold red]Всего accounts: {len(records)}")
    for row in track(records, description='[bold red]Прогресс выполнения работы\n'):
        # Получаем со списка phone, api_id, api_hash
        phone, api_id, api_hash = get_from_the_list_phone_api_id_api_hash(row)
        print(f"\n[bold red]{phone} [!] Account connect")
        client = TelegramClient(f"accounts/{phone}", api_id, api_hash)
        
        try: 
            client.connect()
            print(f"[bold red][!] Account connect {phone}")

            # Открываем базу данных
            cursor, sqlite_connection = opening_the_database(folder, file)
            cursor.execute("""SELECT * from writing_group_links""")
            records = cursor.fetchall()
            print(f"[bold red]Всего групп: {len(records)}")

            # Поочередно выводим записанные группы
            for groups in records:
                group = {'writing_group_links': groups[0]}
                # Вытягиваем данные из кортежа, для подстановки
                groups_wr = group['writing_group_links']
            
                """Показываем уже подписанные группы / каналы"""
                for dialog in client.iter_dialogs():
                    print(f"[bold green]{dialog.name}", 'has ID', f"[bold green]{dialog.id}")
                try:
                    channel_and_group_subscription_function(client, groups_wr)

                except ChannelsTooMuchError:
                    """Если аккаунт подписан на множество групп и каналов, то отписываемся от них"""
                    for dialog in client.iter_dialogs():
                        print(f"[green]{dialog.name}, {dialog.id}")
                        try:
                            client.delete_dialog(dialog)
                        except ChannelPrivateError:
                            continue
                    print('[green][+] Список почистили, и в файл записали.')
                except ChannelPrivateError:
                    """Указанный канал / группа является приватным, и у вас нет разрешения на доступ к нему,
                    или запрет на действия. """
                    print("[bold red][!] Указанный канал является приватным, или вам запретили подписываться.")
                    deleting_groups_and_channels(folder, file, groups_wr)
                except ValueError:
                    """Не верное имя канала / группы"""
                    print("[bold red][!] Не верное имя канала / группы.")
                    deleting_groups_and_channels(folder, file, groups_wr)
                except TypeError:
                    """Ссылка не является группой или каналом"""
                    print(f"[bold red][!] Ссылка {groups_wr} не является группой или каналом")
                    deleting_groups_and_channels(folder, file, groups_wr)
                except (PeerFloodError, FloodWaitError):
                    """Предупреждение о Flood"""
                    print("[red][!] Предупреждение о Flood от telegram.")
            
            # Закрываем сессию при успешной подписке
            client.disconnect()
        
        except (PhoneNumberBannedError, UserDeactivatedBanError):
            """Если номер телефона был banned, то удаляем сессию и номер с базы данных"""
            # Удаляем номер телефона с базы данных
            telegram_phone_number_banned_error(client, phone)
        
    print('[bold green][+] На группы подписались!')
    toaster.show_toast("Telegram_BOT_SMM", "На группы подписались!", icon_path="system/ico/custom.ico", duration=5)


# def chats_id_def_one(client):
#     """Показываем ID чатов, только id, записываем результат в файл"""
#     with open(f"{file_path_gr}", "r") as chat_add:
#         for line in chat_add:
#             for dialog in client.iter_dialogs():
#                 print(f"[bold green]{dialog.name}", 'has ID', f"[bold green]{dialog.id}")
#             client(JoinChannelRequest(line))
#             print(f"[bold red]Присоединился к группе или чату {line}")
#             print(f"[bold green][+] Подождите {time_subscription1}-{time_subscription2} Секунд...")
#             time.sleep(random.randrange(int(time_subscription1), int(time_subscription2)))
#     client.disconnect()
#     print('[bold green][+] На группы подписались.')
#     toaster.show_toast("Telegram_BOT_SMM", "На группы подписались!", icon_path="system/ico/custom.ico", duration=5)


def channel_and_group_subscription_function(client, target_group):
    """Подписываемся на каналы / группы с проверкой ошибок введенных данных пользователем"""
    client(JoinChannelRequest(target_group))
    print(f"[bold red][+] Присоединился к группе или чату {target_group}")
    print(f"[bold green][+] Подождите {time_subscription1}-{time_subscription2} Секунд...")
    time.sleep(random.randrange(int(time_subscription1), int(time_subscription2)))


# def subscription_from_groups_and_channels():
#     """Отписка от групп и каналов с одного аккаунта"""
#     # Открываем базу данных для работы с аккаунтами accounts/config.db
#     cursor = opening_a_database_with_accounts()
#     # Количество аккаунтов на данный момент в работе
#     records = cursor.fetchall()
#     print(f"[bold red]Всего accounts: {len(records)}")
#     phone, api_id, api_hash = connecting_to_the_telegram_client(records)
#     client = telegram_connect(phone, api_id, api_hash)
#     chats_id_def_one(client)


if __name__ == "__main__":
    subscription_all()
