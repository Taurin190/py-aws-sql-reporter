# -*- coding:utf-8 -*-
import sys
import configparser
import bin.usage as u
from bin.retrieve import Retriever
from bin.compress import Compress
from bin.sender import Sender
import logging.config


def main(args):
    logging.config.fileConfig('config/logger.ini')
    config = configparser.ConfigParser()
    config.read("./config/app.conf")
    if len(args) < 2:
        u.usage()
        exit(1)
    if args[1] == 'retrieve':
        Retriever(config).get_all()
    elif args[1] == 'compress':
        Compress(config).exec()
    elif args[1] == 'send':
        Sender(config['mail']).send()
    elif args[1] == 'all':
        Retriever(config).get_all()
        Compress(config).exec()
    elif args[1] == '--help' or args[1] == 'help':
        u.usage('long')
    else:
        u.usage()
        exit(1)


if __name__ == '__main__':
    a = sys.argv
    main(a)
