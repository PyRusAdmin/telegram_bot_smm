import random
import sys
import time
from tkinter import *

from rich import print
from telethon.errors import ChannelPrivateError
from telethon.errors import ChatWriteForbiddenError
from telethon.errors import FloodWaitError
from telethon.errors import PeerFloodError
from telethon.errors import PhoneNumberBannedError
from telethon.errors import UserBannedInChannelError
from telethon.errors import UserDeactivatedBanError
from telethon.errors.rpcerrorlist import BotGroupsBlockedError
from telethon.errors.rpcerrorlist import ChatAdminRequiredError
from telethon.errors.rpcerrorlist import UserChannelsTooMuchError
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.errors.rpcerrorlist import UserKickedError
from telethon.errors.rpcerrorlist import UserNotMutualContactError
from telethon.errors.rpcerrorlist import UserPrivacyRestrictedError
from telethon.errors.rpcerrorlist import UsernameInvalidError
from telethon.errors.rpcerrorlist import UsernameNotOccupiedError
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser

from system.Error.TelegramErrors import removing_a_participant_from_the_list
from system.Error.TelegramErrors import telegram_bot_groups_blocked_error
from system.Error.TelegramErrors import telegram_channel_private_error
from system.Error.TelegramErrors import telegram_chat_admin_required_error
from system.Error.TelegramErrors import telegram_chat_write_forbidden_error
from system.Error.TelegramErrors import telegram_exceeded_the_limit_of_super_groups
from system.Error.TelegramErrors import telegram_flood_error
from system.Error.TelegramErrors import telegram_invalid_user_name
from system.Error.TelegramErrors import telegram_phone_number_banned_error
from system.Error.TelegramErrors import telegram_user_banned_in_channel_error
from system.Error.TelegramErrors import telegram_user_id_invalid_error
from system.Error.TelegramErrors import telegram_user_kicked_error
from system.Error.TelegramErrors import telegram_user_not_mutual_contact_error
from system.auxiliary_functions.auxiliary_functions import clearing_console_showing_banner
from system.auxiliary_functions.auxiliary_functions import write_add_members
from system.auxiliary_functions.global_variables import console
from system.auxiliary_functions.global_variables import name_client
from system.auxiliary_functions.global_variables import toaster
from system.baner.baner import date_of_program_change
from system.baner.baner import program_version
from system.sqlite_working_tools.sqlite_working_tools import opening_a_database_with_accounts
from system.sqlite_working_tools.sqlite_working_tools import opening_the_list_for_inviting
from system.telegram_actions.telegram_actions import account_name
from system.telegram_actions.telegram_actions import deleting_an_invalid_session
from system.telegram_actions.telegram_actions import get_from_the_list_phone_api_id_api_hash


def we_send_a_message_by_members():
    """Рассылка сообщений по списку members_group.db"""
    clearing_console_showing_banner()
    members_db = "setting/members_group.db"

    # Предупреждаем пользователя о вводе ссылок в графическое окно программы
    print("[bold red][+] Введите текст который будем рассылать в личку, для вставки в графическое окно готового "
          "текста используйте комбинацию клавиш Ctrl + V, обратите внимание что при использование комбинации язык "
          "должен быть переключен на английский")

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
        we_send_a_message_from_all_accounts(members_db, message_text)

    def closing_the_input_field():
        """Закрываем программу"""
        root.destroy()

    # Создаем кнопку по нажатии которой выведется поле ввода. После ввода чатов данные запишутся во временный файл
    but = Button(root, text="Готово", command=output_values_from_the_input_field)
    but.pack()
    # Запускаем программу
    root.mainloop()


def we_send_a_message_by_numbers_contacts():
    """Рассылка сообщений по списку members_contacts.db"""
    clearing_console_showing_banner()
    members_db = "parsing_result/members_contacts.db"

    # Предупреждаем пользователя о вводе ссылок в графическое окно программы
    print("[bold red][+] Введите текст который будем рассылать в личку, для вставки в графическое окно готового "
          "текста используйте комбинацию клавиш Ctrl + V, обратите внимание что при использование комбинации язык "
          "должен быть переключен на английский")

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
        we_send_a_message_from_all_accounts(members_db, message_text)

    def closing_the_input_field():
        """Закрываем программу"""
        root.destroy()

    # Создаем кнопку по нажатии которой выведется поле ввода. После ввода чатов данные запишутся во временный файл
    but = Button(root, text="Готово", command=output_values_from_the_input_field)
    but.pack()
    # Запускаем программу
    root.mainloop()


