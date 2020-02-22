import os


class StoreFile:

    def __init__(self, config=None):
        self.tmp_path = "./tmp"
        if config and "tmp_path" in config.keys():
            self.tmp_path = config["tmp_path"]

    def store_file_on_tmp(self, file_name, text):
        return StoreFile.store(self.tmp_path + '/' + file_name, text)

    def get_file_from_tmp(self, file_path):
        return StoreFile.get_file(self.tmp_path + '/' + file_path)

    @staticmethod
    def get_all_file_list(file_path):
        return os.listdir(file_path)

    @staticmethod
    def store(file_path, text):
        with open(file_path, "w") as f:
            f.write(text)

    @staticmethod
    def get_file(file_path):
        with open(file_path, "r") as f:
            return f.read()
