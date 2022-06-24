import random
import sys
import time

from rich import print
from telethon import TelegramClient
from telethon.errors import BotGroupsBlockedError
from telethon.errors import ChannelPrivateError
from telethon.errors import ChannelsTooMuchError
from telethon.errors import ChatAdminRequiredError
from telethon.errors import FloodWaitError
from telethon.errors import PeerFloodError
from telethon.errors import UserBannedInChannelError
from telethon.errors import UserChannelsTooMuchError
from telethon.errors import UserIdInvalidError
from telethon.errors import UserKickedError
from telethon.errors import UserNotMutualContactError
from telethon.errors import UserPrivacyRestrictedError
from telethon.errors import UsernameInvalidError
from telethon.errors import UsernameNotOccupiedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import InputPeerUser

from system.Error.TelegramErrors import removing_a_participant_from_the_list
from system.Error.TelegramErrors import telegram_bot_groups_blocked_error
from system.Error.TelegramErrors import telegram_channel_private_error
from system.Error.TelegramErrors import telegram_chat_admin_required_error
from system.Error.TelegramErrors import telegram_exceeded_the_limit_of_super_groups
from system.Error.TelegramErrors import telegram_flood_error
from system.Error.TelegramErrors import telegram_invalid_user_name
from system.Error.TelegramErrors import telegram_user_banned_in_channel_error
from system.Error.TelegramErrors import telegram_user_kicked_error
from system.Error.TelegramErrors import telegram_user_not_mutual_contact_error
from system.auxiliary_functions.auxiliary_functions import write_add_members
from system.auxiliary_functions.global_variables import config
from system.auxiliary_functions.global_variables import name_client
from system.auxiliary_functions.global_variables import toaster
from system.sqlite_working_tools.sqlite_working_tools import opening_the_list_for_inviting
from system.telegram_actions.telegram_actions import account_name, get_from_the_list_phone_api_id_api_hash, \
    checking_accounts_for_validity, open_database_accounts, we_get_username_user_id_access_hash

config.read('setting/writing_data_to_a_file.ini')
target_group_entity = config['cred']['target_group_entity']


def inviting_by_members():
    """Inviting по списку members_group.db"""
    # Местоположение файла для inviting
    members_db = "setting/members_group.db"
    invitation_from_all_accounts_program_body(members_db)


def inviting_by_numbers_contacts():
    """Inviting по списку members_contacts.db"""
    # Местоположение файла для inviting
    members_db = "members_contacts.db"
    invitation_from_all_accounts_program_body(members_db)


def invitation_from_all_accounts_program_body(members):
    """Inviting по заранее parsing списку и работа с несколькими аккаунтами"""
    toaster.show_toast("Telegram_BOT_SMM", f"Inviting в группу {target_group_entity}",
                       icon_path="system/ico/custom.ico",
                       duration=5)
    checking_accounts_for_validity()
    # Открываем базу данных для работы с аккаунтами accounts/config.db
    records = open_database_accounts()
    for row in records:
        # Получаем со списка phone, api_id, api_hash
        phone, api_id, api_hash = get_from_the_list_phone_api_id_api_hash(row)
        client = TelegramClient(f"accounts/{phone}", api_id, api_hash)
        try:
            client.connect()
            # Показываем имя и фамилию аккаунта к которому подсоединились
            first_name, last_name = account_name(client, name_client)
            print(f"[bold red][!] Account connect {first_name} {last_name} {phone}\n",
                  f"[red][!] Inviting в {target_group_entity}")

            # Подписываемся на группу которую будем inviting, если аккаунт новый, то он автоматически подпишется
            client(JoinChannelRequest(target_group_entity))

            # Открываем parsing список setting/members_group.db для inviting в группу
            cursor_members = opening_the_list_for_inviting(members)
            # Количество аккаунтов на данный момент в работе
            records_members: list = cursor_members.fetchall()
            print(f"[bold red]Всего username: {len(records_members)}")

            for rows in records_members:
                username, user_id, access_hash, user = we_get_username_user_id_access_hash(rows)
                print(f"[bold green][!] Добавляем {user_id}")
                try:
                    user_to_add = client.get_input_entity(username)
                    if username == "":
                        user_to_add = InputPeerUser(user_id, access_hash)
                    client(InviteToChannelRequest(target_group_entity, [user_to_add]))
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
                    telegram_invalid_user_name(user)
                    continue
                except (KeyError, KeyboardInterrupt):
                    print("[bold green][+] Пождите 20-25 Секунд...")
                    time.sleep(random.randrange(20, 25))
                    client.disconnect()
                    break
                except (ValueError, UsernameInvalidError):
                    telegram_invalid_user_name(user)
                    continue
                except (TypeError, UnboundLocalError):
                    continue
        except KeyError:
            sys.exit(1)
    toaster.show_toast("Telegram_BOT_SMM", f"Работа с группой {target_group_entity} окончена!",
                       icon_path="system/ico/custom.ico", duration=5)


if __name__ == "__main__":
    inviting_by_members()
