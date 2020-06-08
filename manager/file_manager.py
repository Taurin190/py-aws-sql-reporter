import os


def get_all_file_list(file_path):
    return os.listdir(file_path)


def get_all_directories(directory_path, files):
    return list(filter(lambda x: os.path.isdir(directory_path + "/" + x), files))

