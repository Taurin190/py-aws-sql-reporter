import os


class Retriever:
    def __init__(self, config):
        self.config = config

    def get_all(self):
        print("all")

    def get(self, sql):
        if not os.path.exists('sql/' + sql):
            print("Error: {} doesn't exist", sql)
            exit(1)
        print(sql)
