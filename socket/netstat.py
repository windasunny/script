import socket
import sys
import re
import os
import glob
from server.tcp import listen


class Netstat:

    path = {
        'tcp': '/proc/net/tcp',
        'tcp6': '/proc/net/tcp6',
        'udp': '/proc/net/udp',
        'udp6': '/proc/net/udp6',
    }

    stat = {
        '01': 'ESTABLISHED',
        '02': 'SYN_SENT',
        '03': 'SYN_RECEIVED',
        '04': 'FIN_WAIT1',
        '05': 'FIN_WAIT2',
        '06': 'TIME_WAIT',
        '07': 'CLOSE',
        '08': 'CLOSE_WAIT',
        '09': 'LAST_ACK',
        '0A': 'LISTEN',
        '0B': 'CLOSING',
        '0C': 'NEW_SYN_RECEIVED',
    }

    header = {
        'proto': 'Proto',
        'local_addr': 'Local_address',
        'remote_addr': 'Remote_address',
        'state': 'State',
        'pid': 'PID/Program name'
    }

    def __init__(self, args) -> None:
        self.args = args
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def procfs(self, file_path):
        with open(file_path) as file:
            file.readline()
            return [line.rstrip() for line in file]

    def _hex2dec(self, hex):
        return str(int(hex, 16))

    def _ip(self, hex_host):
        addr_list = [self._hex2dec(hex_host[6:8]), self._hex2dec(
            hex_host[4:6]), self._hex2dec(hex_host[2:4]), self._hex2dec(hex_host[0:2])]
        return ".".join(addr_list)

    def _conver_linux_net_address(self, string):
        hex_host, hex_port = string.split(':')
        return "{}:{}".format(self._ip(hex_host), self._hex2dec(hex_port))

    def _inode2system(self, inode):
        for item in glob.glob('/proc/[0-9]*/fd/[0-9]*'):
            try:
                if re.search(inode, os.readlink(item)):
                    pid = item.split('/')[2]
                    exe = os.readlink('/proc/'+pid+'/exe')
                    return exe
            except:
                return None

    def _format_line(self, data):
        return (("%(proto)-5s %(local_addr)25s %(remote_addr)25s %(state)18s %(pid)50s" % data) + "\n")

    def _exec(self):
        sys.stderr.write(self._format_line(self.header))

        for protocol in self.path:
            data = self.procfs(self.path[protocol])

            for info in data[1:]:
                row = re.split(r'\s+', info)[1:]

                if row != None:
                    _seq = {
                        'proto': protocol,
                        'local_addr': self._conver_linux_net_address(row[1]),
                        'remote_addr': self._conver_linux_net_address(row[2]),
                        'state': self.stat[row[3]],
                        'pid': "{}/{}".format(row[7], self._inode2system(row[9]))
                    }

                    if len(_seq) > 0:
                        sys.stdout.write(self._format_line(_seq))

    def run(self):
        host = self.args.host
        port = self.args.port

        if not host or not port:
            self._exec()
        else:
            pass
