import argparse
import re
import textwrap
import sys
import netstat
from server.tcp import listen


def validator_host(value):
    pattern = r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
    if not re.match(pattern, value):
        raise argparse.ArgumentTypeError(f'Invalid host format: {value}')
    return value


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Net Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            main.py nc
            main.py nc -V -H {host} -P {port} # show this port is active
            main.py nc -L -H {host} -P {port} # listen this port
        '''
                               )
    )
    # netstat
    parser.add_argument('nc', help='Enable netstat')

    # listen
    parser.add_argument('-H', '--host',
                        type=validator_host, help="Host name")
    parser.add_argument('-P', '--port',
                        type=int, help="Port number")
    parser.add_argument('-V', '--validate',
                        help="validate is actived")
    parser.add_argument('-L', '--listen',
                        action='store_true', help="listen")

    args = parser.parse_args()

    if args.nc:
        nc = netstat.Netstat(args)
        nc.run()
    if args.listen:
        listen = listen(args.host, args.port)
    else:
        print('To be continue...')
