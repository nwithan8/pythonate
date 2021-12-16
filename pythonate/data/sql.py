from enum import Enum

import sqlite3
import mysql.connector

from pythonate.system import os


class SQLType(Enum):
    SQLITE = 1,
    MYSQL = 2,
    MS_SQL = 3


class SQL:
    def __init__(self,
                 sql_type: SQLType,
                 server_ip: str = None,
                 database_name: str = None,
                 username: str = None,
                 password: str = None,
                 use_active_directory: bool = False,
                 sqlite_file: str = None,
                 encryption_key: str = None):
        self.SQL_TYPE = sql_type
        self.SERVER_IP = server_ip
        self.DATABASE_NAME = database_name
        self.USERNAME = username
        self.PASSWORD = password
        self.USE_ACTIVE_DIRECTORY = use_active_directory
        self.SQLITE_FILE = sqlite_file
        self.KEY = encryption_key
        self._requirements_check()

    def _requirements_check(self):
        if self.SQL_TYPE not in [SQLType.SQLITE, SQLType.MYSQL, SQLType.MS_SQL]:
            raise Exception("Not a valid sql_type.")
        if self.SQL_TYPE in [SQLType.SQLITE]:
            if not self.SQLITE_FILE:
                raise Exception("Please provide an SQLite or SQLCipher file.")
        if self.SQL_TYPE in [SQLType.MYSQL, SQLType.MS_SQL]:
            if not (self.SERVER_IP and self.DATABASE_NAME):
                raise Exception("Please provide a server IP address and a database name.")
        if self.SQL_TYPE == SQLType.MYSQL:
            if not (self.USERNAME and self.PASSWORD):
                raise Exception("Please provide a username and password.")
        if self.SQL_TYPE == SQLType.MS_SQL:
            if not os.get_os() == os.OS.WINDOWS:
                raise Exception("MSSQL is only available on Windows.")
            if not ((self.USERNAME and self.PASSWORD) or self.USE_ACTIVE_DIRECTORY):
                raise Exception("Please use either username/password or Active Directory.")

    def _get_connection(self):
        db = None
        if self.SQL_TYPE == SQLType.SQLITE:
            db = sqlite3.connect(self.SQLITE_FILE)
        elif self.SQL_TYPE == SQLType.MYSQL:
            db = mysql.connector.connect(user=self.USERNAME, password=self.PASSWORD, host=self.SERVER_IP,
                                         database=self.DATABASE_NAME)
        elif self.SQL_TYPE == SQLType.MS_SQL:
            if os.get_os() == os.OS.WINDOWS:
                import pyodbc
                db = pyodbc.connect(f'DRIVER={{/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.5.so.2.1}};'
                                    f'SERVER={self.SERVER_IP};'
                                    f'DATABASE={self.DATABASE_NAME};'
                                    f'UID={self.USERNAME};'
                                    f'PWD={self.PASSWORD}')
        return db

    def use_sql_locally(self):
        """
        Pass SQL instance over.
        :return:
        """
        return self._get_connection()

    def custom_query(self,
                     queries: [],
                     commit: bool = False):
        conn = self._get_connection()
        if conn:
            cur = conn.cursor()
            for query in queries:
                cur.execute(query)
            results = cur.fetchall()
            if commit:
                results = cur.rowcount
                conn.commit()
            cur.close()
            conn.close()
            return results
        else:
            raise Exception("Couldn't connect to the database.")
