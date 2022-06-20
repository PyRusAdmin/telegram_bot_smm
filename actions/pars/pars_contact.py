# import os
import random
import sqlite3
import sys
import time

import telethon
from rich import print
from telethon import functions
from telethon import types
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
from telethon.errors.rpcerrorlist import UserDeactivatedBanError
from telethon.sync import TelegramClient

from system.Error.TelegramErrors import telegram_phone_number_banned_error
from system.Error.TelegramErrors import telegram_user_deactivated_ban_error
from system.auxiliary_functions.auxiliary_functions import deleting_files_if_available
from system.auxiliary_functions.global_variables import console
from system.auxiliary_functions.global_variables import name_client
from system.sqlite_working_tools.sqlite_working_tools import opening_a_database_with_accounts
from system.telegram_actions.telegram_actions import account_name, get_from_the_list_phone_api_id_api_hash
from system.telegram_actions.telegram_actions import deleting_an_invalid_session

folder = "parsing_result"
file = "contact.db"


def removing_a_contact_database(user):
    """Удаляем phone списка contact.db"""
    with sqlite3.connect(f'{folder}/{file}', timeout=10) as sqlite_connection_members:
        cursor_members = sqlite_connection_members.cursor()
        cursor_members.execute("""SELECT * from contact""")
        cursor_members.execute("""DELETE from contact where phone = ?""", (user['phone'],))
        sqlite_connection_members.commit()
        cursor_members.close()
        print("[bold green] Подождите 2 - 4 секунды")
        time.sleep(random.randrange(2, 3, 4))


def creating_contact_database():
    """Создание файла с базой контактов"""
    # Удаляем файл contact.db
    deleting_files_if_available(folder, file)

    con = sqlite3.connect(f'{folder}/{file}')
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE contact(phone)")

    # Тесного пообщаемся для ясности работы.
    print("[bold green]Контакты которые были добавлены в телефонную книгу, будем записывать с файл "
          "added_contacts.csv, в папке contacts")
    # Вводим имя файла с которым будем работать
    file_name_input = console.input("[bold green][+] Введите имя файла с контактами, в папке contacts, имя вводим без "
                                    "txt: ")
    # Открываем файл с которым будем работать
    with open(f"{folder}/{file_name_input}.txt", "r") as file_contact:

        for line in file_contact.readlines():
            print(line.strip())
            # strip() - удаляет с конца и начала строки лишние пробелы, в том числе символ окончания строки
            lines = line.strip()

            entities = [lines]
            cursorObj.executemany("INSERT INTO contact(phone) VALUES (?)", (entities,))
        con.commit()
        con.close()


