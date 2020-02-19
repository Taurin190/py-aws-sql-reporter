from sql.sql_handler import SQLHandler
from unittest import TestCase


class TestSQLHandler(TestCase):
    def test_get_all_files(self):
        config = {"sql_path": "./sql"}
        self.driver = SQLHandler(config)
        actual = self.driver.get_all_files()
        self.assertEqual(["test1.sql", "test2.sql"], actual)
