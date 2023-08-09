from enum import Enum
from typing import Union, Optional

from pythonate.internal import MissingSupportError
from pythonate.system import os

has_db_support: bool = False
try:
    import sqlite3  # type: ignore
    import mysql.connector  # type: ignore
    import pymssql  # type: ignore

    has_db_support = True
except ImportError:
    has_db_support = False


class SQLType(Enum):
    """
    SQL Type Enum
    """
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
        """
        Initialize the SQL class.
        :param sql_type: SQL type.
        :type sql_type: SQLType
        :param server_ip: Server IP address (needed if using MYSQL or MS_SQL).
        :type server_ip: str, optional
        :param database_name: Database name (needed if using MYSQL or MS_SQL).
        :type database_name: str, optional
        :param username: Username (needed if using MYSQL or MS_SQL and not using Active Directory).
        :type username: str, optional
        :param password: Password (needed if using MYSQL or MS_SQL and not using Active Directory).
        :type password: str, optional
        :param use_active_directory: Use Active Directory (needed if using MYSQL or MS_SQL and not using username/password).
        :type use_active_directory: bool, optional
        :param sqlite_file: SQLite file (needed if using SQLITE).
        :type sqlite_file: str, optional
        :param encryption_key: Encryption key (needed if using SQL_CIPHER).
        :type encryption_key: str, optional
        """
        if not has_db_support:
            raise MissingSupportError(extension="db")

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
                db = pymssql.connect(server=self.SERVER_IP, database=self.DATABASE_NAME, user=self.USERNAME,
                                     password=self.PASSWORD)
        return db

    def use_sql_locally(self):
        """
        Pass SQL instance over.
        :return: SQL connection
        """
        return self._get_connection()

    def custom_query(self,
                     queries: [],
                     commit: bool = False) \
            -> Union[list, None, list[Optional[dict]], list[Optional[tuple]], list[None]]:
        """
        Execute a custom query.
        :param queries: List of queries to execute.
        :param commit: Commit the query.
        :return: Result of the query.
        """
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
