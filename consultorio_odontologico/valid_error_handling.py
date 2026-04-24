from datetime import datetime

def validacion_cedula():
    while True:
        cedula = input("Ingrese el número de cédula: ").strip()             #Se captura el dato de la cedula y con el metodo .strip() se eliminan espacios al inicio o al final de la cadena de caracteres

        if not cedula:                                                      #Verifica que el valor de la cedula no este vacio
            print("ERROR: El campo de cédula no puede estar vacío.")        #Muestra aviso en terminal
            continue                                                        #Salto para repetir nuevamente el ciclo while

        if not cedula.isdigit():                                            #Verifica que el valor ingresado sea solo numeros, usando el metodo ..isdigit()
            print("ERROR: Ingrese solo números.")                           #Muestra aviso en terminal
            continue                                                        #Salto para repetir nuevamente el ciclo while

        if len(cedula) > 10:                                                #Verifica que la longitud de la cedula no sea mayor a 10 caracteres
            print("ERROR: No puede tener más de 10 caracteres.")            #Muestra aviso en terminal
            continue                                                        #Salto para repetir nuevamente el ciclo while

        if int(cedula) <= 0:                                                #Verifica que el numero de cedula no sea un valor negativo
            print("ERROR: Debe ser un número positivo.")                    #Muestra aviso en terminal
            continue                                                        #Salto para repetir nuevamente el ciclo while

        return int(cedula)                                                  #Retorna con el numero de cedula
    

def validacion_nombre():
    while True:
        nombre = input("Ingrese nombre del cliente: ").strip()              #Se captura el nombre del usuario y con el metodo .strip() se eliminan espacios al inicio o al final de la cadena de caracteres
        if not nombre:                                                      #Verifica que el dato de nombre no este vacio
            print("ERROR: El campo no puede estar vacío.")                  #Muestra aviso en terminal
            continue                                                        #Salto para repetir nuevamente el ciclo while

        if len(nombre) > 22:                                                #Verifica que la longitud del nombre no sea mayor a 22 caracteres
            print("ERROR: No puede tener más de 22 caracteres.")            #Muestra aviso en terminal
            continue                                                        #Salto para repetir nuevamente el ciclo while

        if not nombre.replace(" ", "").isalpha():                           #Verifica que el nombre ingresado sea solo letras, usando el metodo ..isdigit()
            print("ERROR: Ingrese solo letras y espacios.")                 #Muestra aviso en terminal
            continue                                                        #Salto para repetir nuevamente el ciclo while

        return nombre                                                       #Retorna con el nombre de usuario
    
def validacion_telefono():
    while True:
        telefono = input("Ingrese el número de telefono: ").strip()         #Se captura el dato de la cedula y con el metodo .strip() se eliminan espacios al inicio o al final de la cadena de caracteres

        if not telefono:                                                    #Verifica que el valor de la cedula no este vacio
            print("ERROR: El campo de telefono no puede estar vacío.")      #Muestra aviso en terminal
            continue                                                        #Salto para repetir nuevamente el ciclo while

        if not telefono.isdigit():                                          #Verifica que el valor ingresado sea solo numeros, usando el metodo ..isdigit()
            print("ERROR: Ingrese solo números.")                           #Muestra aviso en terminal
            continue                                                        #Salto para repetir nuevamente el ciclo while

        if len(telefono) > 10:                                              #Verifica que la longitud de la cedula no sea mayor a 10 caracteres
            print("ERROR: No puede tener más de 10 caracteres.")            #Muestra aviso en terminal
            continue                                                        #Salto para repetir nuevamente el ciclo while

        if int(telefono) <= 0:                                              #Verifica que el numero de cedula no sea un valor negativo
            print("ERROR: Debe ser un número positivo.")                    #Muestra aviso en terminal
            continue                                                        #Salto para repetir nuevamente el ciclo while

        return int(telefono)                                                #Retorna con el numero de telefono



def validar_opcion_menu(opciones_validas):                                  #Funcion reutilizable
    while True: 
        opcion = input("Ingrese una opción: ")                              #Se imprime el mensaje y se captura el dato 
        if opcion in opciones_validas:                                      #Se valida si de las opciones cargadas inicialmente, una de ellas es verdadera
            return opcion                                                   #Retorna con la opcion seleccionada
        print("Opción inválida")                                            #Si la vlidacion no concuerda con una de las opciones cargadas inicialmente, muestra mensaje de opcion invalida

        

def validar_fecha():
    while True:
        fecha = input("Ingrese fecha de la cita (DD/MM/AAAA): ")            #Se imprime mensaje y se captura dato de la fecha 
        try:                                                                #Se va intentar procesar algo donde podria fallar, esto es para garantizar el dato correcto y el control de errores que puede afectar la aplicación
            datetime.strptime(fecha, "%d/%m/%Y")                            #Se valida que sean valores reales de fecha y formato por medio de la instriccion de importacion de python "from datetime import datetime"
            return fecha                                                    #Si la fecha es correcta retorna con el dato de la fecha
        except ValueError:                                                  #Se genera error cuando el dato ingresado no esta dentro de los parametros establecidos
            print("ERROR: Fecha inválida. Use DD/MM/AAAA")                  #Se imprime el mensaje en el terminal


def cant_intervenciones(mensaje):                                           #Funcion reutilizable
    while True:
        entrada = input(f"Ingrese cantidad de {mensaje} >0: ").strip()      #Se imprime el mensaje, se captura el dato y con el metodo .strip() se eliminan espacios al inicio o al final de la cadena de caracteres
        if not entrada:                                                     #Verifica que el valor no este vacio
            print("Debe ingresar un valor")                                 #Imprimer el mensaje en el terminal
            continue                                                        #Salto para repetir nuevamente el ciclo while

        try:                                                                #Se va intentar procesar algo donde podria fallar, esto es para garantizar el dato correcto y el control de errores que puede afectar la aplicación
            valor = int(entrada)                                            #Convierte lo que tiena "valor" en un numero entero
        except ValueError:                                                  #Si no se puede convertir el valor, genera una excepcion para evitar un error en el sistema
            print("ERROR: Solo se permiten números enteros")                #Imprime mensaje en el terminal
            continue                                                        #Salto para repetir nuevamente el ciclo while

        if valor <= 0:                                                      #Se verifica que el valor no sea cero y tampoco un valor negativo
            print(f"ERROR: El número ingresado no es valido")               #Imprime mensaje en el terminal
            continue                                                        #Salto para repetir nuevamente el ciclo while

        if valor > 32:                                                              #Verifica que el numero no supere la cantidad de piezas dentales de un adulto
            print(f"ERROR: El número ingresado supera las 32 piezas dentales")      #Imprime mensaje en el terminal
            continue                                                                #Salto para repetir nuevamente el ciclo while

        return valor                                                        #Retorna valor de piezas dentales a intervenir
        