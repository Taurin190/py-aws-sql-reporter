from util.zip_compress import ZipCompress


class Compress:
    def __init__(self, config=None):
        self.zip_compress = ZipCompress(config)

    def exec(self):
        self.zip_compress.compress_in_tmp_directory()
