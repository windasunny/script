from basic.net_tools import netstat
from basic.net_tools import tcp
import click

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(help="\nNet tool", context_settings=CONTEXT_SETTINGS)
def cli() -> None:
    pass


cli.add_command(netstat)
cli.add_command(tcp)


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
