import re

def validar_contraseña(contraseña):
    return len(contraseña) >= 6 and bool(re.search(r"[A-Za-z]", contraseña)) and bool(re.search(r"\d", contraseña))
