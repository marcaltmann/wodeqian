import click

VERSION = "0.1.0"


@click.command()
@click.option("-f", "--file", type=click.File("rb"), required=True, help="Ledger file.")
@click.option("-l", "--limit", type=int, help="Number of entries.")
@click.version_option(VERSION)
def cli(file, limit):
    """Print entries from the ledger."""
    if limit is None:
        click.echo(f"There is no limit.")
    else:
        click.echo(f"The limit is {limit}.")

    print(file.name)


if __name__ == "__main__":
    cli(auto_envvar_prefix="WODEQIAN")
