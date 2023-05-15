import socket
import sys
import re
import os
import glob

path = {
    'tcp_path': '/proc/net/tcp',
    'tcp6_path': '/proc/net/tcp6',
    'udp_path': '/proc/net/udp',
    'udp6_path': '/proc/net/udp6',
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

def procfs():
    with open(path['tcp_path']) as file:
        return [line.rstrip() for line in file]

def _hex2dec(hex):
    return str(int(hex, 16))

def _ip(hex_host):
    addr_list = [_hex2dec(hex_host[6:8]), _hex2dec(hex_host[4:6]), _hex2dec(hex_host[2:4]), _hex2dec(hex_host[0:2])]
    return ".".join(addr_list)


def _conver_linux_net_address(string):
    hex_host, hex_port = string.split(':')
    return "{}:{}".format(_ip(hex_host), _hex2dec(hex_port))

def _inode2system(inode):
    for item in glob.glob('/proc/[0-9]*/fd/[0-9]*'):
        try:
            if re.search(inode, os.readlink(item)):
                pid = item.split('/')[2]
                exe = os.readlink('/proc/'+pid+'/exe')
                return exe
        except:
            return None

def format_line(data):
    return (("%(proto)-5s %(local_addr)25s %(remote_addr)25s %(state)18s %(pid)50s" % data) + "\n")

if __name__ == '__main__':
    data = procfs()

    sys.stderr.write(format_line(header))

    return_data = []
    for info in data[1:]:
        row = re.split(r'\s+', info)[1:]

        _seq = {
            'proto': 'tcp',
            'local_addr': _conver_linux_net_address(row[1]),
            'remote_addr': _conver_linux_net_address(row[2]),
            'state': stat[row[3]],
            'pid': "{}/{}".format(row[7], _inode2system(row[9]))
        }

        if len(_seq) > 0 :
            sys.stdout.write(format_line(_seq))
