






# ──────────────────────────────────────────────
#  FUNCIÓN: menu
# ──────────────────────────────────────────────
def menu():
    ciclo_menu = True                                       
    while ciclo_menu == True:                               #Solo información en terminal
        print("\n" + "═" * 50)                              #Solo información en terminal
        print("  CONSULTORIO ODONTOLÓGICO — Dr. AAA")       #Solo información en terminal
        print("═" * 50)                                     #Solo información en terminal
        print("  1. Registrar nuevo cliente")               #Solo información en terminal
        #print("  2. Lista de clientes")                     #Solo información en terminal
        #print("  3. Buscar cliente")                        #Solo información en terminal
        #print("  4. Ver estadísticas")                      #Solo información en terminal
        print("  5. Salir")                                 #Solo información en terminal
        print("─" * 50)                                     #Solo información en terminal
        opcion = input("Ingrese una oipción: ")             #Captura dato para seleccionar la opcion a trabajar
        #if opcion == "1":
         #   registar_cliente()
        #if opcion == "2":
         #   mostrar_cliente()
        #if opcion == "3":
         #   buscar_cliente()
        #if opcion == "4":
         #   estadisticas()
        if opcion == "5":
            ciclo_menu = False                            #Fin del programa



# ──────────────────────────────────────────────
#  Inicio del programa.
# ──────────────────────────────────────────────
if __name__ == "__main__":
    menu()