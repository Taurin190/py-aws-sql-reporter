# -*- coding:utf-8 -*-
import sys
import configparser
import bin.usage as u
from bin.retrieve import Retriever
from bin.compress import Compress
from bin.get_sql import GetSql
import logging.config


def main(args):
    logging.config.fileConfig('config/logger.ini')
    config = configparser.ConfigParser()
    config.read("./config/app.conf")
    if len(args) < 2:
        logging.error("no argument")
        u.usage()
        exit(1)
    if args[1] == 'retrieve':
        logging.debug("command retrieve executed")
        if len(args) == 2:
            logging.debug("retrieve all")
            sql_files = GetSql(config).get_all_sql_in_directory('')
            Retriever(config).retrieve_from_sql_list(sql_files)
        elif len(args) == 3:
            if args[2] == 'all':
                logging.debug("retrieve all")
                sql_files = GetSql(config).get_all_sql_in_directory('')
                Retriever(config).retrieve_from_sql_list(sql_files)
            elif args[2].endswith(".sql"):
                Retriever(config).get(args[2])
        else:
            logging.error("invalid arguments for retrieve function: {}".format(args[2:]))
            u.usage('retrieve')
    elif args[1] == 'get_sql':
        logging.debug("command get_sql executed")
        sql_files = GetSql(config).get_all_sql_in_directory('')
        print(sql_files)
    elif args[1] == 'compress':
        logging.debug("command compress executed")
        Compress(config).exec()
    elif args[1] == 'all':
        logging.debug("command all executed")
        sql_files = GetSql(config).get_all_sql_in_directory('')
        Retriever(config).retrieve_from_sql_list(sql_files)
        Compress(config).exec()
    elif args[1] == '--help' or args[1] == 'help':
        logging.debug("command help executed")
        u.usage('long')
    else:
        logging.error("argument {} does't exist".format(args[1]))
        u.usage()
        exit(1)


if __name__ == '__main__':
    a = sys.argv
    main(a)
