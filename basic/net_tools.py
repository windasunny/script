import click
from basic.net_tool.netstat import Netstat
from basic.net_tool.server.tcp import listen as tcp_listen


@click.group("netstat", help="netstat help...")
def netstat():
    pass


@netstat.command("show", help="nestat show...")
def show():
    netcat = Netstat()
    netcat.exec()


@netstat.command("listen", help="nestat listen...")
@click.option('-H', '--host', type=str, help="host name")
@click.option('-P', '--port', type=int, help="port number")
def listen(host: str, port: int):
    tcp_listen(host, port)


@netstat.command("validator", help="nestat listen...")
@click.option('-H', '--host', type=str, help="host name")
@click.option('-P', '--port', type=int, help="port number")
def validator(host: str, port: int):
    pass
