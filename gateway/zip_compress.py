import shutil
from manager.file_manager import get_all_file_list, get_all_directories


class ZipCompress:
    def __init__(self, config=None):
        self.tmp_path = "./tmp"
        if config and "tmp_path" in config.keys():
            self.tmp_path = config["tmp_path"]

    def compress_in_directory(self, directory_name):
        files = get_all_file_list(directory_name)
        directory_list = get_all_directories(directory_name, files)
        for directory in directory_list:
            shutil.make_archive(self.tmp_path + '/' + directory, 'zip', root_dir=directory_name + '/' + directory)

