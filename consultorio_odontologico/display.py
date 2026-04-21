
# ──────────────────────────────────────────────
#  FUNCIÓN: muestra titulo en terminal
# ──────────────────────────────────────────────

def titulo_a_mostrar(mensaje):
    print("\n" + "═" * 50)                              #Solo información en terminal
    print(mensaje)       #Solo información en terminal
    print("═" * 50)                                     #Solo información en terminal

def mostrar_menu_principal():
    print("  1. Registrar nuevo cliente")               #Solo información en terminal
    print("  2. Lista de clientes")                     #Solo información en terminal
    print("  3. Buscar cliente")                        #Solo información en terminal
    print("  4. Ver estadísticas")                      #Solo información en terminal
    print("  5. Salir")                                 #Solo información en terminal
    print("─" * 50) 

def titulo_a_mostrar_submenu(mensaje):
    print(mensaje)       #Solo información en terminal
    print("═" * 50) 