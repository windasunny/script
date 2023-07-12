import click
from basic.net_tool.netstat import Netstat
from basic.net_tool.server.tcp import listen as tcp_listen
from basic.net_tool.server.tcp import connect as tcp_connect
from basic.net_tool.client.tcp import send as tcp_send


@click.group("netstat", help="netstat help...")
def netstat():
    pass


@click.group("tcp", help="tcp package tool...")
def tcp():
    pass


@netstat.command("list", help="list tcp/tcp6/udp/udp6 all host:port connected")
def list():
    netcat = Netstat()
    netcat.exec()


@tcp.command("listen", help="listen {host}:{port}")
@click.option("-H", "--host", type=str, help="host name")
@click.option("-P", "--port", type=int, help="port number")
def listen(host: str, port: int):
    tcp_listen(host, port)


@tcp.command("connect", help="check if a network is open")
@click.option("-H", "--host", type=str, help="host name")
@click.option("-P", "--port", type=int, help="port number")
def connect(host: str, port: int):
    tcp_connect(host, port)


@tcp.command("send", help="send {data} to {host}:{port}")
@click.option("-H", "--host", type=str, help="host name")
@click.option("-P", "--port", type=int, help="port number")
@click.option("-D", "--data", type=str, help="data to send")
def send(host: str, port: int, data: str):
    tcp_send(host, port, data)
