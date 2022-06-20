# coding: utf-8
import random
import sqlite3
import time

from rich import print
from telethon import TelegramClient
from telethon.errors import ChannelPrivateError, ChatAdminRequiredError
from telethon.errors import PhoneNumberBannedError
from telethon.errors import UserDeactivatedBanError
from telethon.tl import types
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import ChannelParticipantsSearch

from actions.subscription.subscription import deleting_groups_and_channels
from actions.subscription.subscription import writing_group_links_to_file
from system.Error.TelegramErrors import telegram_phone_number_banned_error
from system.auxiliary_functions.auxiliary_functions import clearing_console_showing_banner
from system.auxiliary_functions.global_variables import name_client
from system.auxiliary_functions.global_variables import toaster
from system.sqlite_working_tools.sqlite_working_tools import opening_a_database_with_accounts
from system.telegram_actions.telegram_actions import account_name, get_from_the_list_phone_api_id_api_hash
from system.telegram_actions.telegram_actions import telegram_connect

chunk_size = 200

# Рабочая папка и файл
folder = "setting"
file = "members_group.db"


def opening_accounts_database_for_working_with_limits():
    """Открываем базу с аккаунтами для выставления лимитов и работы с ними поочередно"""
    # Открываем базу данных для работы с аккаунтами accounts/config.db
    cursor = opening_a_database_with_accounts()
    """
    fetchall() – возвращает число записей в виде упорядоченного списка;
    fetchmany(size) – возвращает число записей не более size;
    fetchone() – возвращает первую запись. https://goo.su/EFzsFU
    """
    # Выбираем 1 аккаунт в списке для подписки на группу и parsing
    records: list = cursor.fetchmany(1)
    return records


def opening_database_with_links_to_groups():
    """Открываем базу с группами"""
    # Открываем файл members_group.db, где хранятся ссылки на группы
    sqlite_connection = sqlite3.connect('setting/members_group.db')
    cursor = sqlite_connection.cursor()
    # Считываем таблицу
    cursor.execute("""SELECT * from writing_group_links""")
    """
    fetchall() – возвращает число записей в виде упорядоченного списка;
    fetchmany(size) – возвращает число записей не более size;
    fetchone() – возвращает первую запись.
    """
    records: list = cursor.fetchall()
    return records


def tg_con_all(target_group):
    """Parsing в новый список members"""
    # Открываем базу с аккаунтами и с выставленными лимитами
    records: list = opening_accounts_database_for_working_with_limits()
    for row in records:
        # Получаем со списка phone, api_id, api_hash
        phone, api_id, api_hash = get_from_the_list_phone_api_id_api_hash(row)
        # Подключаемся к аккаунту telegram
        client = TelegramClient(f"accounts/{phone}", api_id, api_hash)
        try:
            client.connect()
            # Выводим имя аккаунта
            first_name, last_name = account_name(client, name_client)
            print(f"[bold red][!] Account connect {first_name} {last_name} {phone}")

            # Предварительно чистим таблицу members
            open_members_db()
            # Parsing групп предварительно подписавшись на них
            group_parsing(client, target_group)
        except (PhoneNumberBannedError, UserDeactivatedBanError):
            """Если номер телефона был Banned, то удаляем сессию и номер с базы данных"""
            # Удаляем номер телефона с базы данных
            telegram_phone_number_banned_error(client, phone)
            break
    # Выводим сообщение пользователю об окончании работы, что-то нейтральное, так как работа может завершиться неудачей
    toaster.show_toast("Telegram_BOT_SMM", "Список успешно сформирован!", icon_path="system/ico/custom.ico", duration=5)


def tg_con_all_write():
    """Вставляем ссылку для parsing и сразу подписываемся на группу"""
    # Чистим консоль и выводим банер
    clearing_console_showing_banner()
    # Записываем ссылки в файл setting/members_group.db, для подписки и parsing
    writing_group_links_to_file()
    # Открываем базу с аккаунтами и с выставленными лимитами
    records: list = opening_accounts_database_for_working_with_limits()
    for row in records:
        # Получаем со списка phone, api_id, api_hash
        phone, api_id, api_hash = get_from_the_list_phone_api_id_api_hash(row)
        # Подключаемся к аккаунту telegram
        client = telegram_connect(phone, api_id, api_hash)
        try:
            # Подсоединяемся к telegram
            client.connect()
            first_name, last_name = account_name(client, name_client)
            print(f"[bold red][!] Account connect {first_name} {last_name} {phone}")
            # Для избежания ошибок с подключением, ставим время сна
            time.sleep(2)
            # Открываем базу с группами для дальнейшего parsing
            records: list = opening_database_with_links_to_groups()
            # Поочередно выводим записанные группы
            for groups in records:
                group = {'writing_group_links': groups[0]}
                # Вытягиваем данные из кортежа, для подстановки
                groups_wr = group['writing_group_links']
                # Parsing групп предварительно подписавшись на них
                group_parsing(client, groups_wr)
                # Удаляем отработанную группу или канал
                deleting_groups_and_channels(folder, file, groups_wr)
            # Отключаемся от telegram
            client.disconnect()
        except (PhoneNumberBannedError, UserDeactivatedBanError):
            # Удаляем номер телефона с базы данных
            telegram_phone_number_banned_error(client, phone)
            continue
    toaster.show_toast("Telegram_BOT_SMM", "Список успешно сформирован!", icon_path="system/ico/custom.ico",
                       duration=5)


