from sql.sql_handler import SQLHandler
from database.mysql import MySQL


class Retriever:
    def __init__(self, config=None):
        self.sql_handler = SQLHandler(config)
        self.db = MySQL(config)

    def get_all(self):
        files = self.sql_handler.get_all_files()
        for file in files:
            self.get(file)

    def get(self, sql_file):
        if not self.sql_handler.exist_sql_file(sql_file):
            exit(1)
        sql = self.sql_handler.get_sql_contents(sql_file)
        print(sql)
        query_result = self.db.get_from_sql(sql)
        print(query_result)

