import os


def get_all_sql_in_directory(directory_path):
    sql_list = {}
    sql_files = get_all_sql_files(directory_path)
    for sql_file in sql_files:
        name = sql_file[:-4]
        sql_list[name] = get_sql_contents(directory_path + sql_file)
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
