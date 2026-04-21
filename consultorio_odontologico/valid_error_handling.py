

def Validacion_cedula():
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

        return int(cedula)                                                  #Retorna con el numero capturado de la cedula