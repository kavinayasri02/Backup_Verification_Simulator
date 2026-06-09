from agent.backup import get_backup_files
from agent.validator import validate_backups
from llm.narrator import generate_report

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def run_backup_verification_cycle():
    files = get_backup_files()

    result = validate_backups(files)

    table = Table(title="Backup Files")

    table.add_column("S.No", justify="center")
    table.add_column("File Name")

    for index, file in enumerate(files, start=1):
        table.add_row(str(index), file)

    console.print(table)

    report = generate_report(result)

    if result["status"] == "SUCCESS":
        console.print(
            Panel(report, title="Verification Result")
        )
    else:
        console.print(
            Panel(report, title="Verification Result")
        )