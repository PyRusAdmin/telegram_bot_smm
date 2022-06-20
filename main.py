# -*- coding: utf-8 -*-
import ctypes
import os.path
import platform

from rich import box
from rich.table import Table

from actions.invite.invite_all import inviting_by_members
from actions.invite.invite_all import inviting_by_numbers_contacts
from actions.invite.invite_time import launching_an_invite_by_time
from actions.pars.pars import tg_con_all
from actions.pars.pars import tg_con_all_write
from actions.pars.pars_contact import creating_contact_database
from actions.pars.pars_contact import delete_contact
from actions.pars.pars_contact import inviting_contact
from actions.pars.pars_contact import show_account_contact_list
from actions.reactions.reactions import users_choice_of_reaction
from actions.send_mess_chat.chat_dialog import message_entry_window
from actions.send_mess_chat.chat_dialog import output_the_input_field
from actions.sms.sms import we_send_a_message_from_all_accounts
from actions.subscription.subscription import cleaning_the_list_with_groups_for_subscription
from actions.subscription.subscription import subscription_all
from actions.subscription.subscription import writing_group_links_to_file
from actions.subscription.unsubscribe import unsubscribe_all
from help.help import open_help
from setting.setting import find_file
from setting.setting import time_changing_accounts_input_recording_limits_file
from setting.setting import time_inviting_input_recording_limits_file
from setting.setting import time_subscription_input_recording_limits_file
from setting.setting import writing_api_id_api_hash
from setting.setting import writing_data_to_a_file
from system.auxiliary_functions.auxiliary_functions import clearing_console_showing_banner
from system.auxiliary_functions.global_variables import config
from system.auxiliary_functions.global_variables import console
from system.auxiliary_functions.global_variables import toaster
from system.baner.baner import date_of_program_change
from system.baner.baner import program_version


# Выводим название программы в шапке окна
if platform == 'win32':
    ctypes.windll.kernel32.SetConsoleTitleW(f"Telegram_BOT_SMM: {program_version} от {date_of_program_change}")

config.read('setting/writing_data_to_a_file.ini')

target_group_entity = config['cred']['target_group_entity']


