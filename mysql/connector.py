"""
MySQL connection Pool
Use DBUtils to make long connection and auto reconnect
"""

from DBUtils.PooledDB import PooledDB
from collections import ChainMap
import pymysql
from . import settings


class ConnectionPool:

    def __init__(self, creator=None, **kwargs):
        if creator is None:
            creator = pymysql
        kwargs['creator'] = creator
        self._params = ChainMap(kwargs, settings.MYSQL_SETTINGS, settings.POOL_SETTINGS)
        self.pool = None

    def connection(self, shareable=False):
        if self.pool is None:
            self.pool = PooledDB(**self._params)
        return self.pool.connection(shareable=shareable)

    def __call__(self, *args, **kwargs):
        return self.connection(*args, **kwargs)
