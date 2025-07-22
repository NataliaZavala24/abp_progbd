from services.auth_service import login
from services.user_service import registrar_usuario, listar_usuarios, eliminar_usuario, cambiar_rol

def mostrar_menu_principal():
    while True:
        print("\n--- Sistema de Usuarios ---")
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            username = input("Nombre de usuario: ")
            contraseña = input("Contraseña: ")
            usuario = login(username, contraseña)
            if usuario:
                mostrar_menu_usuario(usuario)
            else:
                print("❌ Credenciales incorrectas.")
        elif opcion == "2":
            nombre = input("Nombre completo: ")
            username = input("Nombre de usuario: ")
            contraseña = input("Contraseña: ")
            if registrar_usuario(nombre, username, contraseña, "usuario"):
                print("✅ Usuario registrado correctamente.")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

def mostrar_menu_usuario(usuario):
    if usuario["rol"] == "admin":
        mostrar_menu_admin(usuario)
    else:
        mostrar_menu_estandar(usuario)

def mostrar_menu_estandar(usuario):
    while True:
        print(f"\n--- Bienvenido, {usuario['nombre']} (usuario estándar) ---")
        print("1. Ver mis datos")
        print("2. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"\nID: {usuario['id']}")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Rol: {usuario['rol']}")
        elif opcion == "2":
            break
        else:
            print("Opción inválida.")

def mostrar_menu_admin(usuario):
    while True:
        print(f"\n--- Bienvenido, {usuario['nombre']} (administrador) ---")
        print("1. Ver todos los usuarios")
        print("2. Cambiar rol de un usuario")
        print("3. Eliminar un usuario")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_usuarios()
        elif opcion == "2":
            try:
                id_usuario = int(input("Ingrese el ID del usuario a modificar: "))
                nuevo_rol = input("Nuevo rol ('admin' o 'usuario'): ").strip()
                cambiar_rol(id_usuario, nuevo_rol)
            except ValueError:
                print("ID inválido.")
        elif opcion == "3":
            try:
                id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
                if id_usuario == usuario["id"]:
                    print("❌ No puedes eliminarte a ti mismo.")
                else:
                    eliminar_usuario(id_usuario)
            except ValueError:
                print("ID inválido.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
