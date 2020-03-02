from unittest import TestCase
from bin.retrieve import Retriever


class TestRetrieve(TestCase):
    def test_failure(self):
        self.fail()

    def test_fail_to_load_database_config(self):
        with self.assertRaises(SystemExit):
            Retriever({})

