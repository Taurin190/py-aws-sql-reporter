# -*- coding:utf-8 -*-
import sys
import configparser
import bin.usage as u
from bin.retrieve import Retriever


def main(args):
    config = configparser.ConfigParser()
    config.read("./config/app.conf")
    if len(args) < 2:
        u.usage()
        exit(1)
    if args[1] == 'retrieve':
        r = Retriever(config)
        r.get_all()
    elif args[1] == 'compression':
        u.usage()
    elif args[1] == 'send':
        u.usage()
    else:
        u.usage()
        exit(1)


if __name__ == '__main__':
    a = sys.argv
    main(a)
