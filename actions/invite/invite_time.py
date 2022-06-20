import time

import schedule

from system.auxiliary_functions.auxiliary_functions import clearing_console_showing_banner
from system.auxiliary_functions.global_variables import console


def invitation_from_all_accounts_program_body():
    """Inviting по списку members"""
    members_db = "members.db"
    invitation_from_all_accounts_program_body(members_db)


def launching_an_invite_by_time():
    """Запуск Inviting по времени, для автоматизации действий на сервере"""
    # Чистим консоль, выводим банер
    clearing_console_showing_banner()
    # Вводим час запуска программы в формате 03, 06, 23
    hour_user: str = console.input("[bold green]Введите часы (Пример: 02, 03, 06): ")
    # Вводим минуты запуска программы в формате 15, 25, 35
    minute_user: str = console.input("[bold green]Введите минуты (Пример: 02, 25, 59): ")
    console.print(f"[green]Скрипт будет запускаться каждый день в {hour_user}:{minute_user}")
    # Запускаем автоматизацию
    schedule.every().day.at(f"{hour_user}:{minute_user}").do(invitation_from_all_accounts_program_body)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    invitation_from_all_accounts_program_body()
    invitation_from_all_accounts_program_body()
