from collections import deque
from usuario import Usuario
from display import fmt_cop, titulo_a_mostrar
from datetime import datetime

class Consultorio:                          #Se crea la clase Consultorio (el molde)
    nombre: str = ''                        #Se inicializa

    # Colas de atencion urgente
    cola_urgente_particular = deque()
    cola_urgente_eps = deque()
    cola_urgente_prepagada = deque()
    
    # Colas de atencion normales
    cola_normal_particular = deque()
    cola_normal_eps = deque()
    cola_normal_prepagada = deque()

    #Punteros
    colas_urgentes_cont = 0
    colas_normales_cont = 0

    #Booleans
    grup_urgentes = True
    grup_normales = False

    def encolar_usuario(self, usuario:Usuario):                         
        if usuario.prioridad == "2":                                #Se verifica se la prioridad del usuario es urgente(2)
            if usuario.tip_usuario == "Particular":                 #Dentro de la prioridad urgente se verifica a que tipo de usuario pertenese
                self.cola_urgente_particular.append(usuario)        #Se agrega usuario a la cola
            elif usuario.tip_usuario == "EPS":                      #Dentro de la prioridad urgente se verifica a que tipo de usuario pertenese
                self.cola_urgente_eps.append(usuario)               #Se agrega usuario a la cola
            elif usuario.tip_usuario == "Prepagada":                #Dentro de la prioridad urgente se verifica a que tipo de usuario pertenese
                self.cola_urgente_prepagada.append(usuario)         #Se agrega usuario a la cola

        elif usuario.prioridad == "1":                              #Se verifica se la prioridad del usuario es normal (1)
            if usuario.tip_usuario == "Particular":                 #Dentro de la prioridad normal se verifica a que tipo de usuario pertenese
                self.cola_normal_particular.append(usuario)         #Se agrega usuario a la cola
            elif usuario.tip_usuario == "EPS":                      #Dentro de la prioridad normal se verifica a que tipo de usuario pertenese
                self.cola_normal_eps.append(usuario)                #Se agrega usuario a la cola
            elif usuario.tip_usuario == "Prepagada":                #Dentro de la prioridad normal se verifica a que tipo de usuario pertenese
                self.cola_normal_prepagada.append(usuario)          #Se agrega usuario a la cola
        

    def mostrar_usuarios_pendientes_ordenados(self):
        titulo_a_mostrar("  LISTA DE USUARIOS.")                    #Muestrar titulo en terminal desde el modulo display.py  

        #Agrupa las colas de usuarios con prioridad urgente
        colas_urgentes = [
            self.cola_urgente_particular,
            self.cola_urgente_prepagada,
            self.cola_urgente_eps,
        ]
        #Agrupa las colas de usuarios con prioridad normal
        colas_normales = [
            self.cola_normal_particular,
            self.cola_normal_prepagada,
            self.cola_normal_eps,
        ]

        todos_los_usuarios = []                                                 #Lista donde se almacenarán todos los usuarios de ambas categorías, con el fin de ordenar a los usuarios de fechas mas recientes a fechas mas lejanas

        for cola in colas_urgentes:                                             #Recorre cada una de las colas de atención urgente
            if cola:                                                            #Verifica si la cola tiene usuarios registrados
                for usuario in cola:                                            #Recorre toda la cola 
                    todos_los_usuarios.append((usuario, "URGENTE"))             #Agrega usuarios a la lista "todos_los_usuarios" para despues tratarlos

        for cola in colas_normales:                                             #Recorre cada una de las colas de atención normal
            if cola:                                                            #Verifica si la cola tiene usuarios registrados
                for usuario in cola:                                            #Recorre toda la cola 
                    todos_los_usuarios.append((usuario, "NORMAL"))              #Agrega usuarios a la lista "todos_los_usuarios" para despues tratarlos

        if not todos_los_usuarios:                                              #Se consulta si la lista "todos_los_usuarios" no esta vacia
            print(f"\n** La lista de usuarios está vacía.")                     #Si la lista esta vacia, muestra mensaje
            return                                                              #Sale de la funcion

        todos_los_usuarios.sort(key=lambda x: datetime.strptime(x[0].fecha, "%d/%m/%Y"))                                    #Se arregla la lista "todos_los_usuarios en orden de fecha mas reciente a fecha mas lejana"

        print(f"{'#':<4} {'Cédula':<12} {'Nombre':<22} { 'Telefono':<11} {'Tipo cliente':<15} {'Tipo atencion':<15} "       #Imprime encabezado de la tabla para mostrar cliente
                f"{'Cant':>6} {'Prioridad':>12}  {'Fecha':<12} {'Valor cita':>10} {'Valor atencion':>16} {'Total':>12}")    #Imprime encabezado de la tabla para mostrar cliente
            

        for i, (usuario, grupo) in enumerate(todos_los_usuarios, start=1):                                                  #Ciclo for para mostar la informacion de los usuarios en forma de tabla
            print(f"{i:<4} {usuario.cedula:<12} {usuario.nombre:<22} {usuario.telefono:<11} {usuario.tip_usuario:<15} {usuario.tip_atencion:<15} "
                f"{usuario.cantidad:>6} {usuario.prioridad:>12}  {usuario.fecha:<12} {fmt_cop(usuario.valor_cita):>10} {fmt_cop(usuario.valor_atencion):>16} "
                f"{fmt_cop(usuario.total):>12}")


    def atender_siguiente_usuario(self):
        titulo_a_mostrar("  ATENDER SIGUIENTE USUARIO.")                    #Muestrar titulo en terminal desde el modulo display.py  

        #Agrupa las colas de usuarios con prioridad urgente
        colas_urgentes = [
        self.cola_urgente_particular,
        self.cola_urgente_prepagada,
        self.cola_urgente_eps,
        ]
        #Agrupa las colas de usuarios con prioridad normal
        colas_normales = [
        self.cola_normal_particular,
        self.cola_normal_prepagada,
        self.cola_normal_eps,
        ]

    # Intentar atender colas de urgente si aún quedan turnos urgentes
        if self.grup_urgentes:                                                                          #Verifica si el grupo urgentes tiene usuarios registrados                
            atendido = False                                                                            #Predispone booleano para atender control Round Robin
            for cola in colas_urgentes:                                                                 #Recorre cada una de las colas de atención urgente
                if cola:                                                                                #Verifica si la cola tiene usuarios registrados
                    usuario = cola.popleft()                                                            #Desencola usuario de la cola y lo lamacena 
                    print(f"En el consultorio se atiende al usuario: {usuario.nombre} "                 #Muestra en en el terminal el usuario que se esta atendiendo
                         f"con procedimiento de {usuario.tip_atencion} por {usuario.tip_usuario}") 
                    atendido = True                                                                     #Predispone booleano
                    break

            if atendido:                                                                                #Verifica si es falso o verdadero
                self.colas_urgentes_cont += 1                                                           #Incrementa valor para el proceso del ciclo Round Robin "tras 3 usuarios urgentes, toca 1 normal"
                if self.colas_urgentes_cont >= 3:                                                       #Verifica si ya son 3 usuarios atendidos
                    self.colas_urgentes_cont = 0                                                        #Deja valor en cero
                    self.grup_urgentes = False                                                          #Predispone para ciclo de 3 urgentes, toca 1 normal
                return                                                                                  #Sale de la funcion
            else:
                # No hay urgentes, pasar directo a normales
                self.colas_urgentes_cont = 0                                                            #Deja valor en cero
                self.grup_urgentes = False                                                              #Predispone para ciclo de 3 urgentes, toca 1 normal

        # Atender 1 normal
        if not self.grup_urgentes:                                                                      #Verifica si el grupo urgentes tiene usuarios registrados 
            atendido = False                                                                            #Predispone booleano para atender control Round Robin
            for cola in colas_normales:                                                                 #Recorre cada una de las colas de atención urgente
                if cola:                                                                                #Verifica si la cola tiene usuarios registrados
                    usuario = cola.popleft()                                                            #Desencola usuario de la cola y lo lamacena
                    print(f"En el consultorio se atiende al usuario: {usuario.nombre} "                 #Muestra en en el terminal el usuario que se esta atendiendo
                         f"con procedimiento de {usuario.tip_atencion} por {usuario.tip_usuario}") 
                    atendido = True                                                                     #Predispone para indicar que hay usuario
                    break                                                                               #Sale del ciclo

            if not atendido:                                                                            #Consulta si ya no hay mas usuarios
                print("** No hay usuarios en cola.")                                                    #Mustra mensaje
            
            self.grup_urgentes = True                                                                   # Vuelve al ciclo de urgentes

  
    
    def consultar_siguiente_usuario(self):
        titulo_a_mostrar("  CONSULTAR SIGUIENTE USUARIO.")                                              #Muestrar titulo en terminal desde el modulo display.py 

        #Agrupa las colas de usuarios con prioridad urgente
        colas_urgentes = [
        self.cola_urgente_particular,
        self.cola_urgente_prepagada,
        self.cola_urgente_eps,
        ]
        #Agrupa las colas de usuarios con prioridad normal
        colas_normales = [
        self.cola_normal_particular,
        self.cola_normal_prepagada,
        self.cola_normal_eps,
        ]

        hay_urgentes = any(cola for cola in colas_urgentes)                                              #Verifica si al menos una de las colas urgentes contiene usuarios
        hay_normales = any(cola for cola in colas_normales)                                              #Verifica si al menos una de las colas normales contiene usuarios

        # Si no hay nadie en ninguna cola
        if not hay_urgentes and not hay_normales:
            print(f"** No hay usuarios en cola.")                                                        #Mustra mensaje
            return

        if self.grup_urgentes:                                                                           #Verifica si en el grupo urgentes hay usuarios si no pasa a grupo normales
            if hay_urgentes:                                                                             #Verifica si hay usuarios en una de la colas de urgentes
                for cola in colas_urgentes:                                                              #Recorre cada una de las colas de atención urgente
                    if cola:                                                                             #Verifica si la cola tiene usuarios registrados
                        usuario = cola[0]                                                                #Lee el usuario de la cola en la posicion cero y lo lamacena 
                        print(f"** El siguiente usuario es: {usuario.nombre} "                           #Muestra en en el terminal el usuario que se va a atender
                              f"con procedimiento de {usuario.tip_atencion} por {usuario.tip_usuario} de modo URGENTE") 
                        return                                                                          #Sale de la funcion
            elif hay_normales:                                                                          #Verifica si hay usuarios en una de la colas normales
                for cola in colas_normales:                                                             #Recorre cada una de las colas de atención normales
                    if cola:                                                                            #Verifica si la cola tiene usuarios registrados
                        usuario = cola[0]                                                               #Lee el usuario de la cola en la posicion cero y lo lamacena 
                        print(f"** El siguiente usuario es: {usuario.nombre} "                          #Muestra en en el terminal el usuario que se va a atender
                              f"con procedimiento de {usuario.tip_atencion} por {usuario.tip_usuario}") 
                        return                                                                          #Sale de la funcion
        else:                                                                                           #Salto a grupo normales
            if hay_normales:                                                                            #Verifica si hay usuarios en una de la colas normales
                for cola in colas_normales:                                                             #Recorre cada una de las colas de atención normales
                    if cola:                                                                            #Verifica si la cola tiene usuarios registrados
                        usuario = cola[0]                                                               #Lee el usuario de la cola en la posicion cero y lo lamacena
                        print(f"** El siguiente usuario es: {usuario.nombre} "                          #Muestra en en el terminal el usuario que se va a atender
                              f"con procedimiento de {usuario.tip_atencion} por {usuario.tip_usuario}") 
                        return                                                                          #Sale de la funcion
            elif hay_urgentes:                                                                          #Verifica si hay usuarios en una de la colas de urgentes
                for cola in colas_urgentes:                                                             #Recorre cada una de las colas de atención urgente
                    if cola:                                                                            #Verifica si la cola tiene usuarios registrados
                        usuario = cola[0]                                                               #Lee el usuario de la cola en la posicion cero y lo lamacena
                        print(f"** El siguiente usuario es: {usuario.nombre} "                          #Muestra en en el terminal el usuario que se va a atender
                              f"con procedimiento de {usuario.tip_atencion} por {usuario.tip_usuario} de modo URGENTE") 
                        return                                                                          #Sale de la funcion

    def estadistica_de_usuarios(self):
        #Variables para crear la estadistica
        total_usuarios_pendientes = 0
        total_usuarios_urgentes_pendientes = 0
        total_usuarios_no_urgentes_pendientes = 0
        numero_de_calzas_a_realizar = 0
        numero_extracciones_dentales = 0
        numero_limpiezas_a_realizar = 0
        numero_valoraciones_a_realizar = 0
        total_valor_procedimientos_pendientes = 0

        #Agrupa las colas de usuarios con prioridad urgente
        colas_urgentes = [
            self.cola_urgente_particular,
            self.cola_urgente_prepagada,
            self.cola_urgente_eps,
        ]
        #Agrupa las colas de usuarios con prioridad normal
        colas_normales = [
            self.cola_normal_particular,
            self.cola_normal_prepagada,
            self.cola_normal_eps,
        ]

        for cola in colas_urgentes:                                             #Cilco for para recorrer todas las colas del grupo urgente
            for usuario in cola:                                                #Ciclo for para recorrer la cola 
                total_usuarios_urgentes_pendientes += 1                         #Contabiliza usuarios
                if usuario.tip_atencion == "Limpieza":                          #Consulta el tipo de atencion del usuario
                    numero_limpiezas_a_realizar += usuario.cantidad             #Si es "Limpieza" incrementa la variable para la estadistica
                if usuario.tip_atencion == "Calzas":                            #Consulta el tipo de atencion del usuario
                    numero_de_calzas_a_realizar += usuario.cantidad             #Si es "Calzas" incrementa la variable para la estadistica
                if usuario.tip_atencion == "Diagnóstico":                       #Consulta el tipo de atencion del usuario
                    numero_valoraciones_a_realizar += usuario.cantidad          #Si es "Diagnostico" incrementa la variable para la estadistica
                numero_extracciones_dentales += usuario.cant_extraccion         #realiza conteo de extracciones dentales para la estadistica
                total_valor_procedimientos_pendientes += usuario.total          #Suma el valor total de cada usuario para la estadistica

        for cola in colas_normales:                                             #Cilco for para recorrer todas las colas del grupo normal
            for usuario in cola:                                                #Ciclo for para recorrer la cola 
                total_usuarios_no_urgentes_pendientes += 1                      #Contabiliza usuarios
                if usuario.tip_atencion == "Limpieza":                          #Consulta el tipo de atencion del usuario
                    numero_limpiezas_a_realizar += usuario.cantidad             #Si es "Limpieza" incrementa la variable para la estadistica
                if usuario.tip_atencion == "Calzas":                            #Consulta el tipo de atencion del usuario
                    numero_de_calzas_a_realizar += usuario.cantidad             #Si es "Calzas" incrementa la variable para la estadistica
                if usuario.tip_atencion == "Diagnóstico":                       #Consulta el tipo de atencion del usuario
                    numero_valoraciones_a_realizar += usuario.cantidad          #Si es "Diagnostico" incrementa la variable para la estadistica
                numero_extracciones_dentales += usuario.cant_extraccion         #realiza conteo de extracciones dentales para la estadistica
                total_valor_procedimientos_pendientes += usuario.total          #Suma el valor total de cada usuario para la estadistica

        total_usuarios_pendientes = total_usuarios_urgentes_pendientes + total_usuarios_no_urgentes_pendientes #Suma para saber la cantidad de usuarios pendientes

        titulo_a_mostrar("  ESTADISTICAS.")         #Muestrar titulo en terminal desde el modulo display.py 
        #Mustra la tabla de estadisticas del consultorio                                                       
        print(f"{'- Total usuarios urgentes pendientes es: ':<44}{total_usuarios_urgentes_pendientes:>10}")
        print(f"{'- Total usuarios no urgentes pendientes es: ':<42}{total_usuarios_no_urgentes_pendientes:>10}")
        print(f"{'- El total de usuarios pendientes es: ':<44}{total_usuarios_pendientes:>10}")
        print(f"{'- Numero de limpiezas a realizar es : ':<44}{numero_limpiezas_a_realizar:>10}")
        print(f"{'- Numero de calzas a realizar es: ':<44}{numero_de_calzas_a_realizar:>10}")
        print(f"{'- Numero de extracciones a realizar es: ':<44}{numero_extracciones_dentales:>10}")
        print(f"{'- Numero de diagnosticos a realizar es: ':<44}{numero_valoraciones_a_realizar:>10}")
        print(f"{'- El valor total de los procedimientos es: ':<44}{fmt_cop(total_valor_procedimientos_pendientes):>10}")
        return  #Sale de la funcion
    
    
        