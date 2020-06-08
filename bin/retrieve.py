import os
import datetime
import logging
from gateway.mysql import MySQL
from manager.file_manager import get_all_file_list
from gateway.excel_writer import ExcelWriter
import config.format as f

"""
指定されたSQLを元にデータを取り出しExcelファイルをローカルに保存する
 input : 保存するファイルのパス
 output: ローカルにExcelファイルを保存
 output: 保存したファイル名
"""


class Retriever:
    def __init__(self, config=None):
        self.logger = logging.getLogger(__name__)
        if 'database' not in config.keys():
            self.logger.error("gateway config not found")
            exit(1)
        self.db = MySQL(config['database'])
        dt = datetime.datetime.now()
        self.directory_name = dt.strftime(f.OUTPUT_DIRECTORY_DATE)
        os.makedirs("./tmp/" + self.directory_name)
        self.logger = logging.getLogger(__name__)

    def __del__(self):
        # delete empty directory
        file_list = get_all_file_list("./tmp/" + self.directory_name)
        if len(file_list) == 0:
            os.rmdir("./tmp/" + self.directory_name)

    def retrieve_from_sql_list(self, sql_list):
        for name, sql in sql_list.items():
            self.retrieve_from_sql(name, sql)

    def retrieve_from_sql(self, name, sql):
        self.logger.debug("SQL: {}".format(sql))
        header, query_result = self.db.get_from_sql(sql)
        self.logger.debug("Result Header: {}".format(header))
        self.logger.debug("Result Body: {}".format(query_result))
        self.logger.debug("Start creating file {}".format(name))
        ExcelWriter.create_sheet_with_result(name, header, query_result)
