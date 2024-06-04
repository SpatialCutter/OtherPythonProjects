import sqlite3
import time
import math
import re

class Database:
    def __init__(self, filename):
        self.__connection = sqlite3.connect(filename)
        self.__cur = self.__connection.cursor()

    def SelectAll(self, table):
        sql = "SELECT * FROM {0}".format(table)
        try:
            res = self.__cur.execute(sql).fetchall()
            if res:
                return res
        except:
            print("Ошибка чтения из БД")
        return []

    def DeleteAll(self, table):
        sql = "DELETE FROM {0}".format(table)
        try:
            self.__cur.execute(sql)
            self.__connection.commit()
        except:
            print("Ошибка удаления из БД")

    def SelectByID(self, table, id):
        sql = "SELECT * FROM {0} WHERE ID == {1}".format(table, id)
        try:
            res = self.__cur.execute(sql).fetchall()
            if res:
                return res
        except:
            print("Ошибка чтения из БД")
        return []

    def SelectByColumn(self, table, colname, colvalue):
        sql = "SELECT * FROM {0} WHERE {1} == \"{2}\"".format(table, colname, colvalue)
        try:
            res = self.__cur.execute(sql).fetchall()
            if res:
                return res
        except:
            print("Ошибка чтения из БД")
        return []

    def Add(self, table, datastr):
        sql = "INSERT INTO {0} VALUES ({1})".format(table, datastr)
        try:
            self.__cur.execute(sql)
            self.__connection.commit()
        except:
            print("Ошибка записи в БД")

    def CloseConnection(self):
        self.__connection.close()
