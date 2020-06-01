import logging
from manager.sql_manager import SQLManager
from manager.sql_manager import get_all_sql_files, get_all_sql_in_directory
import config.format as f

"""
対象のディレクトリからSQL文を取得する
input : 対象のディレクトリ
output: SQL文のリスト
"""


class GetSql:
    def __init__(self, config=None):
        self.logger = logging.getLogger(__name__)
        self.config = config
        self.sql_handler = SQLManager(config)

    def get_all_sql_in_directory(self, directory):
        sql_path = "./sql"
        if self.config and "sql_path" in self.config.keys():
            sql_path = self.config["sql_path"]
        return get_all_sql_in_directory(sql_path + '/' + directory)

    def find_all_in_directory(self, directory):
        sql_path = "./sql"
        if self.config and "sql_path" in self.config.keys():
            sql_path = self.config["sql_path"]
        return get_all_sql_files(sql_path + '/' + directory)
