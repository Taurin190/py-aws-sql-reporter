import os


def get_all_sql_in_directory(directory_path):
    sql_list = []
    sql_files = get_all_sql_files(directory_path)
    for sql_file in sql_files:
        sql_list.append(get_sql_contents(directory_path + sql_file))
    return sql_list


def get_all_sql_files(directory_path):
    files = os.listdir(directory_path)
    sql_files = list(filter(lambda x: x.endswith(".sql"), files))
    return sql_files


def get_sql_contents(sql_path):
    sql_contents = ""
    with open(sql_path) as f:
        sql_contents = f.read()
    return sql_contents


# 指定したディレクトリのSQLファイルの管理する
class SQLManager:
    def __init__(self, config=None):
        self.sql_path = "./sql"
        if config and "sql_path" in config.keys():
            self.sql_path = config["sql_path"]

    def get_all_files(self):
        files = os.listdir(self.sql_path)
        sql_files = list(filter(lambda x: x.endswith(".sql"), files))
        return sql_files

    def exist_sql_file(self, file_path):
        return os.path.exists(self._get_sql_path(file_path))

    def get_sql_contents(self, sql_path):
        sql_contents = ""
        if self.exist_sql_file(sql_path):
            with open(self._get_sql_path(sql_path)) as f:
                sql_contents = f.read()
        return sql_contents

    def _get_sql_path(self, sql_file):
        return self.sql_path + "/" + sql_file
