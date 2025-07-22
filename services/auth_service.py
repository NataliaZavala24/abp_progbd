from config.db_config import get_connection
from utils.hash import hashear_contraseña

def login(username, contraseña_input):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre, contraseña_hash, salt, rol FROM usuarios WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    if row:
        user_id, nombre, stored_hash, salt, rol = row
        hash_input = hashear_contraseña(contraseña_input, salt)
        if hash_input == stored_hash:
            return {"id": user_id, "nombre": nombre, "rol": rol}
    return None
