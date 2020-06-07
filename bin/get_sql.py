import logging
from manager.sql_manager import get_all_sql_files, get_all_sql_in_directory, get_sql_contents

"""
対象のディレクトリからSQL文を取得する
input : 対象のディレクトリ
output: SQL文のリスト
"""


class GetSql:
    def __init__(self, config=None):
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_all_sql_in_directory(self, directory):
        sql_path = "./sql"
        if self.config and "sql_path" in self.config.keys():
            sql_path = self.config["sql_path"]
        return get_all_sql_in_directory(sql_path + '/' + directory)

    def get_sql_from_path(self, file_name):
        sql_path = "./sql"
        if self.config and "sql_path" in self.config.keys():
            sql_path = self.config["sql_path"]
        return get_sql_contents(sql_path + '/' + file_name)

    def find_all_in_directory(self, directory):
        sql_path = "./sql"
        if self.config and "sql_path" in self.config.keys():
            sql_path = self.config["sql_path"]
        return get_all_sql_files(sql_path + '/' + directory)
