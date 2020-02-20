import os


class SQLHandler:
    def __init__(self, config=None):
        self.sql_path = "./sql/"
        if config and "sql_path" in config.keys():
            self.sql_path = config["sql_path"]

    def get_all_files(self):
        files = os.listdir(self.sql_path)
        sql_files = list(filter(lambda x: x.endswith(".sql"), files))
        return sql_files
