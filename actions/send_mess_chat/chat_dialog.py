# -*- coding: utf-8 -*-
import random
import sys
import time
from tkinter import *

from rich import print
from rich.console import Console
from telethon.errors import ChannelPrivateError
from telethon.errors import ChannelsTooMuchError
from telethon.errors import ChatWriteForbiddenError
from telethon.errors import FloodWaitError
from telethon.errors import PeerFloodError
from telethon.errors import PhoneNumberBannedError
from telethon.errors import UserBannedInChannelError
from telethon.errors import UserDeactivatedBanError
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest

from actions.subscription.subscription import deleting_groups_and_channels
from system.Error.TelegramErrors import telegram_chat_write_forbidden_error
from system.Error.TelegramErrors import telegram_phone_number_banned_error
from system.Error.TelegramErrors import telegram_user_banned_in_channel_error
from system.auxiliary_functions.auxiliary_functions import clearing_console_showing_banner
from system.auxiliary_functions.auxiliary_functions import deleting_files_if_available
from system.auxiliary_functions.global_variables import name_client
from system.baner.baner import date_of_program_change
from system.baner.baner import program_version
from system.sqlite_working_tools.sqlite_working_tools import opening_a_database_with_accounts
from system.sqlite_working_tools.sqlite_working_tools import opening_the_database
from system.telegram_actions.telegram_actions import account_name
from system.telegram_actions.telegram_actions import get_from_the_list_phone_api_id_api_hash

console = Console()
folder: str = "setting"
file: str = "members_group.db"
files: str = "members_group.csv"


def sending_files_via_chats():
    """Рассылка файлов по чатам"""

    clearing_console_showing_banner()
    # Спрашиваем у пользователя, через какое время будем отправлять сообщения
    link_to_the_file: str = console.input("[bold red][+] Введите название файла с папки setting/files_to_send: ")
    message_text_time: str = console.input(
        "[bold red][+] Введите время, через какое время будем отправлять файлы: ")

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
            # Подсоединяемся к telegram
            client.connect()
            first_name, last_name = account_name(client, name_client)
            print(f"[bold red][!] Account connect {first_name} {last_name} {phone}")

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

                try:
                    # Подписываемся на группу которую будем inviting, если аккаунт новый, то он автоматически подпишется
                    client(JoinChannelRequest(groups_wr))
                    # Рассылаем файлов по чатам
                    client.send_file(groups_wr, f"setting/files_to_send/{link_to_the_file}")
                    # Работу записываем в лог файл, для удобства слежения, за изменениями
                    time.sleep(int(message_text_time))
                    print(f"[bold red]{groups_wr} сообщение написал!")

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
                except ChannelsTooMuchError:
                    """Если аккаунт подписан на множество групп и каналов, то отписываемся от них"""
                    for dialog in client.iter_dialogs():
                        print(f"[green]{dialog.name}, {dialog.id}")
                        try:
                            client.delete_dialog(dialog)
                        except ChannelPrivateError:
                            continue
                        print('[green][+] Список почистили, и в файл записали.')
                    continue
                except ChatWriteForbiddenError:
                    """Вы не подписаны на группу / канал, открываем функцию подписки и подписываемся"""
                    telegram_chat_write_forbidden_error(client)
                    break
                except UserBannedInChannelError:
                    telegram_user_banned_in_channel_error(client)
                    break
                except (KeyError, KeyboardInterrupt):
                    print("[bold green][+] Пождите 20-25 Секунд...")
                    time.sleep(random.randrange(20, 25))
                    client.disconnect()
                    break
                except (TypeError, UnboundLocalError):
                    continue
            # Отключаем клиент, для обхода проблем
            client.disconnect()
        except (PhoneNumberBannedError, UserDeactivatedBanError):
            # Удаляем номер телефона с базы данных
            telegram_phone_number_banned_error(client, phone)
            continue
        except KeyError:
            sys.exit(1)


