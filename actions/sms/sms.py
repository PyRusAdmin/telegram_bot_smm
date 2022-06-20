import random
import sqlite3
import sys
import time

from rich import print
from telethon.errors.rpcerrorlist import BotGroupsBlockedError
from telethon.errors.rpcerrorlist import ChannelPrivateError
from telethon.errors.rpcerrorlist import ChatAdminRequiredError
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
from telethon.errors.rpcerrorlist import UserBannedInChannelError
from telethon.errors.rpcerrorlist import UserChannelsTooMuchError
from telethon.errors.rpcerrorlist import UserDeactivatedBanError
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
from system.auxiliary_functions.global_variables import console
from system.auxiliary_functions.global_variables import toaster
from system.sqlite_working_tools.sqlite_working_tools import opening_a_database_with_accounts
from system.telegram_actions.telegram_actions import deleting_an_invalid_session, \
    get_from_the_list_phone_api_id_api_hash


def we_send_a_message_from_all_accounts():
    """Отправка сообщений в личку"""
    # Чистим консоль, выводим банер
    clearing_console_showing_banner()

    print("[green][1] Отправляем сообщения по имени ")
    print("[green][2] Отправляем сообщения по ID")
    mode = int(console.input("[red]Сделай свой выбор : "))
    message = console.input("[red][+] Введите текст сообщения : ")

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
            print(f"[red][!] Account connect {phone}")
            if not client.is_user_authorized():
                # Если не валидная сессия, удаляем со списка accounts/config.db и файл session
                deleting_an_invalid_session(phone)
        except (PhoneNumberBannedError, UserDeactivatedBanError):
            # Удаляем номер телефона с базы данных
            telegram_phone_number_banned_error(client, phone)
            continue
        except KeyError:
            sys.exit(1)
        with sqlite3.connect('setting/members_group.db', timeout=10) as sqlite_connection_members:
            cursor_members = sqlite_connection_members.cursor()
            sqlite_select_query_members = """SELECT * from members"""
            cursor_members.execute(sqlite_select_query_members)
            records_members: list = cursor_members.fetchall()
            users = []
            for rows in records_members:
                user_add = {'username': rows[0], 'id': int(rows[1]), 'access_hash': int(rows[2]), 'name': rows[3]}
                users.append(user_add)
            print(f"[bold red]{users}")
            for user in users:
                try:
                    if mode == 1:
                        if user['username'] == "":
                            continue
                        receiver = client.get_input_entity(user['username'])
                    elif mode == 2:
                        receiver = InputPeerUser(user['id'], user['access_hash'])
                    print("[green][+] Отправляем сообщение:", user['name'])
                    client.send_message(receiver, message.format(user['name']))
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
    toaster.show_toast("Telegram_BOT_SMM", "Работа окончена!", icon_path="system/ico/custom.ico", duration=5)


if __name__ == "__main__":
    we_send_a_message_from_all_accounts()
