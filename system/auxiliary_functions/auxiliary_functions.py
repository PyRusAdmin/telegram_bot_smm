# -*- coding: utf-8 -*-
import os
import platform
from sys import platform

from rich import print

from system.baner.baner import banner


def deleting_files_if_available(folder, file):
    """Удаление список groups_and_channels"""
    try:
        os.remove(f'{folder}/{file}')
    except FileNotFoundError:
        print(f"[green]Файл {file} был ранее удален")


def clearing_console_showing_banner():
    """Чистим консоль, выводим банер"""
    if platform == 'win32':
        # Чистим консоль (для windows cls)
        os.system("cls")
    else:
        # Чистим консоль (для linux clear)
        os.system("clear")
    # Ставим банер программы, для красивого визуального отображения
    banner()


def write_add_members(user):
    """Записываем того, кого пробовали или добавляли и записываем ошибки"""
    with open("log/members_add.csv", "a", encoding="utf-8") as write_log:
        write_log.write(f"{user}\n")


if __name__ == "__main__":
    clearing_console_showing_banner()
