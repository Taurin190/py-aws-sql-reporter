# -*- coding:utf-8 -*-
import sys
import bin.usage as u


def main(args):
    if len(args) < 2:
        u.usage()
        exit(1)
    if args[1] == 'retrieve':
        u.usage()
    elif args[1] == 'compression':
        u.usage()
    elif args[1] == 'send':
        u.usage()
    print("hello world")


if __name__ == '__main__':
    a = sys.argv
    main(a)