def main():
    """Основное меню программы"""

    try:
        # Чистим консоль, выводим банер
        clearing_console_showing_banner()
        # Выводим таблицу
        table = Table(title="[bold red]Основные функции программы!", box=box.HORIZONTALS)
        # Формируем колонки таблицы
        table.add_column("[bold red]№ функции", justify="center", style="cyan")
        table.add_column("[bold red]Функция", justify="left", style="green")
        table.add_column("[bold red]Описание", justify="left", style="cyan")

        # Выводим текст в таблице
        # 0
        table.add_row("[bold cyan]0", f"[bold green]Inviting {target_group_entity}",
                      "[bold cyan]Inviting по времени, по номерам, по parsing списку")
        # 1
        table.add_row("1", "Parsing",
                      "Parsing с обновлением списка members файла members_group, или до запись в существующий")
        # 2
        table.add_row("[bold cyan]2", "[bold green]Работа с контактами",
                      "[bold cyan]Добавляем контакт в телефонную книгу, и создаем список для inviting")
        # 3
        table.add_row("3", "Подписываемся / отписываемся",
                      "Подписка, отписка  групп / каналов, формирование списка, для подписки")
        # 4
        table.add_row("[bold cyan]4", "[bold green]Подключение новых аккаунтов",
                      "[bold cyan]Подключение новых аккаунтов, понадобится id и hash")
        # 5
        table.add_row("5", "Рассылка сообщений",
                      "Рассылка сообщений в личку по списку members")
        # 6
        table.add_row("[bold cyan]6", "[bold green]Рассылка сообщений по чатам",
                      "[bold cyan]Рассылка сообщений по чатам, потребуется сформировать список чатов")
        # 7
        table.add_row("7", "Работа с реакциями",
                      "Ставим реакции на посты в группе или канале, потребуется ссылка на пост и канал")
        # 8
        table.add_row("[bold cyan]8", "[bold green]Настройки",
                      "[bold cyan]Запись ссылки для Inviting, api_id, api_hash, установка времени")
        # 9
        table.add_row("9", "Помощь",
                      "Открыть файл с краткой инструкцией")
        # 10
        table.add_row("[bold cyan]10", "[bold green]Закрыть программу",
                      "[bold cyan]Закрываем программу")
        # Отображаем таблицу
        console.print(table, justify="center")
        user_input = console.input("[bold red][+] Введите номер: ")
        if user_input == "0":
            """Inviting в группы"""
            inviting_groups()
        elif user_input == "1":
            """Parsing, в новый файл members.db и до запись в файл"""
            parsing_groups()
        elif user_input == "2":
            """Работаем с контактами телефонной книги"""
            working_tools_contacts()
        elif user_input == "3":
            """Работаем с подпиской, подписка, отписка, запись ссылок в файл"""
            subscribe_unsubscribe_write_to_file()
        elif user_input == "4":
            """Настройки (подключение новых аккаунтов)"""
            find_file()
            # После отработки функции возвращаемся в начальное меню
            os.system("python main.py")
        elif user_input == "5":
            """Рассылка сообщений по списку members.db"""
            we_send_a_message_from_all_accounts()
            # После отработки функции возвращаемся в начальное меню
            os.system("python main.py")
        elif user_input == "6":
            """Рассылка по чатам"""
            sending_messages_chats()
        elif user_input == "7":
            """Работа с реакциями"""
            working_with_the_reaction()
        elif user_input == "8":
            """Настройки для программы (прописываем ссылку для inviting, api_id, api_hash)"""
            program_settings()
        elif user_input == "9":
            """Помощь (открываем файл help.docx)"""
            open_help()
            # После отработки функции возвращаемся в начальное меню
            os.system("python main.py")
        elif user_input == "10":
            """Закрываем программу"""
            exit()
        else:
            print("[bold red][!] Не верные введенные данные!")
            os.system("python main.py")

    except KeyboardInterrupt:
        """Закрытие окна программы"""
        print("[bold red][!] Скрипт остановлен!")
        toaster.show_toast("Telegram_BOT_SMM", "Работа окончена!", icon_path="system/ico/custom.ico", duration=5)


def subscribe_unsubscribe_write_to_file():
    """Подписка, отписка, запись в файл групп"""

    # Чистим консоль, выводим банер
    clearing_console_showing_banner()
    # Выводим таблицу
    table = Table(title="[bold red]Подписываемся / отписываемся!", box=box.HORIZONTALS)
    # Формируем колонки таблицы
    table.add_column("[bold red]№ функции", justify="center", style="cyan")
    table.add_column("[bold red]Функция", justify="left", style="green")
    table.add_column("[bold red]Описание", justify="left", style="cyan")

    # Выводим текст в таблице
    # 0
    table.add_row("[bold cyan]0", "[bold green]Запись данных в файл",
                  "[bold cyan]Запись групп / каналов в файл, программа записывает данные в существующий файл")
    # 1
    table.add_row("1", "Запись данных в новый файл",
                  "Запись групп / каналов в новый файл, программа удаляет старый файл и записывает данные в "
                  "новый файл, можно использовать для нескольких групп.")
    # 2
    table.add_row("[bold cyan]2", "[bold green]Подписываемся",
                  "[bold cyan]Подписываемся на группы / каналы по ранее созданному списку")
    # 3
    table.add_row("3", "Отписываемся",
                  "Отписываемся от групп / каналов чистим аккаунты")
    # 4
    table.add_row("[bold cyan]4", "[bold green]Помощь",
                  "[bold cyan]Открыть файл с краткой инструкцией")
    # 5
    table.add_row("5", "Вернуться назад",
                  "Возвращаемся в начальное меню")
    # 6
    table.add_row("[bold cyan]6", "[bold green]Закрыть программу",
                  "[bold cyan]Закрываем программу")
    # Отображаем таблицу
    console.print(table, justify="center")
    user_input = console.input("[bold red][+] Введите номер: ")

    if user_input == "0":
        """Запись групп / каналов в файл, программа записывает данные в существующий файл setting/members_group.db"""
        writing_group_links_to_file()
        # После отработки функции возвращаемся в начальное меню
        subscribe_unsubscribe_write_to_file()
    elif user_input == "1":
        """Чистка файла setting/members_group.db и запись 1 ссылки для подписки на группу / канал"""
        # Чистим консоль, выводим банер
        clearing_console_showing_banner()
        writing_group: str = console.input(
            "[bold red][+] Введите ссылку на группу: ")
        cleaning_the_list_with_groups_for_subscription(writing_group)
        # После отработки функции возвращаемся в начальное меню
        subscribe_unsubscribe_write_to_file()
    elif user_input == "2":
        """Подписываемся на группы / каналы (работа с несколькими аккаунтами)"""
        subscription_all()
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "3":
        """Отписываемся от групп / каналов (работа с несколькими аккаунтами)"""
        unsubscribe_all()
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "4":
        """Помощь"""
        open_help()
        # После отработки функции возвращаемся в начальное меню
        subscribe_unsubscribe_write_to_file()
    elif user_input == "5":
        """Вернуться назад"""
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "6":
        """Закрыть программу"""
        exit()
    else:
        print("[bold red][!] Не верные введенные данные!")
        os.system("python main.py")


