from sql.sql_handler import SQLHandler
from database.mysql import MySQL


class Retriever:
    def __init__(self, config=None):
        self.sql_handler = SQLHandler(config)
        self.db = MySQL(config['database'])

    def get_all(self):
        files = self.sql_handler.get_all_files()
        for file in files:
            self.get(file)

    def get(self, sql_file):
        if not self.sql_handler.exist_sql_file(sql_file):
            return
        sql = self.sql_handler.get_sql_contents(sql_file)
        print("SQL: " + sql)
        query_result = self.db.get_from_sql(sql)
        print("Result: " + str(query_result))

