from CursorDelPool import CursorDelPool
from Usuario import Usuario
from logger_base import log

class UsuarioDAO:
    # DAO significa: Data Access Object
    # CRUD significa:
    #   Create -> Insertar
    #   Read   -> Seleccionar
    #   Update -> Actualizar
    #   Delete -> Eliminar

    _SELECCIONAR = 'SELECT id_usuario, username, password FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            log.info(f'Selección de usuarios: {usuarios}')
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            cursor.connection.commit()  # <-- Agrega esto
            log.info(f'Usuario insertado: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            cursor.connection.commit()  # <-- Agrega esto
            log.info(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            cursor.connection.commit()  # <-- Agrega esto
            log.info(f'Usuario eliminado: {usuario}')
            return cursor.rowcount
