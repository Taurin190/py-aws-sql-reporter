import os
import shutil
from service.store_file import StoreFile


class ZipCompress:
    def __init__(self, config=None):
        self.tmp_path = "./tmp"
        if config and "tmp_path" in config.keys():
            self.tmp_path = config["tmp_path"]

    def compress_in_tmp_directory(self):
        files = StoreFile.get_all_file_list(self.tmp_path)
        directory_list = self._get_all_directories(self.tmp_path, files)

        for directory in directory_list:
            shutil.make_archive(self.tmp_path + '/' + directory, 'zip', root_dir=self.tmp_path + '/' + directory)

    @staticmethod
    def _get_all_directories(directory_path, files):
        return list(filter(lambda x: os.path.isdir(directory_path + "/" + x), files))

    @staticmethod
    def _get_all_zip_files(files):
        return list(filter(lambda x: x.endswith(".zip"), files))
