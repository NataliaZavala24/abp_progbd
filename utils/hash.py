import hashlib
import os

def generar_salt():
    return os.urandom(16).hex()  # 16 bytes aleatorios como string hexadecimal

def hashear_contraseña(contraseña, salt):
    """Devuelve hash hexadecimal usando SHA-256 con salt"""
    return hashlib.sha256((salt + contraseña).encode('utf-8')).hexdigest()
