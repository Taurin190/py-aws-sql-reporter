import logging
from gateway.zip_compress import ZipCompress

"""
指定されたディレクトリをZIPに圧縮する
 input : 圧縮するディレクトリ
 output: 圧縮したZIPのファイルの配列
"""


class Compress:
    def __init__(self, config=None):
        self.zip_compress = ZipCompress(config)
        self.logger = logging.getLogger(__name__)

    def exec(self):
        self.logger.debug("Compress function start executing")
        self.zip_compress.compress_in_tmp_directory()
