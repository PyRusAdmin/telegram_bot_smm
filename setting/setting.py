import configparser
import os

from rich import print

from system.auxiliary_functions.auxiliary_functions import clearing_console_showing_banner
from system.auxiliary_functions.global_variables import console
from system.auxiliary_functions.global_variables import toaster
from system.sqlite_working_tools.sqlite_working_tools import opening_the_database
# from system.telegram_actions.telegram_actions import telegram_connect_new_accounts
from system.telegram_actions.telegram_actions import telegram_connect

config = configparser.ConfigParser(empty_lines_in_values=False, allow_no_value=True)

folder = "setting"


def writing_api_id_api_hash():
    """Записываем api, hash полученный с помощью регистрации приложения на сайте https://my.telegram.org/auth"""
    print("[bold red][!] Получить api_id, api_hash можно на сайте https://my.telegram.org/auth или вводим уже "
          "имеющиеся")
    print("[bold red]После ввода данных, программа переведет вас автоматически на начальное меню")
    print("[bold green][+] Не вводите лишние данные, все строго то, что от вас требуют, или прочтите документацию!")

    api_id_data = console.input("[bold green][+] Введите api_id : ")
    api_hash_data = console.input("[bold green][+] Введите api_hash : ")

    config.add_section('cred')
    config.set('cred', 'id', api_id_data)
    config.set('cred', 'hash', api_hash_data)

    file = "api_id_api_hash.ini"
    writing_settings_to_a_file(folder, file, config)


def find_file():
    """Вводим данные в базу данных accounts/config.db"""
    folder_accounts = "accounts"
    file_accounts = "config.db"

    # Чистим консоль, выводим банер
    clearing_console_showing_banner()
    # Файл с настройками
    config.read('setting/api_id_api_hash.ini')

    # api_id и api_hash с файла setting/api_id_api_hash.ini
    api_id_data = config['cred']['id']
    api_hash_data = config['cred']['hash']

    # Вводим номер телефона
    phone_data = console.input("[bold green][+] Введите номер телефона : ")

    entities = (api_id_data, api_hash_data, phone_data)

    # Если файл найден, то записываем данные аккаунта в базу данных
    if os.path.exists("accounts/config.db"):
        cursor, sqlite_connection = opening_the_database(folder_accounts, file_accounts)
        cursor.execute("INSERT INTO config (id, hash, phone) VALUES (?, ?, ?)", entities)

    # Если файл не найден, то записываем данные аккаунта в базу данных
    else:
        # Создадим файл
        cursor, sqlite_connection = opening_the_database(folder_accounts, file_accounts)
        cursor.execute("CREATE TABLE config(id, hash, phone)")
        cursor.executemany("INSERT INTO config (id, hash, phone) VALUES (?, ?, ?)", (entities,))

    # Подключение к telegram, возвращаем client для дальнейшего отключения сессии
    client = telegram_connect(phone_data, api_id_data, api_hash_data)
    # Разрываем сессию, для предотвращения дальнейших сбоев
    client.disconnect()

    sqlite_connection.commit()
    cursor.close()

    toaster.show_toast("Telegram_BOT_SMM", "Аккаунт подсоединился!", icon_path="system/ico/custom.ico", duration=5)


def writing_data_to_a_file():
    """Записываем ссылку для inviting групп"""
    print(f"[bold green][!] Давайте запишем ссылку для inviting, ссылка должна быть [bold red]одна!")
    # Вводим ссылку на группу
    target_group_entity_user = console.input("[bold green][+] Введите ссылку на группу : ")

    config.add_section('cred')
    config.set('cred', 'target_group_entity', target_group_entity_user)

    file = "writing_data_to_a_file.ini"
    writing_settings_to_a_file(folder, file, config)
    return target_group_entity_user


def time_inviting_input_recording_limits_file():
    """Вводим данные для записи в файл"""
    clearing_console_showing_banner()
    print("[bold red][+] Введите время между Inviting! C начала меньшее, потом большее. НАПРИМЕР: 10 20!")
    time_inviting1, time_inviting2 = requesting_time_from_the_user()

    time_inviting(time_inviting1, time_inviting2)


def time_inviting(time_inviting1, time_inviting2):
    """Проводим проверку данных на числовое значение"""
    # Проверяем введенное число
    try:
        int(time_inviting1), int(time_inviting2)
        # Переводим введенное значение пользователем в числовое https://pykili.github.io/prog/02-if-and-comparison-ops
        if int(time_inviting1) < int(time_inviting2):
            recording_limits_file(time_inviting1, time_inviting2)
        else:
            print("[bold red]Не верное значение")
            del time_inviting1, time_inviting2
            time_inviting_input_recording_limits_file()
    # Если не число, то вызываем функцию заново
    except ValueError:
        print("[bold red][!] Это не численное значение!")
        del time_inviting1, time_inviting2
        time_inviting_input_recording_limits_file()


