import os


class SQLHandler:
    def __init__(self, config=None):
        self.sql_path = "./sql"
        if config and "sql_path" in config.keys():
            self.sql_path = config["sql_path"]

    def get_all_files(self):
        files = os.listdir(self.sql_path)
        sql_files = list(filter(lambda x: x.endswith(".sql"), files))
        return sql_files

    def exist_sql_file(self, file_path):
        return os.path.exists(self.sql_path + "/" + file_path)

    def get_sql_contents(self, sql_path):
        sql_contents = ""
        if self.exist_sql_file(sql_path):
            with open(sql_contents) as f:
                sql_contents = f.read()
        return sql_contents
