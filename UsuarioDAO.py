from pip._internal.cli.cmdoptions import log
from Usuario import Usuario
# from conexion import Conexion
from logger_base import log
# from cursor_del_pool import CursorDelPool

class UsuarioDAO:
    # """
    # DAO significa: Data Access Object
    # CRUD significa:
    #                 Create -> Insertar
    #                 Read   -> Seleccionar
    #                 Update -> Actualizar
    #                 Delete -> Eliminar
    # """
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(id_usuario, username, password) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET id_usuario=%s, username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    # Definimos los metodos de clase
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = [] # Creamos una lista
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2], registro[3])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario, usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario Insertada: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario, usuario.username, usuario.password)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizada: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores =  (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Los objetos eliminados son: {usuario}')
            return cursor.rowcount