def sending_messages_files_via_chats():
    """Рассылка сообщений + файлов по чатам"""

    # Создаем программу
    root = Tk()
    root.title(f"Telegram_BOT_SMM: {program_version} от {date_of_program_change}")
    # Создаем окно ввода текста, width=50, height=25 выбираем размер программы
    text = Text(width=50, height=25)
    # Создаем поле ввода
    text.pack()

    def output_values_from_the_input_field():
        """Выводим значения с поля ввода (то что ввел пользователь)"""
        message_text = text.get("1.0", 'end-1c')
        closing_the_input_field()
        clearing_console_showing_banner()
        print("[bold red][+] Введите текс сообщения которое будем отправлять в чаты: ")

        link_to_the_file: str = console.input("[bold red][+] Введите название файла с папки setting/files_to_send: ")
        # Спрашиваем у пользователя, через какое время будем отправлять сообщения
        message_text_time: str = console.input(
            "[bold red][+] Введите время, через какое время будем отправлять сообщения: ")

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
                # Подсоединяемся к telegram
                client.connect()
                first_name, last_name = account_name(client, name_client)
                print(f"[bold red][!] Account connect {first_name} {last_name} {phone}")

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

                    try:
                        # Подписываемся на группу которую будем inviting, если аккаунт новый, то он автоматически
                        # подпишется
                        client(JoinChannelRequest(groups_wr))
                        # Рассылаем сообщение по чатам
                        client.send_message(entity=groups_wr, message=message_text)
                        # Рассылаем файлов по чатам
                        client.send_file(groups_wr, f"setting/files_to_send/{link_to_the_file}")
                        # Работу записываем в лог файл, для удобства слежения, за изменениями
                        time.sleep(int(message_text_time))
                        print(f"[bold red]{groups_wr} сообщение написал!")

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
                    except ChannelsTooMuchError:
                        """Если аккаунт подписан на множество групп и каналов, то отписываемся от них"""
                        for dialog in client.iter_dialogs():
                            print(f"[green]{dialog.name}, {dialog.id}")
                            try:
                                client.delete_dialog(dialog)
                            except ChannelPrivateError:
                                continue
                            print('[green][+] Список почистили, и в файл записали.')
                        continue
                    except ChatWriteForbiddenError:
                        """Вы не подписаны на группу / канал, открываем функцию подписки и подписываемся"""
                        telegram_chat_write_forbidden_error(client)
                        break
                    except UserBannedInChannelError:
                        telegram_user_banned_in_channel_error(client)
                        break
                    except (KeyError, KeyboardInterrupt):
                        print("[bold green][+] Пождите 20-25 Секунд...")
                        time.sleep(random.randrange(20, 25))
                        client.disconnect()
                        break
                    except (TypeError, UnboundLocalError):
                        continue
                # Отключаем клиент, для обхода проблем
                client.disconnect()
            except (PhoneNumberBannedError, UserDeactivatedBanError):
                # Удаляем номер телефона с базы данных
                telegram_phone_number_banned_error(client, phone)
                continue
            except KeyError:
                sys.exit(1)

    def closing_the_input_field():
        """Закрываем программу"""
        root.destroy()

    # Создаем кнопку по нажатии которой выведется поле ввода. После ввода чатов данные запишутся во временный файл
    but = Button(root, text="Готово", command=output_values_from_the_input_field)
    but.pack()
    # Запускаем программу
    root.mainloop()


def sending_messages_via_chats(message_text):
    """Массовая рассылка в чаты"""
    clearing_console_showing_banner()
    # Спрашиваем у пользователя, через какое время будем отправлять сообщения
    message_text_time: str = console.input(
        "[bold red][+] Введите время, через какое время будем отправлять сообщения: ")

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
            # Подсоединяемся к telegram
            client.connect()
            first_name, last_name = account_name(client, name_client)
            print(f"[bold red][!] Account connect {first_name} {last_name} {phone}")

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

                try:
                    # Подписываемся на группу которую будем inviting, если аккаунт новый, то он автоматически подпишется
                    client(JoinChannelRequest(groups_wr))
                    # Рассылаем сообщение по чатам
                    client.send_message(entity=groups_wr, message=message_text)
                    # Работу записываем в лог файл, для удобства слежения, за изменениями
                    time.sleep(int(message_text_time))
                    print(f"[bold red]{groups_wr} сообщение написал!")

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
                except ChannelsTooMuchError:
                    """Если аккаунт подписан на множество групп и каналов, то отписываемся от них"""
                    for dialog in client.iter_dialogs():
                        print(f"[green]{dialog.name}, {dialog.id}")
                        try:
                            client.delete_dialog(dialog)
                        except ChannelPrivateError:
                            continue
                        print('[green][+] Список почистили, и в файл записали.')
                    continue
                except ChatWriteForbiddenError:
                    """Вы не подписаны на группу / канал, открываем функцию подписки и подписываемся"""
                    telegram_chat_write_forbidden_error(client)
                    break
                except UserBannedInChannelError:
                    telegram_user_banned_in_channel_error(client)
                    break
                except (KeyError, KeyboardInterrupt):
                    print("[bold green][+] Пождите 20-25 Секунд...")
                    time.sleep(random.randrange(20, 25))
                    client.disconnect()
                    break
                except (TypeError, UnboundLocalError):
                    continue
            # Отключаем клиент, для обхода проблем
            client.disconnect()
        except (PhoneNumberBannedError, UserDeactivatedBanError):
            # Удаляем номер телефона с базы данных
            telegram_phone_number_banned_error(client, phone)
            continue
        except KeyError:
            sys.exit(1)