def sending_files_to_a_personal_account():
    """Отправка файлов в личку"""

    clearing_console_showing_banner()
    members_db = "setting/members_group.db"
    # Просим пользователя ввести расширение сообщения
    link_to_the_file: str = console.input("[bold red][+] Введите название файла с папки setting/files_to_send: ")
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
            # Показываем имя и фамилию аккаунта к которому подсоединились
            first_name, last_name = account_name(client, name_client)
            print(f"[bold red][!] Account connect {first_name} {last_name} {phone}")
            if not client.is_user_authorized():
                # Если не валидная сессия, удаляем со списка accounts/config.db и файл session
                deleting_an_invalid_session(phone)

            # Открываем parsing список setting/members_group.db для inviting в группу
            cursor_members = opening_the_list_for_inviting(members_db)
            # Количество аккаунтов на данный момент в работе
            records_members: list = cursor_members.fetchall()
            print(f"[bold red]Всего username: {len(records_members)}")

            for rows in records_members:
                user = {'username': rows[0], 'id': rows[1], 'access_hash': rows[2]}
                username = user["username"]
                user_id = user["id"]
                access_hash = user["access_hash"]
                print("[green][+] Отправляем сообщение:", {user_id})
                try:
                    user_to_add = client.get_input_entity(username)
                    if username == "":
                        user_to_add = InputPeerUser(user_id, access_hash)
                    client.send_file(user_to_add, f"setting/files_to_send/{link_to_the_file}")
                    try:
                        # Записываем данные в лог файл
                        write_add_members(user)
                    except (ValueError, TypeError):
                        telegram_invalid_user_name(user)
                        continue
                    removing_a_participant_from_the_list(user)
                except (PeerFloodError, FloodWaitError):
                    telegram_flood_error(client)
                    break
                except ChatWriteForbiddenError:
                    """Вы не подписаны на группу / канал, открываем функцию подписки и подписываемся"""
                    telegram_chat_write_forbidden_error(client)
                    break
                except (UserChannelsTooMuchError, UserPrivacyRestrictedError):
                    telegram_exceeded_the_limit_of_super_groups(user)
                    continue
                except UserBannedInChannelError:
                    telegram_user_banned_in_channel_error(client)
                    break
                except BotGroupsBlockedError:
                    telegram_bot_groups_blocked_error(user)
                    continue
                except UserNotMutualContactError:
                    telegram_user_not_mutual_contact_error(user)
                    continue
                except ChatAdminRequiredError:
                    telegram_chat_admin_required_error(user)
                    continue
                except UserKickedError:
                    telegram_user_kicked_error(user)
                    continue
                except ChannelPrivateError:
                    telegram_channel_private_error(client)
                    break
                except (UserIdInvalidError, UsernameNotOccupiedError):
                    telegram_user_id_invalid_error(client)
                    continue
                except (KeyError, KeyboardInterrupt):
                    print("[green][+] Пождите 20-25 Секунд...")
                    time.sleep(random.randrange(20, 25))
                    client.disconnect()
                    break
                except (ValueError, UsernameInvalidError):
                    telegram_invalid_user_name(user)
                    continue
                except (TypeError, UnboundLocalError):
                    continue
        except (PhoneNumberBannedError, UserDeactivatedBanError):
            # Удаляем номер телефона с базы данных
            telegram_phone_number_banned_error(client, phone)
            continue
        except KeyError:
            sys.exit(1)
    toaster.show_toast("Telegram_BOT_SMM", "Работа окончена!", icon_path="system/ico/custom.ico", duration=5)


def we_send_a_message_from_all_accounts(members, message_text):
    """Отправка сообщений в личку"""

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
            # Показываем имя и фамилию аккаунта к которому подсоединились
            first_name, last_name = account_name(client, name_client)
            print(f"[bold red][!] Account connect {first_name} {last_name} {phone}")
            if not client.is_user_authorized():
                # Если не валидная сессия, удаляем со списка accounts/config.db и файл session
                deleting_an_invalid_session(phone)

            # Открываем parsing список setting/members_group.db для inviting в группу
            cursor_members = opening_the_list_for_inviting(members)
            # Количество аккаунтов на данный момент в работе
            records_members: list = cursor_members.fetchall()
            print(f"[bold red]Всего username: {len(records_members)}")

            for rows in records_members:
                user = {'username': rows[0], 'id': rows[1], 'access_hash': rows[2]}
                username = user["username"]
                user_id = user["id"]
                access_hash = user["access_hash"]
                print("[green][+] Отправляем сообщение:", {user_id})
                try:
                    user_to_add = client.get_input_entity(username)
                    if username == "":
                        user_to_add = InputPeerUser(user_id, access_hash)
                    client.send_message(user_to_add, message_text.format(username))
                    try:
                        # Записываем данные в лог файл
                        write_add_members(user)
                    except (ValueError, TypeError):
                        telegram_invalid_user_name(user)
                        continue
                    removing_a_participant_from_the_list(user)
                except (PeerFloodError, FloodWaitError):
                    telegram_flood_error(client)
                    break
                except ChatWriteForbiddenError:
                    """Вы не подписаны на группу / канал, открываем функцию подписки и подписываемся"""
                    telegram_chat_write_forbidden_error(client)
                    break
                except (UserChannelsTooMuchError, UserPrivacyRestrictedError):
                    telegram_exceeded_the_limit_of_super_groups(user)
                    continue
                except UserBannedInChannelError:
                    telegram_user_banned_in_channel_error(client)
                    break
                except BotGroupsBlockedError:
                    telegram_bot_groups_blocked_error(user)
                    continue
                except UserNotMutualContactError:
                    telegram_user_not_mutual_contact_error(user)
                    continue
                except ChatAdminRequiredError:
                    telegram_chat_admin_required_error(user)
                    continue
                except UserKickedError:
                    telegram_user_kicked_error(user)
                    continue
                except ChannelPrivateError:
                    telegram_channel_private_error(client)
                    break
                except (UserIdInvalidError, UsernameNotOccupiedError):
                    telegram_user_id_invalid_error(client)
                    continue
                except (KeyError, KeyboardInterrupt):
                    print("[green][+] Пождите 20-25 Секунд...")
                    time.sleep(random.randrange(20, 25))
                    client.disconnect()
                    break
                except (ValueError, UsernameInvalidError):
                    telegram_invalid_user_name(user)
                    continue
                except (TypeError, UnboundLocalError):
                    continue
        except (PhoneNumberBannedError, UserDeactivatedBanError):
            # Удаляем номер телефона с базы данных
            telegram_phone_number_banned_error(client, phone)
            continue
        except KeyError:
            sys.exit(1)
    toaster.show_toast("Telegram_BOT_SMM", "Работа окончена!", icon_path="system/ico/custom.ico", duration=5)


if __name__ == "__main__":
    we_send_a_message_by_members()
    we_send_a_message_by_numbers_contacts()
