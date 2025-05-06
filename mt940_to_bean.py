import json

import click
import mt940

from transactions import Transaction


VERSION = "0.1.0"


@click.command()
@click.argument("input", type=click.Path(exists=True))
@click.argument("output", type=click.Path(exists=False))
@click.version_option(VERSION)
def cli(input, output):
    transactions = mt940.parse(input)

    with open(output, "w", newline="") as f:
        for transaction in transactions:
            line = Transaction.from_mt940(transaction).format_bean()
            f.write(line)


if __name__ == "__main__":
    cli(auto_envvar_prefix="WODEQIAN")
