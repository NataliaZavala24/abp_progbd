from config.db_config import get_connection
from utils.hash import generar_salt, hashear_contraseña

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Crear tabla
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            contraseña_hash TEXT NOT NULL,
            salt TEXT NOT NULL,
            rol TEXT CHECK(rol IN ('admin', 'usuario')) NOT NULL
        );
    """)

    # Verificar si hay usuarios
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    cantidad = cursor.fetchone()[0]

    if cantidad == 0:
        # Crear admin por defecto
        salt = generar_salt()
        contraseña = "admin123"
        contraseña_hash = hashear_contraseña(contraseña, salt)

        cursor.execute("""
            INSERT INTO usuarios (nombre, username, contraseña_hash, salt, rol)
            VALUES (?, ?, ?, ?, ?)
        """, ("Administrador", "admin", contraseña_hash, salt, "admin"))

        print("✔ Usuario admin creado: usuario='admin', contraseña='admin123'")

    conn.commit()
    conn.close()
