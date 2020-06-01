import logging
from manager.sql_manager import SQLManager
import config.format as f

"""
対象のディレクトリからSQL文を取得する
input : 対象のディレクトリ
output: SQL文のリスト
"""


class GetSql:
    def __init__(self, config=None):
        self.logger = logging.getLogger(__name__)
        self.sql_handler = SQLManager(config)

    def exec(self):
        return self.sql_handler.get_all_files()