def show_account_contact_list():
    """Показать список контактов аккаунтов и запись результатов в файл"""

    # Открываем базу данных для работы с аккаунтами accounts/config.db
    cursor = opening_a_database_with_accounts()
    # Количество аккаунтов на данный момент в работе
    records = cursor.fetchall()
    print(f"[bold red]Всего accounts: {len(records)}")
    for row in records:
        # Получаем со списка phone, api_id, api_hash
        phone, api_id, api_hash = get_from_the_list_phone_api_id_api_hash(row)
        client = TelegramClient(f"accounts/{phone}", api_id, api_hash)
        try:
            client.connect()
            first_name, last_name = account_name(client, name_client)
            print(f"[bold red][!] Account connect {first_name} {last_name} {phone}")
            if not client.is_user_authorized():
                # Если не валидная сессия, удаляем со списка accounts/config.db и файл session
                deleting_an_invalid_session(phone)
            # client.connect()
            all_participants: list = []
            result = client(functions.contacts.GetContactsRequest(hash=0))
            # Печатаем результат
            all_participants.extend(result.users)

            # Выводим результат parsing
            for user in all_participants:
                if user.username:
                    username = user.username
                else:
                    username = ""
                if user.phone:
                    user_phone = user.phone
                else:
                    user_phone = ""
                if user.first_name:
                    first_name = user.first_name
                else:
                    first_name = ""
                if user.last_name:
                    last_name = user.last_name
                else:
                    last_name = ""
                if isinstance(user.status, types.UserStatusOffline):
                    online_at = user.status.was_online
                else:
                    online_at = ""
                name = (first_name + ' ' + last_name).strip()

                print(f"[bold green]{username}, {user.id}, {user.access_hash}, {name}, {user_phone}, {online_at}")
                entities = [username, user.id, user.access_hash, name, user_phone, online_at]

                # Запись результатов parsing в файл members_contacts.db, для дальнейшего inviting
                sqlite_connection_members = sqlite3.connect('parsing_result/members_contacts.db')
                cursor_members = sqlite_connection_members.cursor()

                cursor_members.executemany(
                    "INSERT INTO members(username, id, access_hash, name, user_phone, online_at) VALUES (?, ?, ?, "
                    "?, ?, ?)",
                    (entities,))

                sqlite_connection_members.commit()

        except sqlite3.OperationalError:
            """Если не валидная сессия, удаляем со списка accounts/config.db"""
            telegram_user_deactivated_ban_error(phone)
        except (PhoneNumberBannedError, UserDeactivatedBanError):
            # Удаляем номер телефона с базы данных
            telegram_phone_number_banned_error(client, phone)
            continue
        except KeyError:
            sys.exit(1)

    # sqlite_connection.close()


def delete_contact():
    """Удаляем контакты с аккаунтов"""

    # Открываем файл с аккаунтами accounts/config.db
    with sqlite3.connect('accounts/config.db', timeout=10) as sqlite_connection:
        cursor = sqlite_connection.cursor()
        sqlite_select_query = """SELECT * from config"""
        cursor.execute(sqlite_select_query)
        records_config: list = cursor.fetchall()
        print(f"[bold red]Всего accounts: {len(records_config)}")
        for row in records_config:
            # Получаем со списка phone, api_id, api_hash
            phone, api_id, api_hash = get_from_the_list_phone_api_id_api_hash(row)
            print(f"[bold red][!] Account connect {phone}")

            client = TelegramClient(f"accounts/{phone}", api_id, api_hash)
            if not client.is_user_authorized():
                # Если не валидная сессия, удаляем со списка accounts/config.db и файл session
                deleting_an_invalid_session(phone)
            try:
                client.connect()

                all_participants: list = []
                result = client(functions.contacts.GetContactsRequest(hash=0))
                # Печатаем результат
                print(result)
                all_participants.extend(result.users)

                # Выводим результат parsing
                for user in all_participants:
                    if user.username:
                        username = user.username
                    else:
                        username = ""
                    if user.phone:
                        user_phone = user.phone
                    else:
                        user_phone = ""
                    if user.first_name:
                        first_name = user.first_name
                    else:
                        first_name = ""
                    if user.last_name:
                        last_name = user.last_name
                    else:
                        last_name = ""
                    if isinstance(user.status, types.UserStatusOffline):
                        online_at = user.status.was_online
                    else:
                        online_at = ""
                    name = (first_name + ' ' + last_name).strip()

                    print(f"[bold green]{username}, {user.id}, {user.access_hash}, {name}, {user_phone}, {online_at}")

                    client(functions.contacts.DeleteContactsRequest(id=[user.id]))
                    # Спим для избежания ошибки о флуде
                    print("[bold green] Подождите 2 - 4 секунды")
                    time.sleep(random.randrange(2, 3, 4))
                    sqlite_connection.commit()

                client.disconnect()
                sqlite_connection.commit()

            except telethon.errors.rpcerrorlist.FloodWaitError:
                time.sleep(random.randrange(300))
                delete_contact()
            except (PhoneNumberBannedError, UserDeactivatedBanError):
                # Удаляем номер телефона с базы данных
                telegram_phone_number_banned_error(client, phone)
                continue
            except KeyError:
                sys.exit(1)

    sqlite_connection.close()