def inviting_groups():
    """"Inviting в группы"""

    # Чистим консоль, выводим банер
    clearing_console_showing_banner()
    # Выводим таблицу
    table = Table(title=f"[bold red]Inviting {target_group_entity}!", box=box.HORIZONTALS)
    # Формируем колонки таблицы
    table.add_column("[bold red]№ функции", justify="center", style="cyan")
    table.add_column("[bold red]Функция", justify="left", style="green")
    table.add_column("[bold red]Описание", justify="left", style="cyan")

    # Выводим текс в таблице
    table.add_row("[bold cyan]0", f"[bold green]Inviting {target_group_entity}",
                  "[bold cyan]Inviting по списку members")
    table.add_row("1", f"Inviting time {target_group_entity}", "Inviting по списку members (запуск по времени)")
    table.add_row("[bold cyan]2", f"[bold green]Inviting contact {target_group_entity}",
                  "[bold cyan]Inviting по списку контактов members")
    table.add_row("3", "Помощь", "Открыть файл с краткой инструкцией")
    table.add_row("[bold cyan]4", "[bold green]Вернуться назад", "[bold cyan]Возвращаемся в начальное меню")
    table.add_row("5", "Закрыть программу", "Закрываем программу")
    # Отображаем таблицу
    console.print(table, justify="center")
    user_input = console.input("[bold red][+] Введите номер: ")
    # Чистим консоль, выводим банер
    if user_input == "0":
        """Inviting по списку members"""
        inviting_by_members()
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "1":
        """Inviting по времени"""
        launching_an_invite_by_time()
    elif user_input == "2":
        """Inviting по сформированному списку контактов"""
        inviting_by_numbers_contacts()
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "3":
        """Помощь"""
        open_help()
        # После отработки функции возвращаемся в начальное меню
        inviting_groups()
    elif user_input == "4":
        """Вернуться назад"""
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "5":
        """Закрыть программу"""
        exit()
    else:
        print("[bold red][!] Не верные введенные данные!")
        os.system("python main.py")


