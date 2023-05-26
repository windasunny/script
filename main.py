import textwrap
from basic.net_tools import netstat
import click

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(
    help=f"\nNet tool",
    context_settings=CONTEXT_SETTINGS
)
def cli() -> None:
    pass


cli.add_command(netstat)


def main() -> None:
    cli()


if __name__ == '__main__':
    main()
