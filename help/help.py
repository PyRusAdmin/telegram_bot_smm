import os

from rich import print

from system.auxiliary_functions.auxiliary_functions import clearing_console_showing_banner


def open_help():
    """Запуск файла с помощью"""
    # Чистим консоль, выводим банер
    clearing_console_showing_banner()
    # Открываем файл
    print(" ", "[green]Открываю инструкцию...", sep="\n")
    file_path = r'help/help.pdf'  # Открываем файл
    os.system("start " + file_path)  # Помощь


if __name__ == "__main__":
    open_help()
