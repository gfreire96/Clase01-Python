from Usuario import Usuario
from UsuarioDAO import UsuarioDAO

class MenuAppUsuario:
    @staticmethod
    def mostrar_menu():
        print("\n--- Menú de Usuarios ---")
        print("1. Listar usuarios")
        print("2. Agregar usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

    @staticmethod
    def ejecutar():
        while True:
            MenuAppUsuario.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                usuarios = UsuarioDAO.seleccionar()
                for usuario in usuarios:
                    print(usuario)
            elif opcion == "2":
                username = input("Ingrese el nombre de usuario: ")
                password = input("Ingrese la contraseña: ")
                usuario = Usuario(None, username, password)
                resultado = UsuarioDAO.insertar(usuario)
                if resultado == 1:
                    print("Usuario agregado correctamente.")
                else:
                    print("No se pudo agregar el usuario.")
            elif opcion == "3":
                id_usuario = int(input("Ingrese el ID del usuario a actualizar: "))
                username = input("Nuevo nombre de usuario: ")
                password = input("Nueva contraseña: ")
                usuario = Usuario(id_usuario, username, password)
                UsuarioDAO.actualizar(usuario)
                print("Usuario actualizado.")
            elif opcion == "4":
                id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
                usuario = Usuario(id_usuario, None, None)
                UsuarioDAO.eliminar(usuario)
                print("Usuario eliminado.")
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
