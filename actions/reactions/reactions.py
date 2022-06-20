import re
import sys
import time

import emoji
from rich import print
from rich.console import Console
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
from telethon.errors.rpcerrorlist import UserDeactivatedBanError
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import SendReactionRequest

from actions.pars.pars import opening_a_database_with_accounts
from system.Error.TelegramErrors import telegram_phone_number_banned_error
from system.auxiliary_functions.auxiliary_functions import clearing_console_showing_banner
from system.auxiliary_functions.global_variables import toaster
from system.telegram_actions.telegram_actions import get_from_the_list_phone_api_id_api_hash

console = Console()
# Реакции pip install --upgrade --force-reinstall https://github.com/LonamiWebs/Telethon/archive/v1.24.zip
# https://pypi.org/project/newthon/


"""
Сайты со смайлами
https://unicode-table.com/ru/
https://emojis.wiki/ru/
"""


def users_choice_of_reaction():
    """Выбираем реакцию для выставления в чате / канале"""
    # Чистим консоль и выводим банер
    clearing_console_showing_banner()
    print("[bold red][!] Давайте выберем какую реакцию будем ставить")
    # Перечисляем варианты реакций
    print(emoji.emojize("[bold green][0] Поднятый большой палец :thumbs_up:"))
    print(emoji.emojize("[bold green][1] Опущенный большой палец :thumbs_down:"))
    print(emoji.emojize("[bold green][2] Красное сердце :red_heart:"))
    print(emoji.emojize("[bold green][3] Огонь :fire:"))
    print(emoji.emojize("[bold green][4] Хлопушка :party_popper:"))
    print(emoji.emojize("[bold green][5] Лицо, кричащее от страха :face_screaming_in_fear:"))
    print(emoji.emojize(
        "[bold green][6] Широко улыбающееся лицо с улыбающимися глазами :beaming_face_with_smiling_eyes:"))
    print(emoji.emojize("[bold green][7] Лицо с открытым ртом и в холодном поту :crying_face:"))
    print(emoji.emojize("[bold green][8] Фекалии :pile_of_poo:"))
    print(emoji.emojize("[bold green][9] Аплодирующие руки :clapping_hands:"))

    user_input = console.input("[bold red][+] Введите номер: ")

    if user_input == "0":
        # Поднятый большой палец
        thumbs_up = "👍"
        reactions_for_groups_and_messages(thumbs_up)
    elif user_input == "1":
        # Опущенный большой палец
        thumbs_down = "👎"
        reactions_for_groups_and_messages(thumbs_down)
    elif user_input == "2":
        # Красное сердце
        red_heart = "❤"
        reactions_for_groups_and_messages(red_heart)
    elif user_input == "3":
        # Огонь
        fire = "🔥"
        reactions_for_groups_and_messages(fire)
    elif user_input == "4":
        # Хлопушка
        party_popper = "🎉"
        reactions_for_groups_and_messages(party_popper)
    elif user_input == "5":
        # Лицо, кричащее от страха
        face_screaming_in_fear = "😱"
        reactions_for_groups_and_messages(face_screaming_in_fear)
    elif user_input == "6":
        # Широко улыбающееся лицо с улыбающимися глазами
        beaming_face_with_smiling_eyes = "😁"
        reactions_for_groups_and_messages(beaming_face_with_smiling_eyes)
    elif user_input == "7":
        # Лицо с открытым ртом и в холодном поту
        crying_face = "😢"
        reactions_for_groups_and_messages(crying_face)
    elif user_input == "8":
        # Фекалии
        pile_of_poo = "💩"
        reactions_for_groups_and_messages(pile_of_poo)
    elif user_input == "9":
        # Аплодирующие руки
        clapping_hands = "👏"
        reactions_for_groups_and_messages(clapping_hands)


def reactions_for_groups_and_messages(reaction_input):
    """Вводим ссылку на группу и ссылку на сообщение"""

    # Ссылка на группу или канал
    chat = console.input("[bold red][+] Введите ссылку на группу / канал: ")
    # Ссылка на сообщение введенное пользователем
    message = console.input("[bold red][+] Введите ссылку на сообщение или пост: ")

    # Ссылка на группу или канал с добавлением символа /
    chat_mod = f"{chat}/"
    # Преобразовываем в номер сообщения, с помощью регулярных выражений
    message_number = re.sub(f'{chat_mod}', '', f"{message}")

    # Выбираем лимиты для аккаунтов
    records = choosing_a_number_of_reactions()
    # Ставим реакцию на пост, сообщение
    send_reaction_request(records, chat, int(message_number), reaction_input)


def choosing_a_number_of_reactions():
    """Выбираем лимиты для аккаунтов"""
    print("[bold red]Введите количество с которых будут поставлены реакции")

    # Открываем базу данных для работы с аккаунтами accounts/config.db
    cursor = opening_a_database_with_accounts()
    # Количество аккаунтов на данный момент в работе
    number_of_accounts = cursor.fetchall()
    print(f"[bold red]Всего accounts: {len(number_of_accounts)}")
    # Закрываем базу, для избежания ошибок с проставлением реакций
    cursor.close()

    # Открываем базу данных для работы с аккаунтами accounts/config.db
    cursor = opening_a_database_with_accounts()
    """
    fetchall() – возвращает число записей в виде упорядоченного списка;
    fetchmany(size) – возвращает число записей не более size;
    fetchone() – возвращает первую запись. https://goo.su/EFzsFU
    """
    # Выбираем количество аккаунтов для выставления реакций
    user_input = console.input("[bold red][+] Введите количество аккаунтов для выставления реакций: ")
    records = cursor.fetchmany(int(user_input))
    return records


def send_reaction_request(records, chat, message, reaction_input):
    """Ставим реакции на сообщения"""
    for row in records:
        # Получаем со списка phone, api_id, api_hash
        phone, api_id, api_hash = get_from_the_list_phone_api_id_api_hash(row)
        client = TelegramClient(f"accounts/{phone}", api_id, api_hash)
        try:
            # Подсоединяемся к telegram
            client.connect()
            # Подписываемся на группу
            client(JoinChannelRequest(chat))
            # Ставим реакцию
            client(SendReactionRequest(chat, message, reaction=f'{reaction_input}'))
            time.sleep(1)
            # Отключаемся после выполненных действий
            client.disconnect()
        # Ловим ошибки 
        except (PhoneNumberBannedError, UserDeactivatedBanError):
            # Удаляем номер телефона с базы данных
            telegram_phone_number_banned_error(client, phone)
            continue
        except KeyError:
            sys.exit(1)
    toaster.show_toast("Telegram_BOT_SMM", f"Работа с группой {chat} окончена!", icon_path="system/ico/custom.ico",
                       duration=5)


if __name__ == "__main__":
    users_choice_of_reaction()