def message_entry_window():
    """Выводим поле ввода для ввода текста сообщения"""

    # Создаем программу
    root = Tk()
    root.title(f"Telegram_BOT_SMM: {program_version} от {date_of_program_change}")
    # Создаем окно ввода текста, width=50, height=25 выбираем размер программы
    text = Text(width=50, height=25)
    # Создаем поле ввода
    text.pack()

    def output_values_from_the_input_field():
        """Выводим значения с поля ввода (то что ввел пользователь)"""
        message_text = text.get("1.0", 'end-1c')
        closing_the_input_field()
        print("[bold red][+] Введите текс сообщения которое будем отправлять в чаты: ")
        sending_messages_via_chats(message_text)

    def closing_the_input_field():
        """Закрываем программу"""
        root.destroy()

    # Создаем кнопку по нажатии которой выведется поле ввода. После ввода чатов данные запишутся во временный файл
    but = Button(root, text="Готово", command=output_values_from_the_input_field)
    but.pack()
    # Запускаем программу
    root.mainloop()


def output_the_input_field():
    """Выводим поле ввода для записи"""

    # Создаем программу
    root = Tk()
    root.title(f"Telegram_BOT_SMM: {program_version} от {date_of_program_change}")
    # Создаем окно ввода текста, width=50, height=25 выбираем размер программы
    text = Text(width=50, height=25)
    # Создаем поле ввода
    text.pack()

    def output_values_from_the_input_field():
        """Выводим значения с поля ввода (то что ввел пользователь)"""
        res = text.get("1.0", 'end-1c')
        closing_the_input_field()
        with open(f'{folder}/{files}', "w") as res_as:
            res_as.write(res)
        # Записываем данные с файла в базу данных
        with open(f'{folder}/{files}', 'r') as chats:
            # Удаление списка с группами
            cursor, sqlite_connection = opening_the_database(folder, file)
            # Удаляем таблицу writing_group_links, функция execute отвечает за SQL-запрос
            cursor.execute('DELETE FROM writing_group_links;')

            for line in chats:
                # Записываем ссылку на группу для parsing в файл setting/members_group.db"""
                """
                IF NOT EXISTS поможет при попытке повторного подключения к базе данных.
                Запрос проверит, существует ли таблица. Если да — проверит, ничего ли не поменялось.
                """
                cursor.execute("CREATE TABLE IF NOT EXISTS writing_group_links(writing_group_links)")
                # strip() - удаляет с конца и начала строки лишние пробелы, в том числе символ окончания строки
                lines = line.strip()
                cursor.execute("INSERT INTO writing_group_links VALUES (?)", (lines,))
                sqlite_connection.commit()
            chats.close()

        # Удаляем файл после работы
        deleting_files_if_available(folder, files)

    def closing_the_input_field():
        """Закрываем программу"""
        root.destroy()

    # Создаем кнопку по нажатии которой выведется поле ввода. После ввода чатов данные запишутся во временный файл
    but = Button(root, text="Готово", command=output_values_from_the_input_field)
    but.pack()
    # Запускаем программу
    root.mainloop()


if __name__ == "__main__":
    output_the_input_field()
    message_entry_window()
