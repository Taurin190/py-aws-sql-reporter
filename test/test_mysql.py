from database.mysql import MySQL
from unittest import TestCase


class TestMySQL(TestCase):
    def setUp(self):
        config = {
            "hostname": "127.0.0.1",
            "user": "root",
            "password": "password",
            "gateway": "forge",
        }
        self.driver = MySQL(config)

    def test_get_from_sql(self):
        actual_header, actual = self.driver.get_from_sql("select id, name from users")
        self.assertEqual("id", actual_header[0][0])
        self.assertEqual("name", actual_header[1][0])
        self.assertEqual((((1, 'test'),)), actual)