def recording_limits_file(time_inviting1, time_inviting2):
    """Запись данных в файл setting/time_inviting.ini"""
    config.add_section('cred')
    config.set('cred', 'time_inviting1', time_inviting1)
    config.set('cred', 'time_inviting2', time_inviting2)

    file = "time_inviting.ini"
    writing_settings_to_a_file(folder, file, config)


def requesting_time_from_the_user():
    """Запрашиваем время у пользователя"""
    time_user_input_1 = console.input("[bold red][+] Введите время в секундах (меньшее): ")
    time_user_input_2 = console.input("[bold red][+] Введите время в секундах (большее): ")
    return time_user_input_1, time_user_input_2


def time_changing_accounts_input_recording_limits_file():
    """Вводим данные для записи в файл"""
    clearing_console_showing_banner()
    print("[bold red][+] Введите время между сменой аккаунтов в секундах. C начала меньшее, потом большее. НАПРИМЕР: "
          "10 20!")
    time_changing_accounts1, time_changing_accounts2 = requesting_time_from_the_user()

    time_changing_accounts(time_changing_accounts1, time_changing_accounts2)


def time_changing_accounts(time_changing_accounts1, time_changing_accounts2):
    """Проводим проверку данных на числовое значение"""
    # Проверяем введенное число
    try:
        int(time_changing_accounts1), int(time_changing_accounts2)
        # Переводим введенное значение пользователем в числовое https://pykili.github.io/prog/02-if-and-comparison-ops
        if int(time_changing_accounts1) < int(time_changing_accounts2):
            recording_limits_file_time_changing_accounts(time_changing_accounts1, time_changing_accounts2)
        else:
            print("[bold red]Не верное значение")
            del time_changing_accounts1, time_changing_accounts2
            time_changing_accounts_input_recording_limits_file()
    # Если не число, то вызываем функцию заново
    except ValueError:
        print("[bold red][!] Это не численное значение!")
        del time_changing_accounts1, time_changing_accounts2
        time_changing_accounts_input_recording_limits_file()


def recording_limits_file_time_changing_accounts(time_changing_accounts1, time_changing_accounts2):
    """Запись данных в файл setting/time_changing_accounts.ini"""
    config.add_section('cred')
    config.set('cred', 'time_changing_accounts1', time_changing_accounts1)
    config.set('cred', 'time_changing_accounts2', time_changing_accounts2)

    file = "time_changing_accounts.ini"
    writing_settings_to_a_file(folder, file, config)


def time_subscription_input_recording_limits_file():
    """Вводим данные для записи в файл"""
    clearing_console_showing_banner()
    print("[bold red][+] Введите время между подпиской на группы / каналы в секундах (между приглашениями) C начала "
          "меньшее, потом большее. НАПРИМЕР: 10 20!")
    time_subscription1, time_subscription2 = requesting_time_from_the_user()

    time_subscription(time_subscription1, time_subscription2)


def time_subscription(time_subscription1, time_subscription2):
    """Проводим проверку данных на числовое значение"""
    # Проверяем введенное число
    try:
        int(time_subscription1), int(time_subscription2)
        # Переводим введенное значение пользователем в числовое https://pykili.github.io/prog/02-if-and-comparison-ops
        if int(time_subscription1) < int(time_subscription2):
            recording_limits_file_time_subscription(time_subscription1, time_subscription2)
        else:
            print("[bold red]Не верное значение")
            del time_subscription1, time_subscription2
            time_subscription_input_recording_limits_file()
    # Если не число, то вызываем функцию заново
    except ValueError:
        print("[bold red][!] Это не численное значение!")
        del time_subscription1, time_subscription2
        time_subscription_input_recording_limits_file()


def recording_limits_file_time_subscription(time_subscription1, time_subscription2):
    """Запись данных в файл setting/time_subscription.ini"""
    config.add_section('cred')
    config.set('cred', 'time_subscription1', time_subscription1)
    config.set('cred', 'time_subscription2', time_subscription2)

    file = "time_subscription.ini"
    writing_settings_to_a_file(folder, file, config)


def writing_settings_to_a_file(folder, file, config):
    """Запись данных в файл ini"""
    # Открываем файл записываем введенные данные
    with open(f'{folder}/{file}', 'w') as setup:
        config.write(setup)


if __name__ == "__main__":
    time_inviting_input_recording_limits_file()
    time_changing_accounts_input_recording_limits_file()
    time_subscription_input_recording_limits_file()
    find_file()
    writing_data_to_a_file()
    writing_api_id_api_hash()
