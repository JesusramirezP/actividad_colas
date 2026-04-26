"""
    Aplicación para consultorio odontologico.
    Version v2.

    Que incluye;
        - Variables
            - input
            - output
            - Tipos de variables:
                - String (str) cadena de texto o cadena de caracteres.
                - Numericas (int): 
                - Boolean (bool): True or False
                - Casse
                - Objeto: Tipos personalizados
                - lista
                - Colas
        - Operadores
            - + : suma
        - Modulos
        - Funciones

    Problemas (BUGS) que se encontraron y se corrigieron.
        1. Valida que el numero de cedula no sea vacío.
        2. Valida que el numero de cedula sea numérico.     "Manejo de errores"
        3. Valida que el numero de cedula no tenga mas de 10 caracteres.

        4. Valida que el nombre del cliente no sea vacío.
        5. Valida que el nombre del cliente solo tenga letras.
        6. Valida que el numbre del cliente no tenga mas de 22 caracteres.

        7. Valida que el numero de telefono no sea vacío.
        8. Valida que el numero de telefono sea numérico.   "Manejo de errores"
        9. Valida que el numero de telefono no tenga mas de 15 caracteres.

        10. Valida que la fecha de la cita no este vacia.
        11. Valida que la fecha de la cita tenga el formato DD/MM/AAAA.  "Manejo de errores"
        12. "Manejo de errores"alida que la fecha tenga valores exagerados en dia y mes.     "Manejo de errores"

        13. Valida que al ingresar las opciones al menu no esten vacias y concuerden con la longitud del menu.
        14. Valida que sean numeros dentro de la longitud del menu.

        15. Valida que la cantidad de calzas y extracciones no sea vacia.
        16. Valida que la cantidad de calzas y extraciones no supere las 32 piezas dentales.
        17. valida que el numero de calzas y extracciones sea numerico. "Manejo de errores"

"""

from tarifas import TARIFAS
from usuario import Usuario
from consultorio import Consultorio
from valid_error_handling import validacion_cedula, validacion_nombre, validacion_telefono, validar_opcion_menu, validar_fecha, cant_intervenciones
from display import titulo_a_mostrar, mostrar_menu_principal, titulo_a_mostrar_submenu, mostar_submenu_1, mostar_submenu_2, mostrar_submenu_3, fmt_cop, mostar_submenu_4

consultorio = Consultorio()             #Inicializa Consultorio()


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

    
    usuario = Usuario()                                         #Se crea usuario
    usuario.cedula = cedula_usuario                             #Se guardan atrubutos del usuario
    usuario.nombre = nombre_usuario                             #
    usuario.telefono = telefono_usuario                         #
    usuario.tip_usuario = tipo_usuario                          #
    usuario.tip_atencion = tipo_atencion                        #
    usuario.cantidad = cant_procedimientos                      #
    usuario.prioridad = prioridad_atencion                      #
    usuario.fecha = fecha_cita                                  #
    usuario.valor_cita = valor_cita                             #
    usuario.valor_atencion = valor_atencion                     #
    usuario.total = total_a_pagar                               #
    usuario.cant_extraccion = numero_extracciones               #
    consultorio.encolar_usuario(usuario)                        #Va a la funcion usuario en la funcion "encolar_usuario" en el modulo consultorio.py
    return                                                      #Retorna al menu


def atender_usuario():
    titulo_a_mostrar("  ATENDER USUARIO.")                      #Mostrar titulo en terminal desde el modulo display.py
   
    titulo_a_mostrar_submenu("  Opción a atender.")             #Mostrar titulo del submenu en terminal desde el modulo display.py
    mostar_submenu_4()                                          #Muestra submenu en el terminal desde el modulo display.py
    atender = validar_opcion_menu(["1","2","3"])                #Se realiza proceso de captura  de la opcion del submenu en el modulo "valid_error_handling.py", se reutiliza funcion "validar_opcion_menu" 
    if atender == "1":
        consultorio.atender_usuario_urgente()                   #
    elif atender == "2":
        consultorio.atender_usuario_extraccion()                               
    elif atender == "3":
        consultorio.atender_usuario_general()


def consultar_usuario():
    titulo_a_mostrar("  CONSULTAR USUARIO.")                    #Mostrar titulo en terminal desde el modulo display.py
   
    titulo_a_mostrar_submenu("  Opción a consultar.")           #Mostrar titulo del submenu en terminal desde el modulo display.py
    mostar_submenu_4()                                          #Muestra submenu en el terminal desde el modulo display.py
    consultar = validar_opcion_menu(["1","2","3"])              #Se realiza proceso de captura  de la opcion del submenu en el modulo "valid_error_handling.py", se reutiliza funcion "validar_opcion_menu" 
    if consultar == "1":                                        
        consultorio.consultar_siguiente_usuario_urgente()       
    elif consultar == "2":
        consultorio.consultar_siguiente_usuario_extraccion()                               
    elif consultar == "3":
        consultorio.consultar_siguiente_usuario_general()

# ──────────────────────────────────────────────
#  FUNCIÓN: menu
# ──────────────────────────────────────────────
def menu():
    

    ciclo_menu = True                                       
    while ciclo_menu == True: 
        titulo_a_mostrar("  CONSULTORIO ODONTOLÓGICO — Dr. AAA")    #Mostrar aviso del consultorio en terminal desde el modulo display.py
        mostrar_menu_principal()                                    #Mostrar menu principal en el terminal desde el modulo display.py
        
        opcion = input("Ingrese una oipción: ")                     #Captura dato para seleccionar la opcion a trabajar
        if opcion == "1":                                           #Se verifica si es la opcion 1
            registar_usuario()                                      #Va a la funcion "egistrar_usuario" la cual esta dentro de este modulo main.py
        if opcion == "2":                                           #Se verifica si es la opcion 2
            consultorio.mostrar_usuarios_pendientes_ordenados()     #Va a la funcion "mostrar_usuarios_pendientes_ordenados" la cual esta dentro del modulo consultorio.py
        if opcion == "3":                                           #Se verifica si es la opcion 2
            atender_usuario()                                       #Va a la funcion "atender_usuario" la cual esta dentro del modulo main.py
        if opcion == "4":                                           #Se verifica si es la opcion 2
            consultar_usuario()                                     #Va a la funcion "consultar_siguiente_usuario" la cual esta dentro del modulo consultorio.py
        if opcion == "5":                                           #Se verifica si es la opcion 2
            consultorio.estadistica_de_usuarios()                   #Va a la funcion "estadistica_de_usuarios" la cual esta dentro del modulo consultorio.py
        if opcion == "6":                                           #Se verifica si es la opcion 2
            ciclo_menu = False                                      #Fin del programa



# ──────────────────────────────────────────────
#  Inicio del programa.
# ──────────────────────────────────────────────
if __name__ == "__main__":
    menu()