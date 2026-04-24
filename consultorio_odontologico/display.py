
# ──────────────────────────────────────────────
#  FUNCIÓN: muestra titulo en terminal
# ──────────────────────────────────────────────

def titulo_a_mostrar(mensaje):
    print("\n" + "═" * 50)                              #Solo información en terminal
    print(mensaje)       #Solo información en terminal
    print("═" * 50)                                     #Solo información en terminal

def mostrar_menu_principal():
    print("  1. Registrar nuevo usuario")               #Solo información en terminal
    print("  2. Atender usuario")                     #Solo información en terminal
    print("  3. Consultar siguiente usuario")           #Solo información en terminal
    print("  4. Ver estadísticas")                      #Solo información en terminal
    print("  5. Salir")                                 #Solo información en terminal
    print("─" * 50) 

def titulo_a_mostrar_submenu(mensaje):
    print("\n")
    print(mensaje)       #Solo información en terminal
    print("═" * 50) 

def mostar_submenu_1():
    print("  1. Particular")    #Solo información en terminal 
    print("  2. EPS")           #Solo información en terminal 
    print("  3. Prepagada")     #Solo información en terminal

def mostar_submenu_2():
    print("  1. Limpieza")              #Solo información en terminal
    print("  2. Calzas")                #Solo información en terminal
    print("  3. Extracción")            #Solo información en terminal
    print("  4. Diagnostico")           #Solo información en terminal

def mostrar_submenu_3():
    print("  1. Normal")                    #Solo información en terminal
    print("  2. Urgente")                   #Solo información en terminal
