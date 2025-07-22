from database.init_db import initialize_db
from ui.menu import mostrar_menu_principal

if __name__ == "__main__":
    initialize_db()
    mostrar_menu_principal()
