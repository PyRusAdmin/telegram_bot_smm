import os

""" 
Работа с базой данных sqlite3
https://proproprogs.ru/modules/podklyuchenie-k-bd-sozdanie-i-udalenie-tablic
"""
# import sqlite3

re = "\033[1;31m"
gr = "\033[1;32m"
cy = "\033[1;36m"

folder = "setting"
file = "members_group.db"


def banner():
    os.system('cls')
    print(f"""              {re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
              {re}╚═╗{cy}├┤  │ │ │├─┘
              {re}╚═╝{cy}└─┘ ┴ └─┘┴""")


# Установка библиотек
def requirements():
    def csv_lib():
        os.system("cls")
        banner()
        print(gr + '[' + cy + '+' + gr + ']' + cy + ' Установка займет некоторое время ...')
        # Делаем красивый вид
        os.system("""pip install rich""")
        # Библиотека для работы с телегой
        os.system("""pip install telethon""")
        # Отображаем уведомление
        os.system("""pip install win10toast""")
        # Запуск скрипта по времени
        os.system("""pip install schedule""")
        # Ставим реакции
        os.system("""pip install newthon""")
        # Выводим смайлы
        os.system("""pip install emoji""")

        print(gr + "[+] Библиотеки установлены\n")

    banner()
    print(gr + '[' + cy + '+' + gr + ']' + cy + ' Установка займет до 10 минут...')
    input_csv = input(gr + '[' + cy + '+' + gr + ']' + cy + ' Продолжить установку (y/n): ').lower()
    if input_csv == "y":
        csv_lib()
    else:
        pass

    # """Создаем необходимые файлы для работы с программой"""
    #
    # def creating_a_database_file_and_tables():
    #     # Создаем файл members_group.db
    #     with sqlite3.connect('setting/members_group.db', timeout=10) as sqlite_connection:
    #         """
    #         После создания объекта соединения с базой данных нужно создать объект cursor.
    #         Он позволяет делать SQL-запросы к базе.
    #         """
    #         cursor = sqlite_connection.cursor()
    #         """
    #         IF NOT EXISTS поможет при попытке повторного подключения к базе данных.
    #         Запрос проверит, существует ли таблица. Если да — проверит, ничего ли не поменялось.
    #         """
    #         # Создаем таблицу members, функция execute отвечает за SQL-запрос
    #         cursor.execute(
    #             "CREATE TABLE IF NOT EXISTS members(username, id, access_hash, name, user_phone, online_at, "
    #             "photos_id, target_groups)")
    #         # Создаем таблицу writing_group_links, функция execute отвечает за SQL-запрос
    #         cursor.execute("CREATE TABLE IF NOT EXISTS writing_group_links(writing_group_links)")
    #         # Сохраняем изменения с помощью функции commit для объекта соединения
    #         cursor.commit()
    #
    # creating_a_database_file_and_tables()


requirements()
