class Usuario:
    def __init__(self, id_usuario, username, password):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, valor):
        self._id_usuario = valor

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, valor):
        self._username = valor

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, valor):
        self._password = valor

    def __str__(self):
        return f'Usuario(id_usuario={self.id_usuario}, username="{self.username}", password="{self.password}")'

