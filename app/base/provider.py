import psycopg2
from psycopg2.extras import RealDictCursor
import os
from config import DATABASE, SQL_ROOT_PATH


class BaseProvider:
    def __init__(self, module_sql_path=''):
        self.connect, self.cursor = self._connect()
        self.sql_root = os.path.join(SQL_ROOT_PATH, module_sql_path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.close()
        self.cursor.close()

    @staticmethod
    def import_sql(sql_root, name):
        with open(os.path.join(sql_root, name), encoding='utf-8', mode='r') as _fne:
            return _fne.read()

    def exec_by_file(self, name, params=None):
        query = self.import_sql(self.sql_root, name)
        return self._execute(query, None or params)

    @staticmethod
    def _connect():
        """
        Метод подключения к бд
        :return:
        """
        config_connect = "dbname='{dbname}' user='{user}' host='{host}' password='{password}' port='{port}'"
        connect = psycopg2.connect(config_connect.format(**DATABASE))
        return connect, connect.cursor(cursor_factory=RealDictCursor)

    def _execute(self, query, params):
        if isinstance(params, str) or isinstance(params, int):
            params = (params,)

        response = None
        try:
            self.cursor.execute(query, params)
            self.connect.commit()
        except psycopg2.Error as e:
            print(e.pgerror)
            print(e.diag.message_primary)
        finally:
            try:
                response = self.cursor.fetchall()
            except:
                pass
        return response