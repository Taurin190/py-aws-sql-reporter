from sql.sql_handler import SQLHandler
from unittest import TestCase


class TestSQLHandler(TestCase):
    def test_get_all_files(self):
        config = {"sql_path": "./sql"}
        self.driver = SQLHandler(config)
        actual = self.driver.get_all_files()
        self.assertEqual(["test1.sql", "test2.sql"], actual)

    def test_exist_sql_file_exist(self):
        config = {"sql_path": "./sql"}
        self.driver = SQLHandler(config)
        actual = self.driver.exist_sql_file("test1.sql")
        self.assertTrue(actual)

    def test_exist_sql_file_not_exist(self):
        config = {"sql_path": "./sql"}
        self.driver = SQLHandler(config)
        actual = self.driver.exist_sql_file("test3.sql")
        self.assertFalse(actual)

