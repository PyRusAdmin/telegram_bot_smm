from rich.console import Console

console = Console()
style = "bold red"
# Версия программы
program_version = "0.4.9"
# Дата изменения
date_of_program_change = "20.06.2022"


# составлено с помощью https://manytools.org/hacker-tools/ascii-banner/
def banner():
    """Банер программы"""
    console.print("╔╦╗╔═╗╦  ╔═╗╔═╗╦═╗╔═╗╔╦╗    ╔═╗╔╦╗╔╦╗    ╔╗ ╔═╗╔╦╗", style=style, justify="center")
    console.print("║ ║╣ ║  ║╣ ║ ╦╠╦╝╠═╣║║║    ╚═╗║║║║║║    ╠╩╗║ ║ ║", style=style, justify="center")
    console.print(" ╩ ╚═╝╩═╝╚═╝╚═╝╩╚═╩ ╩╩ ╩────╚═╝╩ ╩╩ ╩────╚═╝╚═╝ ╩ ", style=style, justify="center")
    console.print("Telegram: https://t.me/VitaliyDN92", style=style, justify="center")
    console.print("   VK:    https://vk.com/zh.vitaliy", style=style, justify="center")
    # Для удобства чтения, разделяем полосками
    # https://rich.readthedocs.io/en/stable/console.html
    # Разнообразие консоли с модулем rich (python -m rich) - возможности модуля
    console.rule(f"[bold red]TELEGRAM_SMM_BOT версия программы: {program_version} "
                 f"(Дата изменения {date_of_program_change})")
    # Разнообразие консоли с модулем rich (пишем текст посередине)


if __name__ == "__main__":
    banner()
