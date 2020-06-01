import logging

"""
指定されたファイルをオブジェクトストレージに保存する
 input : 保存するファイルのパス
 output: 保存先のファイルパス
"""


class Store:
    def __init__(self, config=None):
        self.logger = logging.getLogger(__name__)

    def check(self, file):
        self.logger.debug("Compress function start executing")

    def upload(self):
        self.logger.debug("Compress function start executing")
