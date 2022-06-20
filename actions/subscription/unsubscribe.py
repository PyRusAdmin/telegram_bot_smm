# -*- coding: utf-8 -*-

import telethon
from rich import print
from telethon import TelegramClient

from system.auxiliary_functions.auxiliary_functions import clearing_console_showing_banner
# from system.auxiliary_functions.global_variables import console
from system.auxiliary_functions.global_variables import name_client
from system.auxiliary_functions.global_variables import toaster
from system.sqlite_working_tools.sqlite_working_tools import opening_a_database_with_accounts
# from system.telegram_actions.telegram_actions import connecting_to_the_telegram_client
from system.telegram_actions.telegram_actions import account_name, get_from_the_list_phone_api_id_api_hash
from system.telegram_actions.telegram_actions import deleting_an_invalid_session
# from system.telegram_actions.telegram_actions import telegram_connect


def unsubscribe_all():
    """Отписываемся от групп, каналов, личных сообщений"""
    clearing_console_showing_banner()
    # Открываем базу данных для работы с аккаунтами accounts/config.db
    cursor = opening_a_database_with_accounts()
    # Количество аккаунтов на данный момент в работе
    records = cursor.fetchall()
    print(f"[bold red]Всего accounts: {len(records)}")
    for row in records:
        # Получаем со списка phone, api_id, api_hash
        phone, api_id, api_hash = get_from_the_list_phone_api_id_api_hash(row)

        client = TelegramClient(f"accounts/{phone}", api_id, api_hash)
        client.connect()
        first_name, last_name = account_name(client, name_client)
        print(f"[bold red][!] Account connect {first_name} {last_name} {phone}")
        if not client.is_user_authorized():
            # Если не валидная сессия, удаляем со списка accounts/config.db и файл session
            deleting_an_invalid_session(phone)
        for dialog in client.iter_dialogs():
            print(f"[green]{dialog.name}, {dialog.id}")
            try:
                client.delete_dialog(dialog)
            except telethon.errors.rpcerrorlist.ChannelPrivateError:
                continue
    print('[green][+] Список почистили, и в файл записали.')
    toaster.show_toast("Telegram_BOT_SMM", "Список почистили!", icon_path="system/ico/custom.ico", duration=5)


# def chats_id_def_one(client):
#     """Показываем ID чатов, только id, записываем результат в файл"""
#
#     # Асинхронную функцию оборачиваем в отдельную функцию
#     async def chats_id():
#         async for dialog in client.iter_dialogs():
#             console.print(f"[green]{dialog.name}, {dialog.id}")
#             await client.delete_dialog(dialog)
#
#     with client:
#         client.loop.run_until_complete(chats_id())
#
#     print('[green][+] Список почистили, и в файл записали.')
#     toaster.show_toast("Telegram_BOT_SMM", "Список почистили!", icon_path="system/ico/custom.ico", duration=5)


# def unsubscribe_from_groups_and_channels():
#     """Отписка от групп и каналов с одного аккаунта"""
#
#     # Открываем базу данных для работы с аккаунтами accounts/config.db
#     cursor = opening_a_database_with_accounts()
#     # Количество аккаунтов на данный момент в работе
#     records = cursor.fetchall()
#     print(f"[bold red]Всего accounts: {len(records)}")
#     phone, api_id, api_hash = connecting_to_the_telegram_client(records)
#     client = telegram_connect(phone, api_id, api_hash)
#     chats_id_def_one(client)


if __name__ == "__main__":
    # unsubscribe_from_groups_and_channels()
    unsubscribe_all()
