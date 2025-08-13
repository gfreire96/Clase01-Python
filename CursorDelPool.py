from Conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = Conexion.obtenerConexion()
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, traceback):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            Conexion.obtenerPool().putconn(self.conn)
