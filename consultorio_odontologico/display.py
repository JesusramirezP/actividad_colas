""" 
    Modulo solo para imprimir mensajes y dar formato a los valores 
    numericos a formato de moneda colombiana.
    
"""


# ──────────────────────────────────────────────
#  FUNCIÓN: Formato para moneda colombiana.
# ──────────────────────────────────────────────

def fmt_cop(valor: int) -> str:                         #Funcion para dar formato a los valores de dinero
    return f"${valor:,.0f}".replace(",", ".")           #Ajusta el valor numerico para formato de moneda colombiana COP

# ──────────────────────────────────────────────
#  FUNCIÓN: muestra titulo en terminal
# ──────────────────────────────────────────────

def titulo_a_mostrar(mensaje):
    print("\n" + "═" * 50)                              #Solo información en terminal
    print(mensaje)       #Solo información en terminal
    print("═" * 50)                                     #Solo información en terminal

def mostrar_menu_principal():
    print("  1. Registrar nuevo usuario")               #Solo información en terminal
    print("  2. Ver lista de usuarios")                 #Solo información en terminal
    print("  3. Atender usuario")                      #Solo información en terminal
    print("  4. Consultar siguiente usuario")           #Solo información en terminal
    print("  5. Ver estadísticas")                      #Solo información en terminal
    print("  6. Salir")                                 #Solo información en terminal
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

def mostar_submenu_4():
    print("  1. Urgente")                #Solo información en terminal 
    print("  2. Extracciones")           #Solo información en terminal 
    print("  3. General")                #Solo información en terminal