def inviting_contact():
    """Добавление данных в телефонную книгу с последующим формированием списка members_contacts.db, для inviting"""

    # Открываем файл с аккаунтами accounts/config.db
    # Открываем базу данных для работы с аккаунтами accounts/config.db
    cursor = opening_a_database_with_accounts()
    # Количество аккаунтов на данный момент в работе
    records = cursor.fetchall()
    print(f"[bold red]Всего accounts: {len(records)}")

    for row in records:
        # Получаем со списка phone, api_id, api_hash
        phone, api_id, api_hash = get_from_the_list_phone_api_id_api_hash(row)
        print(f"[bold red][!] Account connect {phone}")

        client = TelegramClient(f"accounts/{phone}", api_id, api_hash)
        if not client.is_user_authorized():
            # Если не валидная сессия, удаляем со списка accounts/config.db и файл session
            deleting_an_invalid_session(phone)

        try:
            client.connect()
            # Открываем сформированный список parsing_result/contact.db
            with sqlite3.connect('parsing_result/contact.db', timeout=10) as sqlite_connection_members:
                cursor_members = sqlite_connection_members.cursor()
                sqlite_select_query_members = """SELECT * from contact"""
                cursor_members.execute(sqlite_select_query_members)
                records_members: list = cursor_members.fetchall()
                print(f"[bold red]Всего номеров: {len(records_members)}")

                for rows in records_members:
                    user = {'phone': rows[0]}
                    phone = user['phone']

                    """Добавляем контакт в телефонную книгу"""
                    client(functions.contacts.ImportContactsRequest(contacts=[
                        types.InputPhoneContact(client_id=0, phone=phone, first_name="Номер",
                                                last_name=phone)]))
                    try:
                        # Получаем данные номера телефона https://docs.telethon.dev/en/stable/concepts/entities.html
                        contact = client.get_entity(phone)

                        if contact.username:
                            username = contact.username
                        else:
                            username = ""
                        if contact.phone:
                            user_phone = contact.phone
                        else:
                            user_phone = ""
                        if contact.first_name:
                            first_name = contact.first_name
                        else:
                            first_name = ""
                        if contact.last_name:
                            last_name = contact.last_name
                        else:
                            last_name = ""
                        if isinstance(contact.status, types.UserStatusOffline):
                            online_at = contact.status.was_online
                        else:
                            online_at = ""
                        name = (first_name + ' ' + last_name).strip()

                        entities = [username, contact.id, contact.access_hash, name, user_phone, online_at]

                        print(f"[bold green][+] Контакт с номером {phone} добавлен в телефонную книгу!")

                        # Запись результатов parsing в файл members_contacts.db, для дальнейшего inviting
                        sqlite_connection_members = sqlite3.connect('parsing_result/members_contacts.db')
                        cursor_members = sqlite_connection_members.cursor()

                        cursor_members.executemany(
                            "INSERT INTO members(username, id, access_hash, name, user_phone, online_at) VALUES ("
                            "?, ?, ?, ?, ?, ?)",
                            (entities,))

                        # После работы с номером телефона, программа удаляет номер со списка
                        removing_a_contact_database(user)

                    except ValueError:
                        print(f"[bold green][+] Контакт с номером {phone} не зарегистрирован или отсутствует "
                              f"возможность добавить в телефонную книгу!")

                        # После работы с номером телефона, программа удаляет номер со списка
                        removing_a_contact_database(user)
                        continue

                    sqlite_connection_members.commit()
            client.disconnect()

        except telethon.errors.rpcerrorlist.FloodWaitError:
            time.sleep(random.randrange(300))
            delete_contact()
            client.disconnect()

        except (PhoneNumberBannedError, UserDeactivatedBanError):
            # Удаляем номер телефона с базы данных
            telegram_phone_number_banned_error(client, phone)
            continue

        except KeyError:
            sys.exit(1)


if __name__ == "__main__":
    creating_contact_database()
    show_account_contact_list()
    delete_contact()
    inviting_contact()
