
class StoreFile:

    @staticmethod
    def store(file_name, text):
        with open('./tmp/' + file_name, "w") as f:
            f.write(text)

    @staticmethod
    def get_file(file_name):
        with open('./tmp/' + file_name, "r") as f:
            return f.read()
