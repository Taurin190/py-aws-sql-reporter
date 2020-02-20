from sql.sql_handler import SQLHandler


class Retriever:
    def __init__(self, config=None):
        self.sql_handler = SQLHandler(config)

    def get_all(self):
        files = self.sql_handler.get_all_files()
        for file in files:
            self.get(file)

    def get(self, sql):
        if self.sql_handler.exist_sql_file(sql):
            print(sql)
