import os
import datetime
import logging
from manager.sql_manager import SQLManager
from gateway.mysql import MySQL
from manager.file_manager import FileManager
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
        self.sql_handler = SQLManager(config)
        self.db = MySQL(config['database'])
        dt = datetime.datetime.now()
        self.directory_name = dt.strftime(f.OUTPUT_DIRECTORY_DATE)
        os.makedirs("./tmp/" + self.directory_name)
        self.logger = logging.getLogger(__name__)

    def __del__(self):
        # delete empty directory
        file_list = FileManager.get_all_file_list("./tmp/" + self.directory_name)
        if len(file_list) == 0:
            os.rmdir("./tmp/" + self.directory_name)

    def get_all(self):
        self.logger.debug("Start Retriever all function")
        files = self.sql_handler.get_all_files()
        for file in files:
            self.get(file)

    def get(self, sql_file):
        self.logger.debug("Start Retriever function with {} file".format(sql_file))
        if not self.sql_handler.exist_sql_file(sql_file):
            self.logger.error("{} File not found".format(sql_file))
            return
        sql = self.sql_handler.get_sql_contents(sql_file)
        self.logger.debug("SQL: {}".format(sql))
        header, query_result = self.db.get_from_sql(sql)
        self.logger.debug("Result Header: {}".format(header))
        self.logger.debug("Result Body: {}".format(query_result))
        file_path = self._get_file_path(sql_file)
        self.logger.debug("Start creating file {}".format(file_path))
        ExcelWriter.create_sheet_with_result(file_path, header, query_result)

    def _get_file_path(self, sql_file_name):
        dt = datetime.datetime.now()
        date_postfix = dt.strftime(f.OUTPUT_FILE_DATE_POSTFIX)
        return "./tmp/{}/{}_{}".format(self.directory_name, sql_file_name[:-4], date_postfix)
