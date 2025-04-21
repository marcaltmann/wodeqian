from datetime import date
from decimal import Decimal
import json

import click

from transactions import Transaction

VERSION = "0.1.0"


@click.command()
@click.option("-f", "--file", type=click.File("rb"), required=True, help="Ledger file.")
@click.option("-l", "--limit", type=int, help="Number of entries.")
@click.version_option(VERSION)
def cli(file, limit):
    """Print entries from the ledger."""
    try:
        raw_transactions = json.load(file)
    except json.decoder.JSONDecodeError:
        click.echo("The provided file is not a valid JSON file.", err=True)
        exit()

    transactions = [Transaction.from_json_dict(t) for t in raw_transactions]

    for t in transactions:
        print(t)


if __name__ == "__main__":
    cli(auto_envvar_prefix="WODEQIAN")
