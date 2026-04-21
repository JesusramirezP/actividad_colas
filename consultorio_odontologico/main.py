#from typing import List
#from cliente import Cliente
#from tarifas import TARIFAS
from valid_error_handling import Validacion_cedula
from display import titulo_a_mostrar, mostrar_menu_principal,titulo_a_mostrar_submenu


# ──────────────────────────────────────────────
#  FUNCIÓN: Registar cliente    "1"
# ──────────────────────────────────────────────
def registar_cliente():
    titulo_a_mostrar("  NUEVO CLIENTE.")    #Mostrar titulo en terminal desde el modulo display.py
    titulo_a_mostrar_submenu("  Datos personales.")    #Mostrar titulo del submenu en terminal desde el modulo display.py
    cedula_cliente = Validacion_cedula()    #Se realiza proceso de captura y validación para el numero de cédula en el modulo "valid_error_handling.py"
    print(f"{cedula_cliente}")
    return                  

    #cedula_cliente = Validacion_cedula()    #Se realiza proceso de captura y validación para el numero de cédula en el modulo "valid_error_handling.py"
    





# ──────────────────────────────────────────────
#  FUNCIÓN: menu
# ──────────────────────────────────────────────
def menu():
    ciclo_menu = True                                       
    while ciclo_menu == True: 
        titulo_a_mostrar("  CONSULTORIO ODONTOLÓGICO — Dr. AAA")    #Mostrar aviso del consultorio en terminal desde el modulo display.py
        mostrar_menu_principal()                                    #Mostrar menu principal en el terminal desde el modulo display.py
        
        opcion = input("Ingrese una oipción: ")                     #Captura dato para seleccionar la opcion a trabajar
        if opcion == "1":
            registar_cliente()
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