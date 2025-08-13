import psycopg2
from psycopg2 import pool

class Conexion:
    DATABASE = 'usuarios'
    USERNAME = 'postgres'
    PASSWORD = '1231'
    DB_PORT = '5432'
    HOST = 'localhost'
    MIN_CON = 1
    MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            cls._pool = pool.SimpleConnectionPool(
                cls.MIN_CON,
                cls.MAX_CON,
                database=cls.DATABASE,
                user=cls.USERNAME,
                password=cls.PASSWORD,
                host=cls.HOST,
                port=cls.DB_PORT
            )
        return cls._pool

    @classmethod
    def obtenerConexion(cls):
        return cls.obtenerPool().getconn()

    @classmethod
    def cerrarConexiones(cls):
        if cls._pool:
            cls._pool.closeall()
