from config.db_config import get_connection
from utils.hash import generar_salt, hashear_contraseña
from utils.validators import validar_contraseña

def registrar_usuario(nombre, username, contraseña, rol):
    if not validar_contraseña(contraseña):
        print("La contraseña debe tener mínimo 6 caracteres y contener letras y números.")
        return False

    salt = generar_salt()
    contraseña_hash = hashear_contraseña(contraseña, salt)

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nombre, username, contraseña_hash, salt, rol)
            VALUES (?, ?, ?, ?, ?)""",
            (nombre, username, contraseña_hash, salt, rol))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al registrar: {e}")
        return False
    finally:
        conn.close()

def listar_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, username, rol FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()

    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("\n--- Lista de usuarios ---")
        for u in usuarios:
            print(f"ID: {u[0]}, Nombre: {u[1]}, Usuario: {u[2]}, Rol: {u[3]}")

def eliminar_usuario(usuario_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Usuario eliminado correctamente.")
    else:
        print("No se encontró un usuario con ese ID.")
    conn.close()

def cambiar_rol(usuario_id, nuevo_rol):
    if nuevo_rol not in ['admin', 'usuario']:
        print("Rol inválido. Solo se permite 'admin' o 'usuario'.")
        return

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET rol = ? WHERE id = ?", (nuevo_rol, usuario_id))
    conn.commit()
    if cursor.rowcount > 0:
        print("Rol actualizado correctamente.")
    else:
        print("No se encontró un usuario con ese ID.")
    conn.close()
