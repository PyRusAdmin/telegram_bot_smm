import configparser

from rich.console import Console
from win10toast import ToastNotifier

# Путь к файлу для чтения groups_and_channels.txt
# file_path_gr = 'working_tools/groups_and_channels.csv'

console = Console()
toaster = ToastNotifier()
config = configparser.ConfigParser(empty_lines_in_values=False, allow_no_value=True)

name_client = "me"
