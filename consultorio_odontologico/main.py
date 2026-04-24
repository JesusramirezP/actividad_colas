#from typing import List
#from cliente import Cliente
from tarifas import TARIFAS
from usuario import Usuario
from consultorio import Consultorio
from valid_error_handling import validacion_cedula, validacion_nombre, validacion_telefono, validar_opcion_menu, validar_fecha, cant_intervenciones
from display import titulo_a_mostrar, mostrar_menu_principal, titulo_a_mostrar_submenu, mostar_submenu_1, mostar_submenu_2, mostrar_submenu_3

consultorio = Consultorio()

# ──────────────────────────────────────────────
#  FUNCIÓN: Formato para moneda colombiana.
# ──────────────────────────────────────────────

def fmt_cop(valor: int) -> str:      
    return f"${valor:,.0f}".replace(",", ".")


# ──────────────────────────────────────────────
#  FUNCIÓN: Registar cliente    "1"
# ──────────────────────────────────────────────
def registar_usuario():
    titulo_a_mostrar("  NUEVO USUARIO.")                      #Mostrar titulo en terminal desde el modulo display.py
    
    titulo_a_mostrar_submenu("  Datos personales.")           #Mostrar titulo del submenu en terminal desde el modulo display.py
    cedula_usuario = validacion_cedula()                      #Se realiza proceso de captura y validación para el numero de cédula en el modulo "valid_error_handling.py"
    nombre_usuario = validacion_nombre()                      #Se realiza proceso de captura y validación para el nombre en el modulo "valid_error_handling.py"
    telefono_usuario = validacion_telefono()                  #Se realiza proceso de captura y validación para el numero de telefono en el modulo "valid_error_handling.py"
    

    titulo_a_mostrar_submenu("  Tipo de cliente.")            #Mostrar titulo del submenu en terminal desde el modulo display.py
    mostar_submenu_1()                                        #Muestra submenu en el terminal desde el modulo display.py
    tipo_usuario = validar_opcion_menu(["1","2","3"])         #Se realiza proceso de captura  de la opcion del submenu en el modulo "valid_error_handling.py", se reutiliza funcion "validar_opcion_menu" 
    if tipo_usuario == "1":
        tipo_usuario = "Particular"                           #Guarda dato en varible dependiendo del valor de la opcion
    elif tipo_usuario == "2":
        tipo_usuario = "EPS"                                  #Guarda dato en varible dependiendo del valor de la opcion
    elif tipo_usuario == "3":
        tipo_usuario = "Prepagada"                            #Guarda dato en varible dependiendo del valor de la opcion
    

    titulo_a_mostrar_submenu("  Tipo de atención.")                 #Mostrar titulo del submenu en terminal desde el modulo display.py
    mostar_submenu_2()                                              #Muestra submenu en el terminal desde el modulo display.py
    cant_procedimientos = 0                                         #Se inicializan variables
    numero_extracciones = 0                                         #Se inicializan variables
    tipo_atencion = validar_opcion_menu(["1","2","3","4"])          #Se realiza proceso de captura  de la opcion del submenu en el modulo "valid_error_handling.py", se reutiliza funcion "validar_opcion_menu" 
    if tipo_atencion == "1":
        tipo_atencion = "Limpieza"                                  #Guarda dato en varible dependiendo del valor de la opcion
        cant_procedimientos = 1                                     #Guarda dato en varible para que limpieza siempre sea 1

    elif tipo_atencion == "2":            
        tipo_atencion = "Calzas"                                    #Guarda dato en varible dependiendo del valor de la opcion
        cant_procedimientos = cant_intervenciones("calzas")         #Se realiza proceso de captura del numero de calzas en el modulo "valid_error_handling.py", se reutiliza funcion "cant_intervenciones"

    elif tipo_atencion == "3":
        tipo_atencion = "Extracción"                                #Guarda dato en varible dependiendo del valor de la opcion
        cant_procedimientos = cant_intervenciones("extracciones")   #Se realiza proceso de captura del numero de calzas en el modulo "valid_error_handling.py", se reutiliza funcion "cant_intervenciones"
        numero_extracciones = cant_procedimientos                   #Guarda dato en varible auxiliar

    elif tipo_atencion == "4":
        tipo_atencion = "Diagnóstico"                               #Guarda dato en varible dependiendo del valor de la opcion
        cant_procedimientos = 1                                     #Guarda dato en varible para que siempre sea 1 *******


    titulo_a_mostrar_submenu("  Prioridad de atención.")            #Mostrar titulo del submenu en terminal desde el modulo display.py
    mostrar_submenu_3()                                             #Muestra submenu en el terminal desde el modulo display.py
    prioridad_atencion = validar_opcion_menu(["1","2"])             #Se realiza proceso de captura  de la opcion del submenu en el modulo "valid_error_handling.py", se reutiliza funcion "validar_opcion_menu"
  
    
    titulo_a_mostrar_submenu("  Fecha de la cita.")                 #Mostrar titulo del submenu en terminal desde el modulo display.py
    fecha_cita = validar_fecha()                                    #Se realiza proceso de captura de la fecha en el modulo "valid_error_handling.py", en la funcion "validar_fecha"
    
    valor_cita = TARIFAS[tipo_usuario]["cita"]                      #Consulta diccionario para los datosd precios de los diferentes servicios, en el modulo "tarifas.py"
    valor_atencion = TARIFAS[tipo_usuario][tipo_atencion]           #Consulta diccionario para los datosd precios de los diferentes servicios, en el modulo "tarifas.py"
    valor_atencion = valor_atencion * cant_procedimientos           #Calculo del valor de la atención programada
    total_a_pagar = valor_cita + valor_atencion                     #Calculo del valor total para el usuario registrado

    titulo_a_mostrar("  RESUMEN DE PAGO.")                                                  #Mostrar titulo en terminal desde el modulo display.py
    print(f"{'1. Valor cita':<35}: {fmt_cop(valor_cita):>10}")                              #Solo información en terminal de forma tabulada
    print(f"{f'2. Valor atención ({tipo_atencion})':<35}: {fmt_cop(valor_atencion):>10}")   #Solo información en terminal de forma tabulada
    print(f"{'3. TOTAL':<35}: {fmt_cop(total_a_pagar):>10}")                                #Solo información en terminal de forma tabulada

    
    usuario = Usuario()
    usuario.cedula = cedula_usuario
    usuario.nombre = nombre_usuario
    usuario.telefono = telefono_usuario
    usuario.tip_usuario = tipo_usuario
    usuario.tip_atencion = tipo_atencion
    usuario.cantidad = cant_procedimientos
    usuario.prioridad = prioridad_atencion
    usuario.valor_cita = valor_cita
    usuario.valor_atencion = valor_atencion
    usuario.total = total_a_pagar
    usuario.cant_extraccion = numero_extracciones
    consultorio.encolar_usuario(usuario)
   
    return                  

   
    

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
            registar_usuario()
        if opcion == "2":
            consultorio.atender_siguiente_usuario()
        if opcion == "3":
            consultorio.consultar_siguiente_usuario()
        if opcion == "4":
            consultorio.estadistica_de_usuarios()
        if opcion == "5":
            ciclo_menu = False                            #Fin del programa



# ──────────────────────────────────────────────
#  Inicio del programa.
# ──────────────────────────────────────────────
if __name__ == "__main__":
    menu()