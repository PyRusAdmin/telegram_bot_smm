# # https://docs.telethon.dev/en/latest/modules/client.html#telethon.client.messages.MessageMethods.send_message
#
# import time
#
# import schedule  # https://schedule.readthedocs.io/en/stable/index.html
# from rich import print
# from rich.console import Console
# from actions.send_mess_chat.chat_dialog import send_mes
# from actions.send_mess_chat.chat_dialog import send_mes_2
# from actions.send_mess_chat.chat_dialog import send_mes_oll
#
# console = Console()
#
#
# def chat_mes_time():
#     """Пишем сообщение в одиночный чат"""
#     print(" ",
#           "Давайте настроим количество сообщений, и время отправки сообщений, работы будет много, но мы справимся",
#           " ", sep="\n")
#     print("Сколько разных сообщений?",
#           "[bold green][1][bold green] - 2 разных сообщений, чередующиеся через раз",
#           "[bold green][2][bold green] - 1 одинаковое сообщение",
#           "[bold green][3][bold green] - 1 одинаковое сообщение (в чаты с файла chat_mess.txt)", sep="\n")
#     user_input_mes_con: str = input("[+] Введите от 1 до 2: ")
#     # 2 разных сообщения, через раз
#     if user_input_mes_con == "1":
#         print("Давайте выберем, сколько сообщений в час, мы будем отправлять", " ",
#               "[bold green][1[bold green]] - 1 сообщение в час",
#               "[bold green][2[bold green]] - 2 сообщение в час",
#               "[bold green][3[bold green]] - 3 сообщение в час",
#               "[bold green][4[bold green]] - 4 сообщение в час",
#               "[bold green][5[bold green]] - 5 сообщение в час", " ", sep="\n")
#         user_input_mes_hour: str = input("[+] Введите от 1 до 5: ")
#
#         # Пишем сообщения 1 раз в час
#         if user_input_mes_hour == "1":
#             print("Пишем сообщения 1 раз в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes_2)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes_2)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes_2)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes_2)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes_2)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes_2)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes_2)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes_2)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes_2)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes_2)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes_2)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes_2)
#
#         # Пишем сообщения 2 раза в час
#         elif user_input_mes_hour == "2":
#             print("Пишем сообщения 2 раза в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_2: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_2}").do(send_mes_2)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_2}").do(send_mes_2)
#
#         # Пишем сообщения 3 раза в час
#         elif user_input_mes_hour == "3":
#             print("Пишем сообщения 3 раза в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_2: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_3: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"00:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"01:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_3}").do(send_mes_2)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"02:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"03:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"04:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_3}").do(send_mes_2)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"05:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"06:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_3}").do(send_mes_2)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"07:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"08:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_3}").do(send_mes_2)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"09:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"10:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_3}").do(send_mes_2)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"11:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"12:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_3}").do(send_mes_2)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"13:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"14:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_3}").do(send_mes_2)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"15:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"16:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_3}").do(send_mes_2)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"17:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"18:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_3}").do(send_mes_2)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"19:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"20:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_3}").do(send_mes_2)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"21:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"22:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_3}").do(send_mes_2)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"23:{user_input_minute_3}").do(send_mes)
#
#         # Пишем сообщения 4 раза в час
#         elif user_input_mes_hour == "4":
#             print("Пишем сообщения 4 раза в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_2: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_3: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_4: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"00:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"01:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"02:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"03:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"04:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"05:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"06:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"07:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"08:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"09:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"10:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"11:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"12:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"13:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"14:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"15:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"16:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"17:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"18:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"19:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"20:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"21:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"22:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_4}").do(send_mes_2)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"23:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_4}").do(send_mes_2)
#
#         # Пишем сообщения 5 раз в час
#         elif user_input_mes_hour == "5":
#             print("Пишем сообщения 5 раза в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_2: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_3: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_4: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_5: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"00:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_4}").do(send_mes_2)
#             schedule.every().day.at(f"00:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"01:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_3}").do(send_mes_2)
#             schedule.every().day.at(f"01:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_5}").do(send_mes_2)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"02:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_4}").do(send_mes_2)
#             schedule.every().day.at(f"02:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"03:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_3}").do(send_mes_2)
#             schedule.every().day.at(f"03:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_5}").do(send_mes_2)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"04:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_4}").do(send_mes_2)
#             schedule.every().day.at(f"04:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"05:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_3}").do(send_mes_2)
#             schedule.every().day.at(f"05:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_5}").do(send_mes_2)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"06:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_4}").do(send_mes_2)
#             schedule.every().day.at(f"06:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"07:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_3}").do(send_mes_2)
#             schedule.every().day.at(f"07:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_5}").do(send_mes_2)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"08:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_4}").do(send_mes_2)
#             schedule.every().day.at(f"08:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"09:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_3}").do(send_mes_2)
#             schedule.every().day.at(f"09:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_5}").do(send_mes_2)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"10:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_4}").do(send_mes_2)
#             schedule.every().day.at(f"10:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"11:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_3}").do(send_mes_2)
#             schedule.every().day.at(f"11:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_5}").do(send_mes_2)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"12:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_4}").do(send_mes_2)
#             schedule.every().day.at(f"12:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"13:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_3}").do(send_mes_2)
#             schedule.every().day.at(f"13:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_5}").do(send_mes_2)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"14:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_4}").do(send_mes_2)
#             schedule.every().day.at(f"14:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"15:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_3}").do(send_mes_2)
#             schedule.every().day.at(f"15:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_5}").do(send_mes_2)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"16:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_4}").do(send_mes_2)
#             schedule.every().day.at(f"16:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"17:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_3}").do(send_mes_2)
#             schedule.every().day.at(f"17:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_5}").do(send_mes_2)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"18:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_4}").do(send_mes_2)
#             schedule.every().day.at(f"18:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"19:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_3}").do(send_mes_2)
#             schedule.every().day.at(f"19:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_5}").do(send_mes_2)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"20:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_4}").do(send_mes_2)
#             schedule.every().day.at(f"20:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"21:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_3}").do(send_mes_2)
#             schedule.every().day.at(f"21:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_5}").do(send_mes_2)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_2}").do(send_mes_2)
#             schedule.every().day.at(f"22:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_4}").do(send_mes_2)
#             schedule.every().day.at(f"22:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes_2)
#             schedule.every().day.at(f"23:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_3}").do(send_mes_2)
#             schedule.every().day.at(f"23:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_5}").do(send_mes_2)
#
#         else:
#             print("Ошибка выбора!")
#
#         while True:
#             schedule.run_pending()
#             time.sleep(1)
#     # 1 сообщение
#     elif user_input_mes_con == "2":
#         print("Давайте выберем, сколько сообщений в час, мы будем отправлять", " ",
#               "[bold green][1][bold green] - 1 сообщение в час",
#               "[bold green][2][bold green] - 2 сообщение в час",
#               "[bold green][3][bold green] - 3 сообщение в час",
#               "[bold green][4][bold green] - 4 сообщение в час",
#               "[bold green][5][bold green] - 5 сообщение в час", " ", sep="\n")
#         user_input_mes_hour: str = input("[+] Введите от 1 до 5: ")
#
#         # Пишем сообщения 1 раз в час
#         if user_input_mes_hour == "1":
#             print("Пишем сообщения 1 раз в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes)
#
#         # Пишем сообщения 2 раза в час
#         elif user_input_mes_hour == "2":
#             print("Пишем сообщения 2 раза в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_2: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_2}").do(send_mes)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_2}").do(send_mes)
#
#         # Пишем сообщения 3 раза в час
#         elif user_input_mes_hour == "3":
#             print("Пишем сообщения 3 раза в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_2: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_3: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_3}").do(send_mes)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_3}").do(send_mes)
#
#         # Пишем сообщения 4 раза в час
#         elif user_input_mes_hour == "4":
#             print("Пишем сообщения 4 раза в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_2: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_3: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_4: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_4}").do(send_mes)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_4}").do(send_mes)
#
#         # Пишем сообщения 5 раз в час
#         elif user_input_mes_hour == "5":
#             print("Пишем сообщения 5 раза в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_2: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_3: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_4: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_5: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"00:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"01:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"02:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"03:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"04:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"05:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"06:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"07:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"08:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"09:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"10:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"11:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"12:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"13:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"14:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"15:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"16:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"17:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"18:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"19:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"20:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"21:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"22:{user_input_minute_5}").do(send_mes)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_2}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_3}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_4}").do(send_mes)
#             schedule.every().day.at(f"23:{user_input_minute_5}").do(send_mes)
#
#     # 1 одинаковое сообщение (в чаты с файла chat_mess.txt)
#     elif user_input_mes_con == "3":
#         print("Давайте выберем, сколько сообщений в час, мы будем отправлять", " ",
#               "[bold green][1][bold green] - 1 сообщение в час",
#               "[bold green][2][bold green] - 2 сообщение в час",
#               "[bold green][3][bold green] - 3 сообщение в час",
#               "[bold green][4][bold green] - 4 сообщение в час",
#               "[bold green][5][bold green] - 5 сообщение в час", " ", sep="\n")
#         user_input_mes_hour: str = input("[+] Введите от 1 до 5: ")
#
#         # Пишем сообщения 1 раз в час
#         if user_input_mes_hour == "1":
#             print("Пишем сообщения 1 раз в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes_oll)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes_oll)
#
#         # Пишем сообщения 2 раза в час
#         elif user_input_mes_hour == "2":
#             print("Пишем сообщения 2 раза в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_2: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"00:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"01:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"02:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"03:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"04:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"05:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"06:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"07:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"08:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"09:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"10:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"11:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"12:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"13:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"14:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"15:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"16:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"17:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"18:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"19:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"20:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"21:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"22:{user_input_minute_2}").do(send_mes_oll)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"23:{user_input_minute_2}").do(send_mes_oll)
#
#         # Пишем сообщения 3 раза в час
#         elif user_input_mes_hour == "3":
#             print("Пишем сообщения 3 раза в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_2: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_3: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"00:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"00:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"01:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"01:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"02:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"02:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"03:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"03:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"04:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"04:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"05:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"05:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"06:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"06:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"07:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"07:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"08:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"08:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"09:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"09:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"10:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"10:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"11:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"11:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"12:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"12:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"13:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"13:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"14:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"14:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"15:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"15:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"16:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"16:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"17:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"17:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"18:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"18:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"19:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"19:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"20:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"20:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"21:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"21:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"22:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"22:{user_input_minute_3}").do(send_mes_oll)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"23:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"23:{user_input_minute_3}").do(send_mes_oll)
#
#         # Пишем сообщения 4 раза в час
#         elif user_input_mes_hour == "4":
#             print("Пишем сообщения 4 раза в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_2: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_3: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_4: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"00:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"00:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"00:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"01:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"01:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"01:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"02:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"02:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"02:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"03:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"03:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"03:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"04:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"04:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"04:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"05:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"05:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"05:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"06:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"06:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"06:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"07:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"07:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"07:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"08:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"08:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"08:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"09:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"09:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"09:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"10:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"10:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"10:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"11:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"11:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"11:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"12:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"12:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"12:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"13:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"13:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"13:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"14:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"14:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"14:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"15:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"15:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"15:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"16:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"16:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"16:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"17:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"17:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"17:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"18:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"18:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"18:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"19:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"19:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"19:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"20:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"20:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"20:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"21:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"21:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"21:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"22:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"22:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"22:{user_input_minute_4}").do(send_mes_oll)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"23:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"23:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"23:{user_input_minute_4}").do(send_mes_oll)
#
#         # Пишем сообщения 5 раз в час
#         elif user_input_mes_hour == "5":
#             print("Пишем сообщения 5 раза в час")
#             # Вводим часы и минуты, повторяем до тех пор, пока не будет нужное количество
#             user_input_minute_1: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_2: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_3: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_4: str = input("[+] Введите минуты, публикации: ")
#             user_input_minute_5: str = input("[+] Введите минуты, публикации: ")
#             # Отправляем сообщения по времени
#
#             schedule.every().day.at(f"00:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"00:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"00:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"00:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"00:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"01:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"01:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"01:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"01:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"01:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"02:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"02:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"02:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"02:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"02:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"03:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"03:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"03:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"03:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"03:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"04:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"04:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"04:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"04:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"04:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"05:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"05:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"05:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"05:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"05:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"06:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"06:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"06:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"06:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"06:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"07:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"07:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"07:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"07:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"07:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"08:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"08:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"08:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"08:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"08:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"09:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"09:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"09:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"09:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"09:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"10:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"10:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"10:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"10:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"10:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"11:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"11:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"11:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"11:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"11:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"12:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"12:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"12:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"12:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"12:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"13:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"13:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"13:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"13:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"13:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"14:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"14:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"14:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"14:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"14:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"15:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"15:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"15:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"15:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"15:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"16:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"16:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"16:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"16:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"16:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"17:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"17:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"17:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"17:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"17:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"18:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"18:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"18:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"18:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"18:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"19:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"19:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"19:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"19:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"19:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"20:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"20:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"20:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"20:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"20:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"21:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"21:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"21:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"21:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"21:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"22:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"22:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"22:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"22:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"22:{user_input_minute_5}").do(send_mes_oll)
#
#             schedule.every().day.at(f"23:{user_input_minute_1}").do(send_mes_oll)
#             schedule.every().day.at(f"23:{user_input_minute_2}").do(send_mes_oll)
#             schedule.every().day.at(f"23:{user_input_minute_3}").do(send_mes_oll)
#             schedule.every().day.at(f"23:{user_input_minute_4}").do(send_mes_oll)
#             schedule.every().day.at(f"23:{user_input_minute_5}").do(send_mes_oll)
#
#     else:
#         print("Ошибка выбора!")
#
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     chat_mes_time()
