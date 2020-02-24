import os
import datetime
from sql.sql_handler import SQLHandler
from database.mysql import MySQL
from service.file_manager import FileManager
from service.excel_writer import ExcelWriter
import config.format as f


class Retriever:
    def __init__(self, config=None):
        self.sql_handler = SQLHandler(config)
        self.db = MySQL(config['database'])
        dt = datetime.datetime.now()
        self.directory_name = dt.strftime(f.OUTPUT_DIRECTORY_DATE)
        os.makedirs("./tmp/" + self.directory_name)

    def __del__(self):
        # delete empty directory
        file_list = FileManager.get_all_file_list("./tmp/" + self.directory_name)
        if len(file_list) == 0:
            os.rmdir("./tmp/" + self.directory_name)

    def get_all(self):
        files = self.sql_handler.get_all_files()
        for file in files:
            self.get(file)

    def get(self, sql_file):
        if not self.sql_handler.exist_sql_file(sql_file):
            return
        sql = self.sql_handler.get_sql_contents(sql_file)
        print("SQL: " + sql)
        header, query_result = self.db.get_from_sql(sql)
        print("Result: " + str(query_result))
        file_path = self._get_file_path(sql_file)
        ExcelWriter.create_sheet_with_result(file_path, header, query_result)

    def _get_file_path(self, sql_file_name):
        dt = datetime.datetime.now()
        date_postfix = dt.strftime(f.OUTPUT_FILE_DATE_POSTFIX)
        return "./tmp/{}/{}_{}".format(self.directory_name, sql_file_name[:-4], date_postfix)
