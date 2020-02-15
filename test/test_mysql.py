from database.mysql import MySQL
from unittest import TestCase


class TestMySQL(TestCase):
    def setUp(self):
        config = {
            "hostname": "127.0.0.1",
            "user": "root",
            "password": "password",
            "database": "forge",
        }
        self.driver = MySQL(config)

    def test_get_from_sql(self):
        actual = self.driver.get_from_sql("select id, name from users")
        self.assertEqual(actual, ((1, 'test'),))
