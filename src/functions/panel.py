from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.style import Style
import json

def Panel():
    with open("./config.json", "r") as json_file:
        data = json.load(json_file)
    print(" ")

    on_style = Style(color="green", bold=True)
    off_style = Style(color="red", bold=True)

    table = Table(title="Server Cloner",show_header=True, header_style="bold")
    table.add_column("Setting", style="cyan", no_wrap=True, width=30)
    table.add_column("Status", justify="center", width=10)

    for setting, status in data["settings"].items():
        table.add_row(setting.capitalize(), Text("ON" if status else " OFF", style=on_style if status else off_style))

    console = Console()
    console.print(table)
    
def Panel_Run(guild, user):
    with open("./config.json", "r") as json_file:
        data = json.load(json_file)
    print(" ")
    
    on_style = Style(color="green", bold=True)
    off_style = Style(color="red", bold=True)

    table = Table(title="Server Cloner",show_header=True, header_style="bold")
    table.add_column("Cloner is running...", style="cyan", no_wrap=True, width=30)
    table.add_column("Status", justify="center", width=10)

    for setting, status in data["settings"].items():
        table.add_row(setting.capitalize(), Text("ON" if status else " OFF", style=on_style if status else off_style))

    footer = Table(show_header=False, header_style="bold", show_lines=False, width=47)
    footer.add_column(justify="center")
    footer.add_row(f"[bold magenta]ID of server to clone ID: [green]{guild}")
    footer.add_row(f"[bold magenta]Account logged in: [green]{user}")

    console = Console()
    console.print(table)
    console.print(footer)