def parsing_groups():
    """Parsing групп"""

    # Чистим консоль, выводим банер
    clearing_console_showing_banner()
    # Выводим таблицу
    table = Table(title="[bold red]Parsing участников групп!", box=box.HORIZONTALS)
    # Формируем колонки таблицы
    table.add_column("[bold red]№ функции", justify="center", style="cyan")
    table.add_column("[bold red]Функция", justify="left", style="green")
    table.add_column("[bold red]Описание", justify="left", style="cyan")

    # Выводим текс в таблице
    table.add_row("[bold cyan]0", "[bold green]Parsing одной группы",
                  "[bold cyan]Parsing одной группы в список members_group.db (старый список очищается и создается "
                  "новый)")
    table.add_row("1", "Parsing нескольких групп",
                  "Parsing нескольких групп в один список members_group.db (все данные формируются в один список)")
    table.add_row("[bold cyan]2", "[bold green]Помощь",
                  "[bold cyan]Открыть файл с краткой инструкцией")
    table.add_row("3", "Вернуться назад",
                  "Возвращаемся в начальное меню")
    table.add_row("[bold cyan]4", "[bold green]Закрыть программу",
                  "[bold cyan]Закрываем программу")
    # Отображаем таблицу
    console.print(table, justify="center")
    user_input = console.input("[bold red][+] Введите номер: ")
    if user_input == "0":
        """Parsing в db обновляем файл setting/members_group.db, пользователь записывает ссылку, программа 
        автоматически подписывается"""
        target_group = console.input("[bold green][+] Введите ссылку на группу : ")
        tg_con_all(target_group)
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "1":
        """Parsing в db записываем данные в существующий файл setting/members_group.db, работа идет с пачкой групп"""
        tg_con_all_write()
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "2":
        """Помощь"""
        open_help()
        # После отработки функции возвращаемся в начальное меню
        parsing_groups()
    elif user_input == "3":
        """Вернуться назад"""
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "4":
        """Закрыть программу"""
        exit()
    else:
        print("[bold red][!] Не верные введенные данные!")
        os.system("python main.py")


def working_tools_contacts():
    """Работаем с контактами телефонной книги"""

    # Чистим консоль, выводим банер
    clearing_console_showing_banner()
    # Выводим таблицу
    table = Table(title="[bold red]Работа с контактами!", box=box.HORIZONTALS)
    # Формируем колонки таблицы
    table.add_column("[bold red]№ функции", justify="center", style="cyan")
    table.add_column("[bold red]Функция", justify="left", style="green")
    table.add_column("[bold red]Описание", justify="left", style="cyan")

    # Выводим текс в таблице
    table.add_row("[bold cyan]0", "[bold green]Формирование списка контактов",
                  "[bold cyan]Подготовление списка контактов для работы с ним")
    table.add_row("1", "Показать список контактов",
                  "Отображение списка контактов аккаунта")
    table.add_row("[bold cyan]2", "[bold green]Удаление контактов",
                  "[bold cyan]Удаление контактов во всех аккаунтах")
    table.add_row("3", "Добавление контактов контактов",
                  "Добавляем контакты в телефонную книгу")
    table.add_row("[bold cyan]4", "[bold green]Помощь",
                  "[bold cyan]Открыть файл с краткой инструкцией")
    table.add_row("5", "Вернуться назад",
                  "Возвращаемся в начальное меню")
    table.add_row("[bold cyan]6", "[bold green]Закрыть программу",
                  "[bold cyan]Закрываем программу")
    # Отображаем таблицу
    console.print(table, justify="center")
    user_input = console.input("[bold red][+] Введите номер: ")
    if user_input == "0":
        """Формирование списка контактов"""
        creating_contact_database()
    elif user_input == "1":
        """Отображение списка контактов"""
        show_account_contact_list()
    elif user_input == "2":
        """Удаляем все контакты с аккаунтов"""
        delete_contact()
    elif user_input == "3":
        """Вносим контакты в телефонную книгу"""
        inviting_contact()
    elif user_input == "4":
        """Помощь"""
        open_help()
        # После отработки функции возвращаемся в начальное меню
        working_tools_contacts()
    elif user_input == "5":
        """Вернуться назад"""
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "6":
        """Закрыть программу"""
        exit()
    else:
        print("[bold red][!] Не верные введенные данные!")
        os.system("python main.py")


