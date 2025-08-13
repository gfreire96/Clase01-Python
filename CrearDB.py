from Conexion import Conexion

def crear_tabla_usuario():
    sql = '''
    CREATE TABLE IF NOT EXISTS usuario (
        id_usuario SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL
    );
    '''
    conn = Conexion.obtenerConexion()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
            print("Tabla 'usuario' creada o ya existe.")
    except Exception as e:
        print(f"Error al crear la tabla: {e}")
        conn.rollback()
    finally:
        Conexion.obtenerPool().putconn(conn)

if __name__ == "__main__":
    crear_tabla_usuario()
