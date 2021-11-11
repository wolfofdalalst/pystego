import argparse
import logging
import sys

from . import ascii_art
from .stego import encode,decode

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(description='Hide secret data within a digital image using good ol\' terminal', add_help=True)
parser.add_argument('-e', help='flag to encode the file', action='store_true')
parser.add_argument('-d', help='flag to decode the file', action='store_true')
parser.add_argument('-s', '--src', help='path to the image file')
parser.add_argument('-m', '--msg', help='path to the message file')

args = parser.parse_args()

def main():
    if len(sys.argv) == 1:
        print('Welcome to,', ascii_art, sep='\n')
        parser.print_help()
        print('\nrefer to https://github.com/GuptaAyush19/pystego for more info')
        return

    if args.d:
        logging.info(f'DECODING `{args.src}`')
        decode(args.src)
    elif args.e:
        logging.info(f'ENCODING `{args.src}`')
        if args.msg:
            message = args.msg
        else:
            message = input('ENTER MESSAGE: ')
        encode(args.src, message)
    else:
        logging.error('INVALID COMMAND LINE ARGS, RUN `pystego -h`')


if __name__ == '__main__':
    main()