def recording_the_delay_time_of_actions():
    """Запись времени задержки"""

    # Чистим консоль, выводим банер
    clearing_console_showing_banner()
    # Выводим таблицу
    table = Table(title="[bold red]Запись времени задержки", box=box.HORIZONTALS)
    # Формируем колонки таблицы
    table.add_column("[bold red]№ функции", justify="center", style="cyan")
    table.add_column("[bold red]Функция", justify="left", style="green")
    table.add_column("[bold red]Описание", justify="left", style="cyan")

    # Выводим текст в таблице
    table.add_row("[bold cyan]0", "[bold green]Время между Inviting",
                  "[bold cyan]Запись времени между приглашениями, (Inviting)")
    table.add_row("1", "Смена аккаунтов", "Запись времени между сменой аккаунтов")
    table.add_row("[bold cyan]2", "[bold green]Время между подпиской",
                  "[bold cyan]Запись времени между сменой групп при подписке.")
    table.add_row("3", "Помощь", "Открыть файл с краткой инструкцией")
    table.add_row("[bold cyan]4", "[bold green]Вернуться в главное меню",
                  "[bold cyan]Возвращаемся в главное меню")
    table.add_row("5", "Закрыть программу", "Закрываем программу")
    # Отображаем таблицу
    console.print(table, justify="center")
    user_input = console.input("[bold red][+] Введите номер: ")
    # Чистим консоль, выводим банер
    if user_input == "0":
        """Время между приглашениями Inviting"""
        time_inviting_input_recording_limits_file()
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "1":
        """Время между сменой аккаунтов"""
        time_changing_accounts_input_recording_limits_file()
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "2":
        """Время между подпиской групп"""
        time_subscription_input_recording_limits_file()
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "3":
        """Помощь"""
        open_help()
        # После отработки функции возвращаемся в начальное меню
        recording_the_delay_time_of_actions()
    elif user_input == "4":
        """Вернуться назад"""
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "5":
        """Закрыть программу"""
        exit()
    else:
        print("[bold red][!] Не верные введенные данные!")
        os.system("python main.py")


def program_settings():
    """Настройки программы, запись времени задержки, api_id, api_hash, запись ссылки для inviting"""

    # Чистим консоль, выводим банер
    clearing_console_showing_banner()
    # Выводим таблицу
    table = Table(title="[bold red]Настройки программы!", box=box.HORIZONTALS)
    # Формируем колонки таблицы
    table.add_column("[bold red]№ функции", justify="center", style="cyan")
    table.add_column("[bold red]Функция", justify="left", style="green")
    table.add_column("[bold red]Описание", justify="left", style="cyan")

    # Выводим текс в таблице
    table.add_row("[bold cyan]0", "[bold green]Запись ссылки",
                  "[bold cyan]Запись ссылки, для Inviting")
    table.add_row("1", "Запись api_id, api_hash",
                  "Запись api_id, api_hash")
    table.add_row("[bold cyan]2", "[bold green]Время задержки",
                  "[bold cyan]Время между действиями: смена аккаунтов, подписка, inviting")
    table.add_row("3", "Помощь", "Открыть файл с краткой инструкцией")
    table.add_row("[bold cyan]4", "[bold green]Вернуться назад",
                  "[bold cyan]Возвращаемся в начальное меню")
    table.add_row("5", "Закрыть программу",
                  "Закрываем программу")
    # Отображаем таблицу
    console.print(table, justify="center")
    user_input = console.input("[bold red][+] Введите номер: ")
    if user_input == "0":
        """Запись ссылки для inviting"""
        # Записываем ссылку на группу, которую будем inviting
        target_group_entity_user = writing_data_to_a_file()
        # Очищаем список с группами
        cleaning_the_list_with_groups_for_subscription(target_group_entity_user)
        # Подписываем все аккаунты
        subscription_all()
        # После отработки функции перезапускам скрипт
        os.system("python main.py")
    elif user_input == "1":
        """Запись id, hash в файл"""
        writing_api_id_api_hash()
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "2":
        """Запись времени задержки"""
        recording_the_delay_time_of_actions()
    elif user_input == "3":
        """Помощь"""
        open_help()
        # После отработки функции возвращаемся в начальное меню
        program_settings()
    elif user_input == "4":
        """Вернуться назад"""
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "5":
        """Закрыть программу"""
        exit()
    else:
        print("[bold red][!] Не верные введенные данные!")
        os.system("python main.py")


