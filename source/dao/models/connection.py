# -*- coding: utf-8 -*-

import pymysql.cursors


class DB:
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.db = 'db_mass'
        self.user = 'kleyton'
        self.password = 'kleysql'

    def connect(self):
        conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        conn.autocommit(True)
        return conn


if __name__ == '__main__':
   DB().connect()