def parsing_of_users_from_the_selected_group(client, target_group):
    """Собираем данные user и записываем в файл members.db (создание нового файла members.db)"""
    all_participants: list = []
    while_condition = True
    my_filter = ChannelParticipantsSearch('')
    offset = 0
    while while_condition:
        participants = client(
            GetParticipantsRequest(channel=target_group, offset=offset, filter=my_filter, limit=chunk_size, hash=0))
        all_participants.extend(participants.users)
        offset += len(participants.users)
        if len(participants.users) < 1:
            while_condition = False
    print('[bold green][+] Ищем участников... Сохраняем в файл members_group.db...')
    return all_participants


def open_members_db():
    """Чистим таблицу members в файле setting/members_group.db"""
    con = sqlite3.connect(f'{folder}/{file}')
    cursor = con.cursor()
    # Удаляем таблицу members, функция execute отвечает за SQL-запрос
    cursor.execute('DELETE FROM members;')
    con.close()


def all_participants_user(all_participants, target_group, cursor, con):
    """Формируем список setting/members_group.db"""
    for user in all_participants:
        username = ""
        if user.username:
            username = user.username
        user_phone = ""
        if user.phone:
            user_phone = user.phone
        first_name = ""
        if user.first_name:
            first_name = user.first_name
        last_name = ""
        if user.last_name:
            last_name = user.last_name
        online_at = ""
        if isinstance(user.status, types.UserStatusOffline):
            online_at = user.status.was_online
        photos_id = ""
        if isinstance(user.photo, types.UserProfilePhoto):
            photos_id = user.photo.photo_id
        name = (first_name + ' ' + last_name).strip()
        entities = [username, user.id, user.access_hash, name, user_phone, online_at, photos_id, target_group]
        print(f"[bold green]{entities}")
        """
        Оператор INSERT INTO используется для добавления записи в таблицу
        https://pythonpip.ru/examples/operatsiya-vstavki-mysql-na-python-dobavlenie-dannyh-v-tablitsu
        """
        cursor.executemany("INSERT INTO members(username, id, access_hash, name, user_phone, "
                           "online_at, photos_id, target_groups) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (entities,))
    con.commit()
    con.close()


def group_parsing(client, groups_wr):
    """Parsing группы, предварительно на них подписавшись"""
    try:
        # Подписываемся на группу
        client(JoinChannelRequest(groups_wr))
        time.sleep(2)
        # Parsing с группы с файла members_group.db и parsing в файл members.db"""
        all_participants: list = parsing_of_users_from_the_selected_group(client, groups_wr)
        # Username и link group в 1 файле, для более удобного перехода на новые версии программ
        con = sqlite3.connect('setting/members_group.db')
        cursor = con.cursor()
        # Создаем таблицу members, функция execute отвечает за SQL-запрос
        """
        IF NOT EXISTS поможет при попытке повторного подключения к базе данных.
        Запрос проверит, существует ли таблица. Если да — проверит, ничего ли не поменялось.
        """
        cursor.execute("CREATE TABLE IF NOT EXISTS members(username, id, access_hash, name, user_phone,"
                       "online_at, photos_id, target_groups)")
        # Записываем parsing данные в файл setting/members_group.db
        all_participants_user(all_participants, groups_wr, cursor, con)
        # Засыпаем, для избежания отказов на parsing со стороны telegram
        time.sleep(random.randrange(10, 11))
    except ChatAdminRequiredError:
        """Данный канал может parsing админ"""
        print("[bold red][!] Только админ может parsing!")
    except ChannelPrivateError:
        """Указанный канал / группа является приватным, и у вас нет разрешения на доступ к нему, 
        или запрет на действия. """
        print(
            "[bold red][!] Указанный канал является приватным, или вам запретили подписываться.")
        # Удаляем отработанную группу или канал
        deleting_groups_and_channels(folder, file, groups_wr)
    except ValueError:
        """Не верное имя канала / группы"""
        print("[bold red][!] Не верное имя канала / группы.")
        # Удаляем отработанную группу или канал
        deleting_groups_and_channels(folder, file, groups_wr)


if __name__ == "__main__":
    tg_con_all_write()