def working_with_the_reaction():
    """Работа с реакциями на посты группы или канала"""

    # Чистим консоль, выводим банер
    clearing_console_showing_banner()
    # Выводим таблицу
    table = Table(title="[bold red]Работа с реакциями!", box=box.HORIZONTALS)
    # Формируем колонки таблицы
    table.add_column("[bold red]№ функции", justify="center", style="cyan")
    table.add_column("[bold red]Функция", justify="left", style="green")
    table.add_column("[bold red]Описание", justify="left", style="cyan")

    # Выводим текст в таблице
    # 0
    table.add_row("[bold cyan]0", "[bold green]Ставим реакцию на 1 пост",
                  "[bold cyan]Ставим реакции на один пост с группе / канале")
    # # 1
    # table.add_row("1", "Запись чатов",
    #               "Запись чатов для рассылки сообщений")
    # # 2
    # table.add_row("[bold cyan]2", "[bold green]Ставим реакцию на все посты группы / канала",
    #               "[bold cyan]Ставим реакции на все посты группы / канала нужна ссылка на последний пост")
    # 1
    table.add_row("1", "Помощь", "Открыть файл с краткой инструкцией")
    # 2
    table.add_row("[bold cyan]2", "[bold green]Вернуться назад",
                  "[bold cyan]Возвращаемся в начальное меню")
    # 3
    table.add_row("3", "Закрыть программу",
                  "Закрываем программу")
    # Отображаем таблицу
    console.print(table, justify="center")
    user_input = console.input("[bold red][+] Введите номер: ")
    if user_input == "0":
        """Ставим реакции на один пост с группе / канале"""
        users_choice_of_reaction()
        # После отработки функции перезапускам скрипт
        os.system("python main.py")
    # elif user_input == "1":
    #     """Запись чатов для рассылки"""
    #     creating_a_list_of_chats_for_mailing()
    # # elif user_input == "2":
    # #     """Ставим реакции на все посты группы / канала нужна ссылка на последний пост"""
    # #     print("[!] В разработке!")
    elif user_input == "1":
        """Помощь"""
        open_help()
        # После отработки функции возвращаемся в начальное меню
        program_settings()
    elif user_input == "2":
        """Вернуться назад"""
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "3":
        """Закрыть программу"""
        exit()
    else:
        print("[bold red][!] Не верные введенные данные!")
        os.system("python main.py")


def sending_messages_chats():
    """Рассылка сообщений по чатам"""

    # Чистим консоль, выводим банер
    clearing_console_showing_banner()
    # Выводим таблицу
    table = Table(title="[bold red]Рассылка сообщений по чатам!", box=box.HORIZONTALS)
    # Формируем колонки таблицы
    table.add_column("[bold red]№ функции", justify="center", style="cyan")
    table.add_column("[bold red]Функция", justify="left", style="green")
    table.add_column("[bold red]Описание", justify="left", style="cyan")

    # Выводим текст в таблице
    # 0
    table.add_row("[bold cyan]0", "[bold green]Рассылка сообщений по чатам",
                  "[bold cyan]Рассылка сообщений по чатам, потребуется заранее записать чаты в файл")
    # 1
    table.add_row("1", "Формирование списка чатов",
                  "Формирование списка чатов для рассылки сообщений. Откроется txt файл для записи списка чатов")
    # 2
    table.add_row("[bold cyan]2", "[bold green]Помощь",
                  "[bold cyan]Открыть файл с краткой инструкцией")
    # 3
    table.add_row("3", "Вернуться назад",
                  "Возвращаемся в начальное меню")
    # 4
    table.add_row("[bold cyan]4", "[bold green]Закрыть программу",
                  "[bold cyan]Закрываем программу")
    # Отображаем таблицу
    console.print(table, justify="center")
    user_input = console.input("[bold red][+] Введите номер: ")
    if user_input == "0":
        """Рассылка сообщений по чатам"""
        message_entry_window()
        # После отработки функции перезапускам скрипт
        os.system("python main.py")
    elif user_input == "1":
        """Запись чатов в файл для рассылки сообщений"""
        output_the_input_field()
    elif user_input == "2":
        """Помощь"""
        open_help()
        # После отработки функции возвращаемся в начальное меню
        program_settings()
    elif user_input == "3":
        """Вернуться назад"""
        # После отработки функции возвращаемся в начальное меню
        os.system("python main.py")
    elif user_input == "4":
        """Закрыть программу"""
        exit()
    else:
        print("[bold red][!] Не верные введенные данные!")
        os.system("python main.py")


if __name__ == "__main__":
    main()
