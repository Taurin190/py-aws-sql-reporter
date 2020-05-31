from gateway.db import DB
import mysql.connector


class MySQL(DB):
    def __init__(self, config):
        self.connection = mysql.connector.connect(
            host=config['hostname'],
            user=config['user'],
            passwd=config['password'],
            db=config['database'])
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def get_from_sql(self, sql):
        self.cursor.execute(sql)
        return self.cursor.description, self.cursor.fetchall()
